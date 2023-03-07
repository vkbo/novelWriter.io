#!/usr/bin/env python3
"""
novelWriter.io Maintenance Script
"""

import re
import sys
import json
import shutil
import argparse
import urllib.request

from pathlib import Path
from datetime import datetime

from tools import DownloadAssets
from tools.assets import AssetType


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


def processReleaseNotes(text):
    """Format the release notes text.
    """
    def ghLinks(x):
        return f"`#{x.group(1)} <https://github.com/vkbo/novelWriter/issues/{x.group(1)}>`_"

    buffer = []
    buffer.append(".. dropdown:: Release Notes")
    buffer.append("   :animate: fade-in-slide-down")
    buffer.append("   :icon: info")
    buffer.append("")
    for line in text.splitlines():
        if line.startswith("###"):
            title = line.lstrip("#").lstrip()
            buffer.append(f"   .. rubric:: {title}")
        else:
            line = line.replace("`", "``")
            line = re.sub(r"#([0-9]+)\b", ghLinks, line)
            buffer.append(f"   {line}".rstrip())

    buffer.append("")

    return "\n".join(buffer)


##
#  Documentation
##

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
        ".. _main_documentation:",
        "",
        "#############",
        "Documentation",
        "#############",
    ] + indexText.splitlines()[3:]
    docsIndex.write_text("\n".join(newText), encoding="utf-8")

    print("")
    print("Docs updated")
    print("")

    return


##
#  Releases
##

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
    releaseNotes = data.get("body", "")
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
    assets = DownloadAssets(data)

    print("")

    # Update Files
    print("Updating Files")

    aAppImg = assets.getAsset(AssetType.APP_IMAGE)
    aDebian = assets.getAsset(AssetType.DEBIAN)
    aWinExe = assets.getAsset(AssetType.WINDOWS_EXE)
    aMacDmg = assets.getAsset(AssetType.MAC_DMG)

    if isPreRelease:
        # Updating Pre-Release Info
        buildFromTemplate("download_release.rst", "download_pre_release.rst", {
            "release_version": releaseVersion,
            "release_date": releaseDateFmt,
            "release_url": releaseUrl,
            "release_notes": processReleaseNotes(releaseNotes),
            "download_tabs": assets.generateDownloadTabs(
                f"novelWriter-{shortVersion}.zip", zipBall,
                f"novelWriter-{shortVersion}.tar.gz", tarBall
            ),
        })

    else:
        # Updating Latest Release Info
        buildFromTemplate("download_block.rst", "download_block.rst", {
            "release_version": releaseVersion,
            "release_date": releaseDateFmt,
            "release_url": releaseUrl,
            "appimage_download": aAppImg.assetUrl,
            "debian_download": aDebian.assetUrl,
            "winexe_download": aWinExe.assetUrl,
            "macdmg_download": aMacDmg.assetUrl,
        })

        buildFromTemplate("checksum_block.rst", "checksum_block.rst", {
            "appimage_name": aAppImg.assetName,
            "appimage_shasum": aAppImg.assetShaSum,
            "appimage_shasumfile": aAppImg.assetShaSumUrl,
            "debian_name": aDebian.assetName,
            "debian_shasum": aDebian.assetShaSum,
            "debian_shasumfile": aDebian.assetShaSumUrl,
            "winexe_name": aWinExe.assetName,
            "winexe_shasum": aWinExe.assetShaSum,
            "winexe_shasumfile": aWinExe.assetShaSumUrl,
            "macdmg_name": aMacDmg.assetName,
            "macdmg_shasum": aMacDmg.assetShaSum,
            "macdmg_shasumfile": aMacDmg.assetShaSumUrl,
        })

        buildFromTemplate("download_release.rst", "download_release.rst", {
            "release_version": releaseVersion,
            "release_date": releaseDateFmt,
            "release_url": releaseUrl,
            "release_notes": processReleaseNotes(releaseNotes),
            "download_tabs": assets.generateDownloadTabs(
                f"novelWriter-{shortVersion}.zip", zipBall,
                f"novelWriter-{shortVersion}.tar.gz", tarBall
            ),
        })

    print("")

    return


def buildFromTemplate(name, output, data):
    """Write data to a template.
    """
    output = output or name
    templateDir = Path("templates")
    generateDir = Path("source/generated")
    templateText = (templateDir / name).read_text().format(**data)
    if not output:
        return templateText
    (generateDir / output).write_text(templateText, encoding="utf-8")
    print(f"Updated: {generateDir / output}")
    return None


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
