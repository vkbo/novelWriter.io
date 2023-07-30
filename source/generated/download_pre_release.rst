.. _AppImage website: https://appimage.org/
.. _Ubuntu: https://ubuntu.com/
.. _Debian: https://www.debian.org/
.. _Linux Mint: https://linuxmint.com/
.. _novelWriter Repository: https://github.com/vkbo/novelWriter/

| **Release Version:** Version 2.1 Beta 1
| **Release Date:** July 30, 2023
| **Release Page:** :octicon:`mark-github` `GitHub <https://github.com/vkbo/novelWriter/releases/tag/v2.1b1>`__

.. dropdown:: Release Notes
   :animate: fade-in-slide-down
   :icon: info

   This is a beta release of the next release version, and is intended for testing purposes. Please be careful when using this version on live writing projects, and make sure you take frequent backups.

   Please check the changelog for an overview of changes. The full release notes will be added to the final release.

.. dropdown:: Detailed Changelog
   :animate: fade-in-slide-down
   :icon: tasklist

   **Usability**

   * When the main window is resized, the change in size is only assigned to the editor and viewer. To resize the project tree area, its slider needs to be moved. PR `#1388 <https://github.com/vkbo/novelWriter/issues/1388>`_.
   * The default text font on MacOS is now Helvetica instead of Courier. Issue `#1463 <https://github.com/vkbo/novelWriter/issues/1463>`_. PR `#1479 <https://github.com/vkbo/novelWriter/issues/1479>`_.
   * Backup files now contain the project name again. Issue `#1476 <https://github.com/vkbo/novelWriter/issues/1476>`_. PR `#1484 <https://github.com/vkbo/novelWriter/issues/1484>`_.
   * The backup success dialog now displays the file size of the backup file. Issue `#1453 <https://github.com/vkbo/novelWriter/issues/1453>`_. PR `#1484 <https://github.com/vkbo/novelWriter/issues/1484>`_.
   * New root folders in the Project Tree now appear next to the root folder of the item selected when the request to make the root folder was made. Previously, it would appear at the bottom of the Project Tree. Issue `#1259 <https://github.com/vkbo/novelWriter/issues/1259>`_. PR `#1487 <https://github.com/vkbo/novelWriter/issues/1487>`_.

   **Features**

   * A new Manuscript Build Tool has been added. The new tool allows for detailed handling of which documents are included in a build, as well as a much better tool for formatting headers. It also allows for saving multiple build presets. PRs `#1389 <https://github.com/vkbo/novelWriter/issues/1389>`_ and `#1466 <https://github.com/vkbo/novelWriter/issues/1466>`_. Issues `#971 <https://github.com/vkbo/novelWriter/issues/971>`_, `#1315 <https://github.com/vkbo/novelWriter/issues/1315>`_ and `#1448 <https://github.com/vkbo/novelWriter/issues/1448>`_.
   * Exported ODT documents now have an accessible style for scene separators. It is also possible to define page size and margin sizes from the new build tool. Issue `#622 <https://github.com/vkbo/novelWriter/issues/622>`_. PR `#1477 <https://github.com/vkbo/novelWriter/issues/1477>`_.
   * A proper light colour theme has been added. The default theme will usually default to light colours, but in Qt6 it will not depending on host OS settings, so creating a proper light theme is needed. This also allows for some tweaking of the colours. The contrast of the dark theme has been improved a bit as well, and a default icon theme is now selected based on the lightness of the background if an icon theme is not specified in the theme definition file. Issues `#1472 <https://github.com/vkbo/novelWriter/issues/1472>`_ and `#1473 <https://github.com/vkbo/novelWriter/issues/1473>`_. PR `#1475 <https://github.com/vkbo/novelWriter/issues/1475>`_.
   * Documents, folders and root folders can now be duplicated from the Project Tree, including all child elements. The duplicated content is stored next to the source items, and can then be moved to wherever the user wants a copy. Issue `#1469 <https://github.com/vkbo/novelWriter/issues/1469>`_. PR `#1480 <https://github.com/vkbo/novelWriter/issues/1480>`_.
   * A set of new keyboard shortcuts have been added to make some types of navigation in the Project Tree easier. ``Alt+Up`` and ``Alt+Down`` will move between sibling items in the tree, skipping child items. ``Alt+Left`` will move to the parent of the selected item without triggering the collapse of the node like the ``Left`` key does. ``Alt+Right`` does the reverse, and both expands the node and moves to the first child in one click. Issue `#1348 <https://github.com/vkbo/novelWriter/issues/1348>`_. PRs `#1488 <https://github.com/vkbo/novelWriter/issues/1488>`_ and `#1489 <https://github.com/vkbo/novelWriter/issues/1489>`_.

   **Packaging and Installation**

   * Support for Python 3.7 is no longer maintained, but has not officially been dropped. It is expected to be dropped for the final release of 2.1. PR `#1452 <https://github.com/vkbo/novelWriter/issues/1452>`_.
   * The ``lxml`` package has been removed from the source code, dropping it as a dependency of novelWriter. The standard Python ``xml`` library is used instead. The standard library is somewhat limited, which is why it wasn't originally used, but when dropping support for Python 3.7, it is now good alternative. Issue `#1257 <https://github.com/vkbo/novelWriter/issues/1257>`_. PR `#1452 <https://github.com/vkbo/novelWriter/issues/1452>`_.
   * The ``setup.py`` file has been removed. The custom packaging utilities in the old ``setup.py`` file are now available in ``pkgutils.py`` instead. Issues `#1437 <https://github.com/vkbo/novelWriter/issues/1437>`_ and `#1438 <https://github.com/vkbo/novelWriter/issues/1438>`_. PR `#1483 <https://github.com/vkbo/novelWriter/issues/1483>`_.

   **Code Improvements**

   * All imports of modules are now direct imports instead of going via init files. All subfolder init files have been reduced to empty files. PR `#1262 <https://github.com/vkbo/novelWriter/issues/1262>`_.
   * The mocking of the main config object in the test suite has been rewritten to be easier to deal with when writing tests. The new approach also removes the need to access the config object via an attribute in many classes, and is now instead accessed directly. This should give a tiny performance boost as a bonus. PR `#1447 <https://github.com/vkbo/novelWriter/issues/1447>`_.
   * The building of manuscript documents from novelWriter source text is now handled by a core builder class, thus separating it from any GUI module. Previously, this was baked into the build tool. PR `#1316 <https://github.com/vkbo/novelWriter/issues/1316>`_.
   * SVG icons have been optimised in terms of storage size and object complexity. PR `#1456 <https://github.com/vkbo/novelWriter/issues/1456>`_.
   * The file names for the project meta data files have been simplified and references to legacy formats removed. The wordlist has been converted to a JSON file, and the session log to a JSON Lines file. All old files are renamed or converted on the fly when opening the project. PR `#1464 <https://github.com/vkbo/novelWriter/issues/1464>`_.
   * The core project item and tree classes have been modified to improve how items, and in particular, orphaned items are handled. These are mostly internal changes that simplifies how items are accessed in the source code. Issue `#1481 <https://github.com/vkbo/novelWriter/issues/1481>`_. PR `#1482 <https://github.com/vkbo/novelWriter/issues/1482>`_.
   * Many of the above PRs adds type annotations to classes and functions in the source code. These will be added gradually to the entire source code going forward.

Linux
-----

**AppImage (Legacy)**
   For older Linux distros you may need to download this AppImage instead.

   | **Download:** :octicon:`download` `novelWriter-2.1b1-oldlinux.AppImage <https://github.com/vkbo/novelWriter/releases/download/v2.1b1/novelWriter-2.1b1-oldlinux.AppImage>`__ [ 93.5 MB ]
   | **Checksum:** :octicon:`hash` ``4ea2c35b66d5155bb77173071a1c4451f2ac3fa81303e1371135ab237fc91053`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.1b1/novelWriter-2.1b1-oldlinux.AppImage.sha256>`__

**Debian Package**
   The package is built for Debian_, but should also work for Ubuntu_ and `Linux Mint`_.

   | **Download:** :octicon:`download` `novelwriter_2.1b1_all.deb <https://github.com/vkbo/novelWriter/releases/download/v2.1b1/novelwriter_2.1b1_all.deb>`__ [ 1.95 MB ]
   | **Checksum:** :octicon:`hash` ``85c862591302362857400815fa5cee12a62e3ed01957e9f4c1776c6ef73297da`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.1b1/novelwriter_2.1b1_all.deb.sha256>`__


Windows
-------

**Setup Installer**
   This is a standard setup installer for Windows. It is made for Windows 10 or newer.

   | **Download:** :octicon:`download` `novelwriter-2.1b1-amd64-setup.exe <https://github.com/vkbo/novelWriter/releases/download/v2.1b1/novelwriter-2.1b1-amd64-setup.exe>`__ [ 31.4 MB ]
   | **Checksum:** :octicon:`hash` ``dd9abb65493ff50c22a2c992f7c1f3cac686832ea27030a0d10f2ae29801469f`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.1b1/novelwriter-2.1b1-amd64-setup.exe.sha256>`__


MacOS
-----

**DMG Image**
   This is a DMG image for MacOS, and should work on MacOS 10 or higher.

   | **Download:** :octicon:`download` `novelWriter-2.1b1.dmg <https://github.com/vkbo/novelWriter/releases/download/v2.1b1/novelWriter-2.1b1.dmg>`__ [ 91.1 MB ]
   | **Checksum:** :octicon:`hash` ``278d5eb20ece7ce51b822250540a6e80a215481b1446013d1d6772517df86b93`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.1b1/novelWriter-2.1b1.dmg.sha256>`__


Other Packages
--------------

**Python Wheel**
   The Wheel package can be installed with ``pip install <file_path>``.

   | **Download:** :octicon:`download` `novelWriter-2.1b1-py3-none-any.whl <https://github.com/vkbo/novelWriter/releases/download/v2.1b1/novelWriter-2.1b1-py3-none-any.whl>`__ [ 2.30 MB ]
   | **Checksum:** :octicon:`hash` ``a0b2c330d10380d951faf7e763a022dd90e0eb254e55e6a7845e0c5e92bae51e`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.1b1/novelWriter-2.1b1-py3-none-any.whl.sha256>`__

**Source Code**
The source code packages are archived files of the entire source code. See also the `novelWriter Repository`_.

| **Download:** :octicon:`download` `novelWriter-2.1b1.zip <https://api.github.com/repos/vkbo/novelWriter/zipball/v2.1b1>`__
| **Download:** :octicon:`download` `novelWriter-2.1b1.tar.gz <https://api.github.com/repos/vkbo/novelWriter/tarball/v2.1b1>`__

