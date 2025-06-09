#!/usr/bin/env python3
"""
novelWriter.io Maintenance Script
"""

import argparse
import json
import re
import sys
import urllib.request

from datetime import datetime
from pathlib import Path

from tools import AssetType, Documentation, DownloadAssets


def stripVersion(version: str) -> str:
    """Strip the pre-release part from a version number."""
    if "a" in version:
        return version.partition("a")[0]
    elif "b" in version:
        return version.partition("b")[0]
    elif "rc" in version:
        return version.partition("rc")[0]
    else:
        return version


def updateSetting(name: str, value: str) -> None:
    """Update a setting in the settings.json file."""
    setFile = Path("source/settings.json")
    if setFile.exists():
        settings = json.loads(setFile.read_text())
    else:
        settings = {}

    if isinstance(settings, dict):
        settings[name] = value
        setFile.write_text(json.dumps(settings, indent=2))

    return


def writeReleaseInfo(version: str, force: bool, info: dict[str, str | dict[str, str]]) -> None:
    """Write the release info file."""
    relFile = Path("source/_extra/release-latest.json")
    current = json.loads(relFile.read_text(encoding="utf-8")) if relFile.exists() else {}
    release = current.get("release", {})
    numeric = tuple(int(x) for x in f"{version}.0.0.0".split(".")[:3])
    previous = (release.get("major", 0), release.get("minor", 0), release.get("patch", 0))
    if previous > numeric and not force:
        print(("Current release info is for %s, not updating. "
               "Use --force to override.") % release.get("version", "0"))
        return
    relFile.write_text(
        json.dumps({
            "release": {
                "version": version,
                "major": numeric[0],
                "minor": numeric[1],
                "patch": numeric[2],
                "info": info,
            }
        }, indent=2), encoding="utf-8"
    )
    return


def processReleaseNotes(text):
    """Format the release notes text."""
    def ghLinks(x):
        return f"`#{x.group(1)} <https://github.com/vkbo/novelWriter/issues/{x.group(1)}>`_"

    buffer = []
    for line in text.splitlines():
        if line.startswith("### "):
            title = line.lstrip("#").lstrip()
            icon = None
            if "release" in title.lower():
                icon = "info"
            elif "changelog" in title.lower():
                icon = "tasklist"
            buffer.append(f".. dropdown:: {title.title()}")
            buffer.append("   :animate: fade-in-slide-down")
            if icon:
                buffer.append(f"   :icon: {icon}")
        elif line.startswith("#"):
            title = line.lstrip("#").lstrip()
            buffer.append(f"   **{title}**")
        elif line.startswith("_") and line.endswith("_"):
            text = line.strip("_")
            buffer.append(f"   *{text}*")
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
    """Download docs and extract them into the website source."""
    print("")
    print("Pulling Documentation Source")
    print("============================")
    print("")

    if args.branch:
        target = args.branch
        isBranch = True
    elif args.tag:
        target = args.tag
        isBranch = False
    else:
        print("ERROR: Not tag or branch specified")
        sys.exit(1)

    docs = Documentation(target, isBranch=isBranch)
    docs.pullDocs()
    docs.writeDocsCopy()

    updateSetting("docVersion", docs.release)

    print("")
    print("Docs updated")
    print("")

    return


##
#  Releases
##

def pullRelease(args):
    """Download release info from the GitHub API."""
    print("")
    print("Pulling Release Info")
    print("====================")
    print("")

    if args.remove_pre:
        print("Removing Pre-Release")
        Path("source/generated/download_pre_release.rst").write_text(
            "*There are currently no pre-release downloads available ...*", encoding="utf-8"
        )
        Path("source/generated/checksum_pre_release.rst").write_text(
            "", encoding="utf-8"
        )
        return

    print(f"Tag: {args.tag}")

    apiUrl = f"https://api.github.com/repos/vkbo/novelwriter/releases/tags/{args.tag}"
    urlReq = urllib.request.Request(apiUrl)
    urlReq.add_header("User-Agent", "Mozilla/5.0 (compatible; novelWriter (Python))")
    urlReq.add_header("Accept", "application/vnd.github.v3+json")

    urlData = urllib.request.urlopen(urlReq, timeout=10)
    data = json.loads(urlData.read().decode())

    outDir = Path("_temp")
    outDir.mkdir(exist_ok=True)
    with open(outDir / "api_data.json", mode="w") as apiDump:
        json.dump(data, apiDump, indent=2)

    discussUrl = data.get("discussion_url", "Unknown")
    releaseUrl = data.get("html_url", "Unknown")
    releaseVersion = data.get("name", "Version ???")
    releaseDate = data.get("published_at", "")
    shortVersion = data.get("tag_name", "???").lstrip("v")
    releaseRef = "main_release_" + "_".join(stripVersion(shortVersion).split(".")[:2])
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
    aMacAMD = assets.getAsset(AssetType.MAC_DMG_INTEL)
    aMacARM = assets.getAsset(AssetType.MAC_DMG_ARM)
    aPWheel = assets.getAsset(AssetType.PYTHON_WHEEL)

    if isPreRelease:
        # Updating Pre-Release Info
        buildFromTemplate("download_release.rst", "download_pre_release.rst", {
            "release_version": releaseVersion,
            "release_date": releaseDateFmt,
            "release_url": releaseUrl,
            "release_ref": releaseRef,
            "discuss_url": discussUrl,
            "appimage_name": aAppImg.assetName,
            "appimage_url": aAppImg.assetUrl,
            "appimage_size": aAppImg.assetSizeString,
            "appimage_shasumfile": aAppImg.assetShaSumUrl,
            "debian_name": aDebian.assetName,
            "debian_url": aDebian.assetUrl,
            "debian_size": aDebian.assetSizeString,
            "debian_shasumfile": aDebian.assetShaSumUrl,
            "winexe_name": aWinExe.assetName,
            "winexe_url": aWinExe.assetUrl,
            "winexe_size": aWinExe.assetSizeString,
            "winexe_shasumfile": aWinExe.assetShaSumUrl,
            "macx86_name": aMacAMD.assetName,
            "macx86_url": aMacAMD.assetUrl,
            "macx86_size": aMacAMD.assetSizeString,
            "macx86_shasumfile": aMacAMD.assetShaSumUrl,
            "macarm_name": aMacARM.assetName,
            "macarm_url": aMacARM.assetUrl,
            "macarm_size": aMacARM.assetSizeString,
            "macarm_shasumfile": aMacARM.assetShaSumUrl,
            "wheel_name": aPWheel.assetName,
            "wheel_url": aPWheel.assetUrl,
            "wheel_size": aPWheel.assetSizeString,
            "wheel_shasumfile": aPWheel.assetShaSumUrl,
            "short_version": shortVersion,
            "zip_url": zipBall,
            "tar_url": tarBall,
        })

        buildFromTemplate("checksum.rst", "checksum_pre_release.rst", {
            "appimage_name": aAppImg.assetName,
            "appimage_shasumfile": aAppImg.assetShaSumUrl,
            "debian_name": aDebian.assetName,
            "debian_shasumfile": aDebian.assetShaSumUrl,
            "winexe_name": aWinExe.assetName,
            "winexe_shasumfile": aWinExe.assetShaSumUrl,
            "macx86_name": aMacAMD.assetName,
            "macx86_shasumfile": aMacAMD.assetShaSumUrl,
            "macarm_name": aMacARM.assetName,
            "macarm_shasumfile": aMacARM.assetShaSumUrl,
        })

    else:
        # Write the release-info.json file
        writeReleaseInfo(shortVersion, args.force, {
            "name": releaseVersion,
            "date": releaseDate,
            "url": releaseUrl,
            "assets": {
                "appimage": aAppImg.assetUrl,
                "debian": aDebian.assetUrl,
                "winexe": aWinExe.assetUrl,
                "macx86": aMacAMD.assetUrl,
                "macarm": aMacARM.assetUrl,
                "zipball": zipBall,
                "tarball": tarBall,
            }
        })

        # Updating Latest Release Info
        buildFromTemplate("download.rst", "download_main.rst", {
            "release_version": releaseVersion,
            "release_date": releaseDateFmt,
            "release_ref": releaseRef,
            "appimage_download": aAppImg.assetUrl,
            "debian_download": aDebian.assetUrl,
            "winexe_download": aWinExe.assetUrl,
            "macx86_download": aMacAMD.assetUrl,
            "macarm_download": aMacARM.assetUrl,
        })

        buildFromTemplate("checksum.rst", "checksum_release.rst", {
            "appimage_name": aAppImg.assetName,
            "appimage_shasumfile": aAppImg.assetShaSumUrl,
            "debian_name": aDebian.assetName,
            "debian_shasumfile": aDebian.assetShaSumUrl,
            "winexe_name": aWinExe.assetName,
            "winexe_shasumfile": aWinExe.assetShaSumUrl,
            "macx86_name": aMacAMD.assetName,
            "macx86_shasumfile": aMacAMD.assetShaSumUrl,
            "macarm_name": aMacARM.assetName,
            "macarm_shasumfile": aMacARM.assetShaSumUrl,
        })

        buildFromTemplate("download_release.rst", "download_release.rst", {
            "release_version": releaseVersion,
            "release_date": releaseDateFmt,
            "release_url": releaseUrl,
            "release_ref": releaseRef,
            "discuss_url": discussUrl,
            "appimage_name": aAppImg.assetName,
            "appimage_url": aAppImg.assetUrl,
            "appimage_size": aAppImg.assetSizeString,
            "appimage_shasumfile": aAppImg.assetShaSumUrl,
            "debian_name": aDebian.assetName,
            "debian_url": aDebian.assetUrl,
            "debian_size": aDebian.assetSizeString,
            "debian_shasumfile": aDebian.assetShaSumUrl,
            "winexe_name": aWinExe.assetName,
            "winexe_url": aWinExe.assetUrl,
            "winexe_size": aWinExe.assetSizeString,
            "winexe_shasumfile": aWinExe.assetShaSumUrl,
            "macx86_name": aMacAMD.assetName,
            "macx86_url": aMacAMD.assetUrl,
            "macx86_size": aMacAMD.assetSizeString,
            "macx86_shasumfile": aMacAMD.assetShaSumUrl,
            "macarm_name": aMacARM.assetName,
            "macarm_url": aMacARM.assetUrl,
            "macarm_size": aMacARM.assetSizeString,
            "macarm_shasumfile": aMacARM.assetShaSumUrl,
            "wheel_name": aPWheel.assetName,
            "wheel_url": aPWheel.assetUrl,
            "wheel_size": aPWheel.assetSizeString,
            "wheel_shasumfile": aPWheel.assetShaSumUrl,
            "short_version": shortVersion,
            "zip_url": zipBall,
            "tar_url": tarBall,
        })

    print("")

    return


def buildFromTemplate(name, output, data):
    """Write data to a template."""
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
    pRelease.add_argument("--force", action="store_true", help="Force update of release info")
    pRelease.set_defaults(func=pullRelease)

    args = parser.parse_args()
    args.func(args)
