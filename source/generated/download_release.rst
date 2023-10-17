.. _AppImage website: https://appimage.org/
.. _Ubuntu: https://ubuntu.com/
.. _Debian: https://www.debian.org/
.. _Linux Mint: https://linuxmint.com/
.. _novelWriter Repository: https://github.com/vkbo/novelWriter/

| **Release Version:** Version 2.1
| **Release Date:** October 17, 2023
| **Release Page:** :octicon:`mark-github` `GitHub <https://github.com/vkbo/novelWriter/releases/tag/v2.1>`__

.. dropdown:: Release Notes
   :animate: fade-in-slide-down
   :icon: info

   The primary focus of this release has been a complete redesign of the Build Tool, that is, the tool that assembles your project into a manuscript document. The new tool, called the "Manuscript Build Tool" allows you to define multiple build definitions for your project. The build definitions are edited in a new Manuscript Build Settings dialog, with a lot more options than the old tool.

   The reason for this redesign is a long list of feature requests that could not easily be accommodated in the old, much simpler tool. Far from all the features have been added yet, but now that the new tool is in place, they will be gradually added in the coming releases.

   The key feature added in this release is the extended control you now have for selecting exactly what part of your project is included in a given build definition. You have the same filters for selecting documents and notes, and turning on or off root folders as before, but you can now easily override on a per-document basis what is included or excluded in addition to the filter.

   A second major improvement is a better tool to format your manuscript headings. You no longer have to look up formatting codes and add them manually. Instead, there is now a heading format editor in the Build Settings dialog for creating the header format, with syntax highlighting included.

   **Other Changes**

   Among other features is a new option to duplicate documents and folders in the project tree. The duplicate feature is available from the right-click menu. A proper light colour theme has also been added. In most cases it will be the same as the default theme, depending on your platform.

   There are other, minor improvements as well, and a lot of code improvements under the hood. For a full list of changes, see the detailed changelogs.

   *These Release Notes also include the changes from the 2.1 Beta 1 and 2.1 RC 1 releases.*

.. dropdown:: Detailed Changelog
   :animate: fade-in-slide-down
   :icon: tasklist

   **Usability**

   * A widget has been added to the Build Manuscript tool main window to show some select build settings for the selected build definition. This should make it a little easier to find the wanted build definition if there are many available. PR `#1516 <https://github.com/vkbo/novelWriter/issues/1516>`_.
   * All columns on the Writing Stats tool now uses the same fixed width font. Issue `#1442 <https://github.com/vkbo/novelWriter/issues/1442>`_, PR `#1518 <https://github.com/vkbo/novelWriter/issues/1518>`_.

   **Documentation**

   * The documentation has received significant updates for the 2.1 release. PR `#1531 <https://github.com/vkbo/novelWriter/issues/1531>`_.

   **Packaging and Installation**

   * Python 3.7 support has officially been dropped. Python 3.7 has reached end of life, and dropping it relaxes some restrictions on development. PR `#1515 <https://github.com/vkbo/novelWriter/issues/1515>`_.
   * MacOS and Windows is now tested against Python 3.11, and 3.12 has been added to Linux. PR `#1515 <https://github.com/vkbo/novelWriter/issues/1515>`_.

Linux
-----

**AppImage**
   The AppImage should run on any recent Linux distro. See the `AppImage website`_ for more info.

   | **Download:** :octicon:`download` `novelWriter-2.1.AppImage <https://github.com/vkbo/novelWriter/releases/download/v2.1/novelWriter-2.1.AppImage>`__ [ 94.7 MB ]
   | **Checksum:** :octicon:`hash` ``bdae7c23920097ff360b64937b999f8aaf42fa94c561dc6ffe2d80116ff21fb5`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.1/novelWriter-2.1.AppImage.sha256>`__

**AppImage (Legacy)**
   For older Linux distros you may need to download this AppImage instead.

   | **Download:** :octicon:`download` `novelWriter-2.1-oldlinux.AppImage <https://github.com/vkbo/novelWriter/releases/download/v2.1/novelWriter-2.1-oldlinux.AppImage>`__ [ 94.0 MB ]
   | **Checksum:** :octicon:`hash` ``b7ccf55fc2b46ddecfefad92065d3de31d8b3d644127d6f137d6e47fbb9b0612`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.1/novelWriter-2.1-oldlinux.AppImage.sha256>`__

**Debian Package**
   The package is built for Debian_, but should also work for Ubuntu_ and `Linux Mint`_.

   | **Download:** :octicon:`download` `novelwriter_2.1_all.deb <https://github.com/vkbo/novelWriter/releases/download/v2.1/novelwriter_2.1_all.deb>`__ [ 2.49 MB ]
   | **Checksum:** :octicon:`hash` ``66c4b1c0ca3c227c3f903cbb02b61024d0e5cc3846995d75f12c819e93e0c3b1`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.1/novelwriter_2.1_all.deb.sha256>`__


Windows
-------

**Setup Installer**
   This is a standard setup installer for Windows. It is made for Windows 10 or newer.

   | **Download:** :octicon:`download` `novelwriter-2.1-amd64-setup.exe <https://github.com/vkbo/novelWriter/releases/download/v2.1/novelwriter-2.1-amd64-setup.exe>`__ [ 34.9 MB ]
   | **Checksum:** :octicon:`hash` ``cc96f2fafc1c5210949c70e0e9bf2b5ed7fdc133880228441a5377876978a478`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.1/novelwriter-2.1-amd64-setup.exe.sha256>`__


MacOS
-----

**DMG Image**
   This is a DMG image for MacOS, and should work on MacOS 10 or higher.

   | **Download:** :octicon:`download` `novelWriter-2.1.dmg <https://github.com/vkbo/novelWriter/releases/download/v2.1/novelWriter-2.1.dmg>`__ [ 93.2 MB ]
   | **Checksum:** :octicon:`hash` ``e6d7cc7ef7ae84e8d23ec7c5d637752bf81a5224af5ebf748b1fb35e89bdcf7b`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.1/novelWriter-2.1.dmg.sha256>`__


Other Packages
--------------

**Python Wheel**
   The Wheel package can be installed with ``pip install <file_path>``.

   | **Download:** :octicon:`download` `novelWriter-2.1-py3-none-any.whl <https://github.com/vkbo/novelWriter/releases/download/v2.1/novelWriter-2.1-py3-none-any.whl>`__ [ 2.87 MB ]
   | **Checksum:** :octicon:`hash` ``dda7b8b991c35ce970e76b74b6b9d554c4f4c14a9845ae69d2763c2ef9a03809`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.1/novelWriter-2.1-py3-none-any.whl.sha256>`__

**Source Code**
The source code packages are archived files of the entire source code. See also the `novelWriter Repository`_.

| **Download:** :octicon:`download` `novelWriter-2.1.zip <https://api.github.com/repos/vkbo/novelWriter/zipball/v2.1>`__
| **Download:** :octicon:`download` `novelWriter-2.1.tar.gz <https://api.github.com/repos/vkbo/novelWriter/tarball/v2.1>`__

