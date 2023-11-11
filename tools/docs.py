"""
Custom code to handle documentation versions from the main repo.
"""

import shutil
import subprocess
import urllib.request

from pathlib import Path
from datetime import datetime

ROOT_DIR = Path(__file__).parent.parent


class Documentation:

    def __init__(self, target: str, isBranch=False):

        self._tag = None if isBranch else target
        self._branch = target if isBranch else None

        self._tempDir = ROOT_DIR / "_temp"
        self._extPath = self._tempDir / "novelWriter"
        self._tplPath = ROOT_DIR / "templates"
        self._dstPath = ROOT_DIR / "source" / "docs"
        self._pdfPath = ROOT_DIR / "source" / "about"

        self._nwRelease = "Unknown"
        self._nwDate = "1970-01-01"
        self._nwMajor = 0
        self._nwMinor = 0
        self._nwPatch = 0
        self._nwDev = ""

        return

    @property
    def release(self):
        return self._nwRelease

    def pullDocs(self):
        """Pull the archived version of the docs from GitHub."""
        if self._branch:
            dlUrl = f"https://github.com/vkbo/novelWriter/archive/refs/heads/{self._branch}.zip"
            dlZip = f"novelWriter-{self._branch}.zip"
            reUse = False
        elif self._tag:
            dlUrl = f"https://github.com/vkbo/novelWriter/archive/refs/tags/{self._tag}.zip"
            dlZip = f"novelWriter-{self._tag.lstrip('v')}.zip"
            reUse = True
        else:
            raise Exception("No tag or branch specified")

        outDir = ROOT_DIR / "_temp"
        self._tempDir.mkdir(exist_ok=True)

        zipFile = outDir / dlZip
        if not (zipFile.is_file() and reUse):
            print(f"Downloading: {dlUrl}")
            urllib.request.urlretrieve(dlUrl, zipFile)
        else:
            print(f"Using: {zipFile}")

        print("Extracting ... ", end="")
        self._extPath = outDir / zipFile.stem
        if self._extPath.exists():
            shutil.rmtree(self._extPath)
        shutil.unpack_archive(zipFile, outDir)
        print("Done")

        self._extractReleaseInfo()

        return

    def writeDocsCopy(self):
        """Write a copy of the documentation to the correct output
        folder.
        """
        docsSrc = self._extPath / "docs" / "source"
        docsDst = self._dstPath

        if self._dstPath.exists():
            print("Deleting Current Docs ... ", end="")
            shutil.rmtree(self._dstPath)
            print("Done")

        docsDst.mkdir()
        for item in docsSrc.iterdir():
            if item.is_file() and item.suffix in (".rst", ".pdf"):
                print(f"Copying: {item}")
                shutil.copyfile(item, docsDst / item.name)
            elif item.is_dir() and item.name == "images":
                print(f"Copying: {item}")
                shutil.copytree(item, docsDst / item.name)

        self._buildPdfManual()
        self._rewriteIndex(docsDst / "index.rst")
        self._createPdfPage()

        return

    ##
    #  Internal Functions
    ##

    def _buildPdfManual(self):
        """This function will build the documentation as manual.pdf."""
        buildDir = str(self._extPath / "docs")
        buildFile = self._extPath / "docs" / "build" / "latex" / "manual.pdf"
        buildFile.unlink(missing_ok=True)

        print("Building PDF manual ... ", end="")
        subprocess.call(["make", "clean"], cwd=buildDir)
        exCode = subprocess.call(
            ["make", "latexpdf"], cwd=buildDir,
            stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT
        )
        if exCode != 0:
            raise Exception(f"Build returned error code {exCode}")

        if buildFile.exists():
            newDoc = self._pdfPath / f"novelWriter-{self._nwMajor}.{self._nwMinor}.pdf"
            newDoc.unlink(missing_ok=True)
            buildFile.rename(newDoc)
            print("Done")
        else:
            print("FAILED")

        return

    def _createPdfPage(self):
        """Create the index of PDF manuals."""
        pdfs = []
        for item in self._pdfPath.iterdir():
            if item.is_file() and item.suffix == ".pdf":
                bits = item.stem[12:].split(".")
                key = f"{int(bits[0]):02d}.{int(bits[1]):03d}"
                pdfs.append((key, item.name))

        with open(self._pdfPath / "docs.rst", mode="w", encoding="utf-8") as of:
            of.write((self._tplPath / "about_docs.rst").read_text(encoding="utf-8"))
            of.write("\n")
            for _, pdf in sorted(pdfs, key=lambda x: x[0], reverse=True):
                of.write(f"| :download:`{pdf}`\n")
        return

    def _rewriteIndex(self, indexFile: Path):
        """Rewrite the index file with updated information."""
        relVersion = f"{self._nwMajor}.{self._nwMinor}"
        relDateStr = datetime.fromisoformat(self._nwDate).strftime("%A, %-d %B %Y")
        nowDateStr = datetime.now().strftime("%A, %-d %B %Y")

        if self._nwDev.startswith("alpha"):
            relVersionStr = f"{relVersion} (Development)"
            relDateStr = "Not Yet Released"
        elif self._nwDev:
            dev = self._nwDev.replace("rc", "RC ").replace("beta", "Beta ")
            relVersionStr = f"{relVersion} {dev} (Pre-Release)"
        elif self._nwPatch > 0:
            relVersionStr = f"{relVersion}.{self._nwPatch}"
        else:
            relVersionStr = relVersion

        indexText = indexFile.read_text(encoding="utf-8")
        indexBuffer = [
            ".. _main_documentation:",
            "",
            "*************",
            "Documentation",
            "*************",
            "",
            f"| **Release Version:** {relVersionStr}",
            f"| **Release Date:** {relDateStr}",
            f"| **Docs Updated:** {nowDateStr}",
            "",
            (
                f"**PDF:** :download:`novelWriter-{self._nwMajor}.{self._nwMinor}.pdf "
                f"<../about/novelWriter-{self._nwMajor}.{self._nwMinor}.pdf>` "
                "[ :ref:`Older Versions <main_about_docs>` ]"
            ),
            "",
        ]

        indexLines = indexText.splitlines()
        for n, line in enumerate(indexLines):
            if line.startswith("novelWriter is an"):
                indexBuffer += indexLines[n:]
                break
        else:
            raise Exception(f"Could not find beginning of body text in {indexFile}")

        indexFile.write_text("\n".join(indexBuffer), encoding="utf-8")

        return

    def _extractReleaseInfo(self):
        """Extract information about the release version and date."""
        print("Extracting Version Info ... ", end="")
        foundV = False
        foundD = False
        with open(self._extPath / "novelwriter" / "__init__.py") as inFile:
            for aLine in inFile:
                if aLine.startswith("__version__"):
                    self._nwRelease = aLine.split('"')[1].strip()
                    foundV = True
                elif aLine.startswith("__date__"):
                    self._nwDate = aLine.split('"')[1].strip()
                    foundD = True
                if foundV and foundD:
                    break
            else:
                raise Exception("Could not find release version and date")

        version, _, dev = self._nwRelease.partition("-")
        self._nwDev = dev
        bits = version.split(".")
        if len(bits) > 0:
            self._nwMajor = int(bits[0])
        if len(bits) > 1:
            self._nwMinor = int(bits[1])
        if len(bits) > 2:
            self._nwPatch = int(bits[2])

        print("Done")

        return

# END Class Documentation
