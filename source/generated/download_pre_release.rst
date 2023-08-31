.. _AppImage website: https://appimage.org/
.. _Ubuntu: https://ubuntu.com/
.. _Debian: https://www.debian.org/
.. _Linux Mint: https://linuxmint.com/
.. _novelWriter Repository: https://github.com/vkbo/novelWriter/

| **Release Version:** Release 2.1 RC 1
| **Release Date:** August 31, 2023
| **Release Page:** :octicon:`mark-github` `GitHub <https://github.com/vkbo/novelWriter/releases/tag/v2.1rc1>`__

.. dropdown:: Release Notes
   :animate: fade-in-slide-down
   :icon: info

   This is a release candidate of the next release version, and is intended for testing purposes. Please be careful when using this version on live writing projects, and make sure you take frequent backups.

   Please check the changelog for an overview of changes. The full release notes will be added to the final release.

.. dropdown:: Detailed Changelog
   :animate: fade-in-slide-down
   :icon: tasklist

   **Bugfixes**

   * Fixed an issue where closing modal dialogs would close their parent. Issue `#1494 <https://github.com/vkbo/novelWriter/issues/1494>`_. PR `#1496 <https://github.com/vkbo/novelWriter/issues/1496>`_.
   * The log output no longer prints an error message if the project does not have anything in its custom dictionary. PR `#1495 <https://github.com/vkbo/novelWriter/issues/1495>`_.

   **Usability**

   * novelWriter will no longer try to restore full screen mode if full screen was activated when it was last closed. This never worked right anyway. PR `#1498 <https://github.com/vkbo/novelWriter/issues/1498>`_.
   * There are several usability updates for the Build Settings tool. Please check the PR for details. Some key changes are that the build dialogs are now children of the main GUI, so they can be moved freely from each other. The Selection page has been given a new look that should hopefully make it easier to understand, and the side bar for the tool has been redesigned. A few labels have also been changed to be easier to understand. Issue `#1497 <https://github.com/vkbo/novelWriter/issues/1497>`_. PR `#1499 <https://github.com/vkbo/novelWriter/issues/1499>`_.
   * The alert and message boxes have been reimplemented with the full feature set of the Qt message box dialog instead of using the quick access functions with limited functionality. PR `#1501 <https://github.com/vkbo/novelWriter/issues/1501>`_.
   * A project's spell check dictionary can now be set directly from the Tools menu. Issue `#1260 <https://github.com/vkbo/novelWriter/issues/1260>`_. PR `#1508 <https://github.com/vkbo/novelWriter/issues/1508>`_.
   * The document details dialog box now shows a document's creation and update date if that has been set. Issue `#1423 <https://github.com/vkbo/novelWriter/issues/1423>`_. PR `#1510 <https://github.com/vkbo/novelWriter/issues/1510>`_.
   * Moving the mouse wheel on any area within the border of the text editor or viewer will now scroll the document. Issue `#1425 <https://github.com/vkbo/novelWriter/issues/1425>`_. PR `#1511 <https://github.com/vkbo/novelWriter/issues/1511>`_.

   **Code Improvements**

   * A new shared data instance now owns the Gui Theme, the Project class and holds a link to the main Gui instance as well. This new class also handles message and alert boxes. The project instance is now destroyed and recreated between each project close/open cycle. This should guard better from project to project data leakage. PRs `#1502 <https://github.com/vkbo/novelWriter/issues/1502>`_ and `#1504 <https://github.com/vkbo/novelWriter/issues/1504>`_.
   * The spell checker instance has been moved to the new shared data instance where it is destroyed and recreated together with the project instance. This blocks against bleed-through of the user's custom dictionary. PR `#1508 <https://github.com/vkbo/novelWriter/issues/1508>`_.
   * Text hash (SHA1) and creation and update time stamps are now added to the document file's meta data section. The hash is used to detect file changes outside of novelWriter while documents are open. The old checker has been deleted. Issue `#1423 <https://github.com/vkbo/novelWriter/issues/1423>`_. PR `#1509 <https://github.com/vkbo/novelWriter/issues/1509>`_.

Linux
-----

**AppImage**
   The AppImage should run on any recent Linux distro. See the `AppImage website`_ for more info.

   | **Download:** :octicon:`download` `novelWriter-2.1rc1.AppImage <https://github.com/vkbo/novelWriter/releases/download/v2.1rc1/novelWriter-2.1rc1.AppImage>`__ [ 93.8 MB ]
   | **Checksum:** :octicon:`hash` ``25809f2d0427851be9629fcd30efcd2aa38bdfa82b2ca63820c3c1a9b49e265e`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.1rc1/novelWriter-2.1rc1.AppImage.sha256>`__

**AppImage (Legacy)**
   For older Linux distros you may need to download this AppImage instead.

   | **Download:** :octicon:`download` `novelWriter-2.1rc1-oldlinux.AppImage <https://github.com/vkbo/novelWriter/releases/download/v2.1rc1/novelWriter-2.1rc1-oldlinux.AppImage>`__ [ 93.6 MB ]
   | **Checksum:** :octicon:`hash` ``32f712def7c4d90a1dc06cae23f99f7dd0d9a62c02373242957b2b0cc832db14`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.1rc1/novelWriter-2.1rc1-oldlinux.AppImage.sha256>`__

**Debian Package**
   The package is built for Debian_, but should also work for Ubuntu_ and `Linux Mint`_.

   | **Download:** :octicon:`download` `novelwriter_2.1rc1_all.deb <https://github.com/vkbo/novelWriter/releases/download/v2.1rc1/novelwriter_2.1rc1_all.deb>`__ [ 1.94 MB ]
   | **Checksum:** :octicon:`hash` ``577e163fd00ec862cfde1a326c94dd0d0d689a4991a1569a8862f6ef4594e38c`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.1rc1/novelwriter_2.1rc1_all.deb.sha256>`__


Windows
-------

**Setup Installer**
   This is a standard setup installer for Windows. It is made for Windows 10 or newer.

   | **Download:** :octicon:`download` `novelwriter-2.1rc1-amd64-setup.exe <https://github.com/vkbo/novelWriter/releases/download/v2.1rc1/novelwriter-2.1rc1-amd64-setup.exe>`__ [ 33.8 MB ]
   | **Checksum:** :octicon:`hash` ``42dd2ce94ec7b45be276d0fd92b1b585986e41a1e072492752a6e6d293290f1d`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.1rc1/novelwriter-2.1rc1-amd64-setup.exe.sha256>`__


MacOS
-----

**DMG Image**
   This is a DMG image for MacOS, and should work on MacOS 10 or higher.

   | **Download:** :octicon:`download` `novelWriter-2.1rc1.dmg <https://github.com/vkbo/novelWriter/releases/download/v2.1rc1/novelWriter-2.1rc1.dmg>`__ [ 91.1 MB ]
   | **Checksum:** :octicon:`hash` ``c248f858463b15ee65fb27270c11869c23cd78b71e2f74ef76dba4fcbcb2f205`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.1rc1/novelWriter-2.1rc1.dmg.sha256>`__


Other Packages
--------------

**Python Wheel**
   The Wheel package can be installed with ``pip install <file_path>``.

   | **Download:** :octicon:`download` `novelWriter-2.1rc1-py3-none-any.whl <https://github.com/vkbo/novelWriter/releases/download/v2.1rc1/novelWriter-2.1rc1-py3-none-any.whl>`__ [ 2.29 MB ]
   | **Checksum:** :octicon:`hash` ``78e8e4488e7cf7a68a0472a5ab358f402fa2a9f58743e4511a8f6cf07965cea3`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.1rc1/novelWriter-2.1rc1-py3-none-any.whl.sha256>`__

**Source Code**
The source code packages are archived files of the entire source code. See also the `novelWriter Repository`_.

| **Download:** :octicon:`download` `novelWriter-2.1rc1.zip <https://api.github.com/repos/vkbo/novelWriter/zipball/v2.1rc1>`__
| **Download:** :octicon:`download` `novelWriter-2.1rc1.tar.gz <https://api.github.com/repos/vkbo/novelWriter/tarball/v2.1rc1>`__

