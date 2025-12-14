"""
Custom code to handle assets from the GitHub API.
"""

import urllib.request

from enum import Enum
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent


class AssetType(Enum):

    NONE          = 0
    APP_IMAGE     = 1
    APP_IMAGE_OLD = 2
    DEBIAN        = 3
    DEBIAN_OLD    = 4
    WINDOWS_EXE   = 5
    MAC_DMG_INTEL = 6
    MAC_DMG_ARM   = 7
    PYTHON_WHEEL  = 8


class AssetOS(Enum):

    LINUX   = 0
    WINDOWS = 1
    MACOS   = 2
    OTHER   = 3


def fmtSize(size):
    """Formats a size with kB, MB, GB, etc."""
    value = float(size)
    for pF in ["k", "M", "G", "T", "P", "E"]:
        value /= 1000.0
        if value < 1000.0:
            if value < 10.0:
                return f"{value:.2f} {pF}B"
            elif value < 100.0:
                return f"{value:.1f} {pF}B"
            else:
                return f"{value:.0f} {pF}B"

    return str(value)


class Asset:

    def __init__(self, data):
        self._raw = data
        self._type = AssetType.NONE
        self._os = AssetOS.OTHER
        self._name = ""
        self._download = ""
        self._shasum = ""
        self._shasumUrl = ""
        self._size = -1
        self._processAsset()
        return

    @property
    def assetType(self):
        return self._type

    @property
    def assetOS(self):
        return self._os

    @property
    def assetName(self):
        return self._name

    @property
    def assetUrl(self):
        return self._download

    @property
    def assetShaSum(self):
        return self._shasum

    @property
    def assetShaSumUrl(self):
        return self._shasumUrl

    @property
    def assetSize(self):
        return self._size

    @property
    def assetSizeString(self):
        return fmtSize(self._size)

    def _processAsset(self):
        """Process the raw asset data."""
        data = self._raw
        name = data.get("name", "")
        if not name:
            return

        if name.endswith(".AppImage") and "oldlinux" in name:
            self._type = AssetType.APP_IMAGE_OLD
            self._os = AssetOS.LINUX
        elif name.endswith(".AppImage"):
            self._type = AssetType.APP_IMAGE
            self._os = AssetOS.LINUX
        elif name.endswith(".deb") and "oldstable" in name:
            self._type = AssetType.DEBIAN_OLD
            self._os = AssetOS.LINUX
        elif name.endswith(".deb"):
            self._type = AssetType.DEBIAN
            self._os = AssetOS.LINUX
        elif name.endswith("setup.exe"):
            self._type = AssetType.WINDOWS_EXE
            self._os = AssetOS.WINDOWS
        elif name.endswith(".dmg") and "x86_64" in name:
            self._type = AssetType.MAC_DMG_INTEL
            self._os = AssetOS.MACOS
        elif name.endswith(".dmg") and "aarch64" in name:
            self._type = AssetType.MAC_DMG_ARM
            self._os = AssetOS.MACOS
        elif name.endswith(".whl"):
            self._type = AssetType.PYTHON_WHEEL
            self._os = AssetOS.OTHER
        else:
            return

        self._name = name
        self._size = data.get("size", -1)
        self._download = data.get("browser_download_url")

        self._pullShaSum()

        return

    def _pullShaSum(self):
        """Retrieve the shasum file for the asset."""
        tempDir = ROOT_DIR / "_temp" / "shafiles"
        tempDir.mkdir(exist_ok=True)
        shaFile = tempDir / f"{self._name}.sha256"
        shaUrl = f"{self._download}.sha256"
        if shaFile.is_file():
            print(f"Found ShaSum: {shaFile.name}")
        else:
            urllib.request.urlretrieve(shaUrl, shaFile)
            print(f"Downloaded: {shaFile}")

        self._shasum = shaFile.read_text()[:64]
        self._shasumUrl = shaUrl

        return

# END Class DownloadAsset


class DownloadAssets:

    def __init__(self, data):
        self._raw = data
        self._assets: dict[AssetType, Asset | None] = {
            AssetType.APP_IMAGE:     None,
            AssetType.APP_IMAGE_OLD: None,
            AssetType.DEBIAN:        None,
            AssetType.DEBIAN_OLD:    None,
            AssetType.WINDOWS_EXE:   None,
            AssetType.MAC_DMG_INTEL: None,
            AssetType.MAC_DMG_ARM:   None,
            AssetType.PYTHON_WHEEL:  None,
        }
        for asset in data.get("assets", []):
            self._processAsset(asset)

        return

    def getAsset(self, assetType):
        """Return an asset from the records."""
        asset = self._assets.get(assetType, None)
        if isinstance(asset, Asset):
            return asset
        return Asset({})

    def _processAsset(self, data):
        """Process an asset."""
        asset = Asset(data)
        aType = asset.assetType
        if aType in self._assets:
            if self._assets[aType] is None:
                self._assets[aType] = asset
                print(f"Found Asset: {asset.assetName}")
            else:
                print(f"ERROR: Duplicate asset of type {aType.name}")
        return
