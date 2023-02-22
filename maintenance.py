#!/usr/bin/env python3
"""
novelWriter.io Maintenance Script
"""

import sys
import shutil
import argparse
import urllib.request

from pathlib import Path


def pullDocs(args):
    """Download docs from and extract them into the website source.
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

    print("")
    print("Docs updated")
    print("")

    return


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    subParsers = parser.add_subparsers()

    pDocs = subParsers.add_parser("docs")
    pDocs.add_argument("--branch", type=str, help="Pull docs from a specific branch")
    pDocs.add_argument("--tag", type=str, help="Pull docs from a specific tag")
    pDocs.set_defaults(func=pullDocs)

    args = parser.parse_args()
    args.func(args)
