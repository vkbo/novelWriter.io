#!/usr/bin/env python3
"""
novelWriter.io Maintenance Script
"""

import sys
import json
import shutil
import argparse
import urllib.request

from pathlib import Path
from datetime import datetime


def updateSetting(name, value):
    """Update a setting in the settings.json file.
    """
    setFile = Path("source/settings.json")
    if setFile.exists():
        settings = json.loads(setFile.read_text())
    else:
        settings = {}

    if isinstance(settings, dict):
        settings[name] = value
        setFile.write_text(json.dumps(settings, indent=2))

    return


def fmtSize(size):
    """Formats a size with kB, MB, GB, etc.
    """
    value = float(size)
    for pF in ["k", "M", "G", "T", "P", "E"]:
        value /= 1000.0
        if value < 1000.0:
            if value < 10.0:
                return f"{value:5.2f} {pF}B"
            elif value < 100.0:
                return f"{value:5.1f} {pF}B"
            else:
                return f"{value:3.0f} {pF}B"

    return str(value)


def pullDocs(args):
    """Download docs and extract them into the website source.
    """
    print("")
    print("Pulling Documentation Source")
    print("============================")
    print("")

    dlUrl = ""
    dlZip = ""
    if args.branch:
        dlUrl = f"https://github.com/vkbo/novelWriter/archive/refs/heads/{args.branch}.zip"
        dlZip = f"novelWriter-{args.branch}.zip"
    elif args.tag:
        dlUrl = f"https://github.com/vkbo/novelWriter/archive/refs/tags/{args.tag}.zip"
        dlZip = f"novelWriter-{args.tag.lstrip('v')}.zip"
    else:
        print("ERROR: Not tag or branch specified")
        sys.exit(1)

    outDir = Path("_temp")
    outDir.mkdir(exist_ok=True)

    print(f"Downloading: {dlUrl}")
    zipFile = outDir / dlZip
    urllib.request.urlretrieve(dlUrl, zipFile)

    extPath = outDir / zipFile.stem
    docsSrc = extPath / "docs" / "source"
    docsDst = Path("source/docs")

    print("Extracting ... ", end="")
    if extPath.exists():
        shutil.rmtree(extPath)
    shutil.unpack_archive(zipFile, outDir)
    print("Done")

    release = "unknown"
    with open(extPath / "novelwriter" / "__init__.py") as inFile:
        for aLine in inFile:
            if aLine.startswith("__version__"):
                release = aLine.split('"')[1].strip()
                break

    updateSetting("docVersion", release)
    print(f"Release: {release}")

    if docsDst.exists():
        print("Deleting old docs ... ", end="")
        shutil.rmtree(docsDst)
        print("Done")

    docsDst.mkdir()
    for item in docsSrc.iterdir():
        if item.is_file() and item.suffix in (".rst", ".pdf"):
            print(f"Copying: {item}")
            shutil.copyfile(item, docsDst / item.name)
        elif item.is_dir() and item.name == "images":
            print(f"Copying: {item}")
            shutil.copytree(item, docsDst / item.name)

    # Change the Main Heading
    docsIndex = docsDst / "index.rst"
    indexText = docsIndex.read_text(encoding="utf-8")
    newText = [
        "#############",
        "Documentation",
        "#############",
    ] + indexText.splitlines()[3:]
    docsIndex.write_text("\n".join(newText), encoding="utf-8")

    print("")
    print("Docs updated")
    print("")

    return


def pullRelease(args):
    """Download release info from the GitHub API.
    """
    print("")
    print("Pulling Release Info")
    print("====================")
    print("")

    if args.remove_pre:
        print("Removing Pre-Release")
        Path("source/generated/download_pre_release.rst").write_text(
            "*There are currently no pre-releases available ...*", encoding="utf-8"
        )
        return

    print(f"Tag: {args.tag}")

    apiUrl = f"https://api.github.com/repos/vkbo/novelwriter/releases/tags/{args.tag}"
    urlReq = urllib.request.Request(apiUrl)
    urlReq.add_header("User-Agent", "Mozilla/5.0 (compatible; novelWriter (Python))")
    urlReq.add_header("Accept", "application/vnd.github.v3+json")

    urlData = urllib.request.urlopen(urlReq, timeout=10)
    data = json.loads(urlData.read().decode())
    print(json.dumps(data, indent=2))

    releaseUrl = data.get("html_url", "Unkown")
    releaseVersion = data.get("name", "Version ???")
    releaseDate = data.get("published_at", "")
    shortVersion = data.get("tag_name", "???").lstrip("v")
    # releaseNote = data.get("body", "")
    isPreRelease = data.get("prerelease", False)
    tarBall = data.get("tarball_url", "")
    zipBall = data.get("zipball_url", "")
    print(f"Release URL:     {releaseUrl}")
    print(f"Release Version: {releaseVersion}")
    print(f"Release Short:   {shortVersion}")
    print(f"Release Date:    {releaseDate}")
    print(f"Release TarBall: {tarBall}")
    print(f"Release ZipBall: {zipBall}")
    print("")

    releaseDateFmt = datetime.fromisoformat(releaseDate).strftime("%B %-d, %Y")

    pkgFiles = {}
    shaFiles = {}
    shaSums = {}

    def processAsset(asset):
        return {
            "name": asset.get("name"),
            "download": asset.get("browser_download_url"),
            "size": asset.get("size", -1),
        }

    for asset in data.get("assets", []):
        assetName = asset.get("name")
        if not assetName:
            continue

        if assetName.endswith(".deb"):
            print(f"Found Asset: {assetName}")
            pkgFiles["Debian"] = processAsset(asset)
        elif assetName.endswith(".AppImage"):
            print(f"Found Asset: {assetName}")
            pkgFiles["AppImage"] = processAsset(asset)
        elif assetName.endswith("setup.exe"):
            print(f"Found Asset: {assetName}")
            pkgFiles["WinExe"] = processAsset(asset)
        elif assetName.endswith(".dmg"):
            print(f"Found Asset: {assetName}")
            pkgFiles["MacDMG"] = processAsset(asset)
        elif assetName.endswith(".whl"):
            print(f"Found Asset: {assetName}")
            pkgFiles["Wheel"] = processAsset(asset)
        elif assetName.endswith(".sha256"):
            shaFiles[assetName] = asset.get("browser_download_url", "error")

    # Download ShaSum Files
    print("")
    print("Checking Sha Files")
    tempDir = Path("_temp/shafiles")
    tempDir.mkdir(exist_ok=True)
    for shaFile, shaUrl in shaFiles.items():
        shaPath = tempDir / shaFile
        if shaPath.is_file():
            print(f"Found: {shaFile}")
        else:
            urllib.request.urlretrieve(shaUrl, shaPath)
            print(f"Downloaded: {shaFile}")

        shaData = shaPath.read_text()
        shaSums[shaData[66:].rstrip()] = shaData[:64]

    print("")

    # Update Files
    print("Updating Files")

    nmAppImage = pkgFiles["AppImage"]["name"]
    nmDebian = pkgFiles["Debian"]["name"]
    nmWinExe = pkgFiles["WinExe"]["name"]
    nmMacDMG = pkgFiles["MacDMG"]["name"]
    nmWheel = pkgFiles["Wheel"]["name"]

    if isPreRelease:
        # Updating Pre-Release Info
        buildFromTemplate("download_release.rst", {
            "release_version": releaseVersion,
            "release_date": releaseDateFmt,
            "release_url": releaseUrl,
            "appimage_name": nmAppImage,
            "appimage_size": fmtSize(pkgFiles["AppImage"]["size"]),
            "appimage_shasum": shaSums[nmAppImage],
            "appimage_download": pkgFiles["AppImage"]["download"],
            "appimage_shasumfile": shaFiles[f"{nmAppImage}.sha256"],
            "debian_name": nmDebian,
            "debian_size": fmtSize(pkgFiles["Debian"]["size"]),
            "debian_shasum": shaSums[nmDebian],
            "debian_download":  pkgFiles["Debian"]["download"],
            "debian_shasumfile": shaFiles[f"{nmDebian}.sha256"],
            "winexe_name": nmWinExe,
            "winexe_size": fmtSize(pkgFiles["WinExe"]["size"]),
            "winexe_shasum": shaSums[nmWinExe],
            "winexe_download":  pkgFiles["WinExe"]["download"],
            "winexe_shasumfile": shaFiles[f"{nmWinExe}.sha256"],
            "macdmg_name": nmMacDMG,
            "macdmg_size": fmtSize(pkgFiles["MacDMG"]["size"]),
            "macdmg_shasum": shaSums[nmMacDMG],
            "macdmg_download":  pkgFiles["MacDMG"]["download"],
            "macdmg_shasumfile": shaFiles[f"{nmMacDMG}.sha256"],
            "wheel_name": nmWheel,
            "wheel_size": fmtSize(pkgFiles["Wheel"]["size"]),
            "wheel_shasum": shaSums[nmWheel],
            "wheel_download":  pkgFiles["Wheel"]["download"],
            "wheel_shasumfile": shaFiles[f"{nmWheel}.sha256"],
            "srczip_name": f"novelWriter-{shortVersion}.zip",
            "srczip_download": zipBall,
            "srctar_name": f"novelWriter-{shortVersion}.tar.gz",
            "srctar_download": tarBall,
        }, "download_pre_release.rst")

    else:
        # Updating Latest Release Info
        buildFromTemplate("download_block.rst", {
            "release_version": releaseVersion,
            "release_date": releaseDateFmt,
            "release_url": releaseUrl,
            "appimage_download": pkgFiles["AppImage"]["download"],
            "debian_download":  pkgFiles["Debian"]["download"],
            "winexe_download": pkgFiles["WinExe"]["download"],
            "macdmg_download": pkgFiles["MacDMG"]["download"],
        })

        buildFromTemplate("checksum_block.rst", {
            "appimage_name": nmAppImage,
            "appimage_shasum": shaSums[nmAppImage],
            "appimage_shasumfile": shaFiles[f"{nmAppImage}.sha256"],
            "debian_name": nmDebian,
            "debian_shasum": shaSums[nmDebian],
            "debian_shasumfile": shaFiles[f"{nmDebian}.sha256"],
            "winexe_name": nmWinExe,
            "winexe_shasum": shaSums[nmWinExe],
            "winexe_shasumfile": shaFiles[f"{nmWinExe}.sha256"],
            "macdmg_name": nmMacDMG,
            "macdmg_shasum": shaSums[nmMacDMG],
            "macdmg_shasumfile": shaFiles[f"{nmMacDMG}.sha256"],
        })

        buildFromTemplate("download_release.rst", {
            "release_version": releaseVersion,
            "release_date": releaseDateFmt,
            "release_url": releaseUrl,
            "appimage_name": nmAppImage,
            "appimage_size": fmtSize(pkgFiles["AppImage"]["size"]),
            "appimage_shasum": shaSums[nmAppImage],
            "appimage_download": pkgFiles["AppImage"]["download"],
            "appimage_shasumfile": shaFiles[f"{nmAppImage}.sha256"],
            "debian_name": nmDebian,
            "debian_size": fmtSize(pkgFiles["Debian"]["size"]),
            "debian_shasum": shaSums[nmDebian],
            "debian_download":  pkgFiles["Debian"]["download"],
            "debian_shasumfile": shaFiles[f"{nmDebian}.sha256"],
            "winexe_name": nmWinExe,
            "winexe_size": fmtSize(pkgFiles["WinExe"]["size"]),
            "winexe_shasum": shaSums[nmWinExe],
            "winexe_download":  pkgFiles["WinExe"]["download"],
            "winexe_shasumfile": shaFiles[f"{nmWinExe}.sha256"],
            "macdmg_name": nmMacDMG,
            "macdmg_size": fmtSize(pkgFiles["MacDMG"]["size"]),
            "macdmg_shasum": shaSums[nmMacDMG],
            "macdmg_download":  pkgFiles["MacDMG"]["download"],
            "macdmg_shasumfile": shaFiles[f"{nmMacDMG}.sha256"],
            "wheel_name": nmWheel,
            "wheel_size": fmtSize(pkgFiles["Wheel"]["size"]),
            "wheel_shasum": shaSums[nmWheel],
            "wheel_download":  pkgFiles["Wheel"]["download"],
            "wheel_shasumfile": shaFiles[f"{nmWheel}.sha256"],
            "srczip_name": f"novelWriter-{shortVersion}.zip",
            "srczip_download": zipBall,
            "srctar_name": f"novelWriter-{shortVersion}.tar.gz",
            "srctar_download": tarBall,
        })

    print("")

    return


def buildFromTemplate(name, data, output=None):
    """Write data to a template.
    """
    output = output or name
    templateDir = Path("templates")
    generateDir = Path("source/generated")
    templateText = (templateDir / name).read_text().format(**data)
    (generateDir / output).write_text(templateText, encoding="utf-8")
    print(f"Updated: {generateDir / output}")
    return


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    subParsers = parser.add_subparsers()

    pDocs = subParsers.add_parser("docs", help="Update documentation")
    pDocs.add_argument("--branch", type=str, help="Pull docs from a specific branch")
    pDocs.add_argument("--tag", type=str, help="Pull docs from a specific tag")
    pDocs.set_defaults(func=pullDocs)

    pRelease = subParsers.add_parser("release", help="Update release")
    pRelease.add_argument("--tag", type=str, help="Pull release info from a specific tag")
    pRelease.add_argument("--remove-pre", action="store_true", help="Remove pre release")
    pRelease.set_defaults(func=pullRelease)

    args = parser.parse_args()
    args.func(args)
