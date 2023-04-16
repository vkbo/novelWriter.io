.. _AppImage website: https://appimage.org/
.. _Ubuntu: https://ubuntu.com/
.. _Debian: https://www.debian.org/
.. _Linux Mint: https://linuxmint.com/
.. _novelWriter Repository: https://github.com/vkbo/novelWriter/

| **Release Version:** Version 2.0.7
| **Release Date:** April 16, 2023
| **Release Page:** :octicon:`mark-github` `GitHub <https://github.com/vkbo/novelWriter/releases/tag/v2.0.7>`__

.. dropdown:: Release Notes
   :animate: fade-in-slide-down
   :icon: info

   This is a patch release that fixes a few issues and adds a Japanese translation.

   The issues were mostly related to spell checking. In particular, issues with finding the word boundary when using underscore characters for italics markup. These issues should now be resolved. In addition, escaped markup characters are now rendered properly in HTML and ODT build formats.

   A few usability improvements have also been made. The Add Item menu in the project tree no longer shows the options to create Novel Documents when an item in the tree is selected that cannot hold such a document. In addition, the "Change Label" context menu entry has been changed to say "Rename", which is a more logical choice.

.. dropdown:: Detailed Changelog
   :animate: fade-in-slide-down
   :icon: tasklist

   **Bugfixes**

   * Fixed an issue where novelWriter sometimes shows up in the desktop environment on Linux under another name than it's supposed to, which meant it would show up without the correct icon. The desktop environment was apparently guessing its name based on various values. It is now set explicitly. PR `#1405 <https://github.com/vkbo/novelWriter/issues/1405>`_.
   * Fixed an issue where the syntax highlighting for spell checked words were not cleared when spell checking was disabled. Issue `#1414 <https://github.com/vkbo/novelWriter/issues/1414>`_. PR `#1416 <https://github.com/vkbo/novelWriter/issues/1416>`_.
   * Fixed a series of issues with spell checking of words and sentences with italics styling using underscores. The spell checker relies on RegEx for splitting words, and RegEx considers the underscore a word character. Issue `#1415 <https://github.com/vkbo/novelWriter/issues/1415>`_. PR `#1417 <https://github.com/vkbo/novelWriter/issues/1417>`_.
   * Fixed an issue where escaped markup characters were not being cleaned up when building HTML and ODT outputs. Issue `#1412 <https://github.com/vkbo/novelWriter/issues/1412>`_. PR `#1418 <https://github.com/vkbo/novelWriter/issues/1418>`_.

   **Usability Fixes**

   * The context menu entry "Change Label" in the project tree has now been changed to say "Rename", which matches with the main menu, and is also more in line with what users expect. PR `#1403 <https://github.com/vkbo/novelWriter/issues/1403>`_.
   * The entries for creating new Novel Documents in the project tree's Add Item menu are now hidden when the select item in the tree does not allow Novel Documents. This is less confusing than the previous behaviour where it would just create a Project Note regardless of selected file option. Issue `#1404 <https://github.com/vkbo/novelWriter/issues/1404>`_. PR `#1406 <https://github.com/vkbo/novelWriter/issues/1406>`_.

   **Internationalisation**

   * Added Japanese translation, contributed by @hebekeg. PR `#1407 <https://github.com/vkbo/novelWriter/issues/1407>`_.
   * Updated existing translations. PR `#1407 <https://github.com/vkbo/novelWriter/issues/1407>`_.

   **Packaging**

   * Legacy AppImage formats have been added to support glibc 2.24. This is a temporary solution until the AppImage base image is deprecated later in 2023. Issue `#1391 <https://github.com/vkbo/novelWriter/issues/1391>`_. PR `#1410 <https://github.com/vkbo/novelWriter/issues/1410>`_.

Linux
-----

**AppImage**
   The AppImage should run on any recent Linux distro. See the `AppImage website`_ for more info.

   | **Download:** :octicon:`download` `novelWriter-2.0.7-py3.10-manylinux_2_28_x86_64.AppImage <https://github.com/vkbo/novelWriter/releases/download/v2.0.7/novelWriter-2.0.7-py3.10-manylinux_2_28_x86_64.AppImage>`__ [ 99.1 MB ]
   | **Checksum:** :octicon:`hash` ``a493fbdb16f4ee9d63bf42568a0d057f9093fa9c69f9a6ba1d6c043673c3b2a4`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.0.7/novelWriter-2.0.7-py3.10-manylinux_2_28_x86_64.AppImage.sha256>`__

**AppImage (Legacy)**
   For older Linux distros you may need to download this AppImage instead.

   | **Download:** :octicon:`download` `novelWriter-2.0.7-py3.10-manylinux_2_24_x86_64.AppImage <https://github.com/vkbo/novelWriter/releases/download/v2.0.7/novelWriter-2.0.7-py3.10-manylinux_2_24_x86_64.AppImage>`__ [ 100 MB ]
   | **Checksum:** :octicon:`hash` ``9f243a7bad56aa765dd1142ae2bccaedf2dba6e22e88038440f0698629ca6b02`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.0.7/novelWriter-2.0.7-py3.10-manylinux_2_24_x86_64.AppImage.sha256>`__

**Debian Package**
   The package is built for Debian_, but should also work for Ubuntu_ and `Linux Mint`_.

   | **Download:** :octicon:`download` `novelwriter_2.0.7_all.deb <https://github.com/vkbo/novelWriter/releases/download/v2.0.7/novelwriter_2.0.7_all.deb>`__ [ 1.94 MB ]
   | **Checksum:** :octicon:`hash` ``aeaa3e1bc797ea1527313e4b64b691a516b013e0e5d160e4644421881162736f`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.0.7/novelwriter_2.0.7_all.deb.sha256>`__


Windows
-------

**Setup Installer**
   This is a standard setup installer for Windows. It is made for Windows 10 or newer.

   | **Download:** :octicon:`download` `novelwriter-2.0.7-py3.10.11-win10-amd64-setup.exe <https://github.com/vkbo/novelWriter/releases/download/v2.0.7/novelwriter-2.0.7-py3.10.11-win10-amd64-setup.exe>`__ [ 33.5 MB ]
   | **Checksum:** :octicon:`hash` ``342f4257bfbcbfa5fc0655c7f7c980c94fbc94967f0f91d2bc71d8a2b872ac88`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.0.7/novelwriter-2.0.7-py3.10.11-win10-amd64-setup.exe.sha256>`__


MacOS
-----

**DMG Image**
   This is a DMG image for MacOS, and should work on MacOS 10 or higher.

   | **Download:** :octicon:`download` `novelWriter-2.0.7-macos.dmg <https://github.com/vkbo/novelWriter/releases/download/v2.0.7/novelWriter-2.0.7-macos.dmg>`__ [ 96.0 MB ]
   | **Checksum:** :octicon:`hash` ``9e5fc4fd03e636f64e7b6ae38e52190f21d76b62a4519a746f853d4ebdeec3a0`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.0.7/novelWriter-2.0.7-macos.dmg.sha256>`__


Other Packages
--------------

**Python Wheel**
   The Wheel package can be installed with ``pip install <file_path>``.

   | **Download:** :octicon:`download` `novelWriter-2.0.7-py3-none-any.whl <https://github.com/vkbo/novelWriter/releases/download/v2.0.7/novelWriter-2.0.7-py3-none-any.whl>`__ [ 2.31 MB ]
   | **Checksum:** :octicon:`hash` ``28c4aca900afa65132f8be0c3bc164c4df2deaca399262499c3e270fcdbb98ac`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.0.7/novelWriter-2.0.7-py3-none-any.whl.sha256>`__

**Source Code**
The source code packages are archived files of the entire source code. See also the `novelWriter Repository`_.

| **Download:** :octicon:`download` `novelWriter-2.0.7.zip <https://api.github.com/repos/vkbo/novelWriter/zipball/v2.0.7>`__
| **Download:** :octicon:`download` `novelWriter-2.0.7.tar.gz <https://api.github.com/repos/vkbo/novelWriter/tarball/v2.0.7>`__

