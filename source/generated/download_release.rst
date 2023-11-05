.. _AppImage website: https://appimage.org/
.. _Ubuntu: https://ubuntu.com/
.. _Debian: https://www.debian.org/
.. _Linux Mint: https://linuxmint.com/
.. _novelWriter Repository: https://github.com/vkbo/novelWriter/

| **Release Version:** Version 2.1.1
| **Release Date:** November 5, 2023
| **Release Page:** :octicon:`mark-github` `GitHub <https://github.com/vkbo/novelWriter/releases/tag/v2.1.1>`__

.. dropdown:: Release Notes
   :animate: fade-in-slide-down
   :icon: info

   This is a patch release that fixes a layout issue and internationalisation issues with the new Manuscript Build tool. It also fixes a number of issues related to bugs in the underlying Qt framework that affects drag and drop functionality in the project tree. These issues were mostly
   only affecting Debian Linux package releases.

   Other, minor issues related to updating the editor on colour theme change and project word list changes have been fixed as well. See the full changelog for more details.

.. dropdown:: Detailed Changelog
   :animate: fade-in-slide-down
   :icon: tasklist

   **Bugfixes**

   * Fix an issue with width of the last two columns on Selection page of the Build Settings dialog on Windows. They were far too wide by default. Issue `#1551 <https://github.com/vkbo/novelWriter/issues/1551>`_. PR `#1553 <https://github.com/vkbo/novelWriter/issues/1553>`_.
   * Fix an issue where a lot of string were not translated to the UI language in the new Manuscript Build tool. Issue `#1563 <https://github.com/vkbo/novelWriter/issues/1563>`_. PR `#1565 <https://github.com/vkbo/novelWriter/issues/1565>`_.
   * Fix an issue in the Document Viewer where it wouldn't scroll to a heading further down the page when following a reference pointing to it. Issue `#1566 <https://github.com/vkbo/novelWriter/issues/1566>`_. PR `#1568 <https://github.com/vkbo/novelWriter/issues/1568>`_.
   * Add back in checks for illegal drag and drop moves in the project tree. In 2.0, the logic here was changed to set certain restrictions on the elements of the project tree itself, but there are numerous bugs in the Qt framework related to drag and drop, so the checks are ignored on at least Qt 5.15.8. In particular, it is possible to drop items on the root level, and it's possible to move root items to other locations. Neither should be possible and will severely mess up the project if done. Issue `#1569 <https://github.com/vkbo/novelWriter/issues/1569>`_. PR `#1570 <https://github.com/vkbo/novelWriter/issues/1570>`_.
   * Add a custom autoscroll feature when dragging an item in the project tree to near the top or bottom. This is actually a default feature of the tree widget in the Qt library, but this too is broken in some versions of Qt 5.15.x. The default feature has been permanently disabled and replaced by a custom written feature that behaves similarly. Issue `#1561 <https://github.com/vkbo/novelWriter/issues/1561>`_. PR `#1571 <https://github.com/vkbo/novelWriter/issues/1571>`_.
   * Fix an issue where the editor document wasn't re-highlighted when the Syntax Theme for it was changed. Issue `#1535 <https://github.com/vkbo/novelWriter/issues/1535>`_. PR `#1573 <https://github.com/vkbo/novelWriter/issues/1573>`_.
   * Fix an issue where editing the Project Word List would not refresh the spell checking of the editor. Issue `#1559 <https://github.com/vkbo/novelWriter/issues/1559>`_. PR `#1573 <https://github.com/vkbo/novelWriter/issues/1573>`_.

   **Usability**

   * Changed how the default UI language is selected. It used to default to the system locale, but that is now changed to British English if the system local is not available in novelWriter. The only real effects of this is that the dropdown box in Preferences now selects British English if the system locale is not available rather than the first in the list (currently Deutch). The second effect is that the language on buttons and other Qt components will match the rest of the UI. Issue `#1564 <https://github.com/vkbo/novelWriter/issues/1564>`_. PR `#1565 <https://github.com/vkbo/novelWriter/issues/1565>`_.
   * There is a bug in Qt on Wayland desktops where menus don't open in the correct location. According to one Qt ticket, QTBUG-68636, this can be mitigated by ensuring all QMenu instances have a parent set. This does not fix all issues, but it should help. The menus without a parent set have now been updated. Issue `#1536 <https://github.com/vkbo/novelWriter/issues/1536>`_. PR `#1572 <https://github.com/vkbo/novelWriter/issues/1572>`_.

   **Documentation**

   * Fixed a number of spelling errors and typing mistakes in the documentation for 2.1. Contributed by @nisemono-neko. PR `#1567 <https://github.com/vkbo/novelWriter/issues/1567>`_.

Linux
-----

**AppImage**
   The AppImage should run on any recent Linux distro. See the `AppImage website`_ for more info.

   | **Download:** :octicon:`download` `novelWriter-2.1.1.AppImage <https://github.com/vkbo/novelWriter/releases/download/v2.1.1/novelWriter-2.1.1.AppImage>`__ [ 94.1 MB ]
   | **Checksum:** :octicon:`hash` ``6a572066fd1d11e115ffe78270be8df7ff8f2d9d005f8f01b3fb4c9ee56e1295`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.1.1/novelWriter-2.1.1.AppImage.sha256>`__

**AppImage (Legacy)**
   For older Linux distros you may need to download this AppImage instead.

   | **Download:** :octicon:`download` `novelWriter-2.1.1-oldlinux.AppImage <https://github.com/vkbo/novelWriter/releases/download/v2.1.1/novelWriter-2.1.1-oldlinux.AppImage>`__ [ 94.0 MB ]
   | **Checksum:** :octicon:`hash` ``487326cc9ad8de145259e5d9684449a99048b8efd602cd887b2f22e5cb13c9ad`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.1.1/novelWriter-2.1.1-oldlinux.AppImage.sha256>`__

**Debian Package**
   The package is built for Debian_, but should also work for Ubuntu_ and `Linux Mint`_.

   | **Download:** :octicon:`download` `novelwriter_2.1.1_all.deb <https://github.com/vkbo/novelWriter/releases/download/v2.1.1/novelwriter_2.1.1_all.deb>`__ [ 2.49 MB ]
   | **Checksum:** :octicon:`hash` ``39e328775b5505014527be9df8bdd1b040e160d9db4569cba99cb1d14741b942`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.1.1/novelwriter_2.1.1_all.deb.sha256>`__


Windows
-------

**Setup Installer**
   This is a standard setup installer for Windows. It is made for Windows 10 or newer.

   | **Download:** :octicon:`download` `novelwriter-2.1.1-amd64-setup.exe <https://github.com/vkbo/novelWriter/releases/download/v2.1.1/novelwriter-2.1.1-amd64-setup.exe>`__ [ 34.9 MB ]
   | **Checksum:** :octicon:`hash` ``a1474c478081bfcdf269cae73ebf92819e4d296b257e7122a783ba0a59048131`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.1.1/novelwriter-2.1.1-amd64-setup.exe.sha256>`__


MacOS
-----

**DMG Image**
   This is a DMG image for MacOS, and should work on MacOS 10 or higher.

   | **Download:** :octicon:`download` `novelWriter-2.1.1.dmg <https://github.com/vkbo/novelWriter/releases/download/v2.1.1/novelWriter-2.1.1.dmg>`__ [ 93.2 MB ]
   | **Checksum:** :octicon:`hash` ``064f64ba6d579b6680fa0e0b9bc5652bfa8cb57f50114144a8ea032596850282`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.1.1/novelWriter-2.1.1.dmg.sha256>`__


Other Packages
--------------

**Python Wheel**
   The Wheel package can be installed with ``pip install <file_path>``.

   | **Download:** :octicon:`download` `novelWriter-2.1.1-py3-none-any.whl <https://github.com/vkbo/novelWriter/releases/download/v2.1.1/novelWriter-2.1.1-py3-none-any.whl>`__ [ 2.87 MB ]
   | **Checksum:** :octicon:`hash` ``89e80f6467d41e8f09a762107ffd7d20e470ce4b1446f77b05e74b9126dcaf33`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.1.1/novelWriter-2.1.1-py3-none-any.whl.sha256>`__

**Source Code**
The source code packages are archived files of the entire source code. See also the `novelWriter Repository`_.

| **Download:** :octicon:`download` `novelWriter-2.1.1.zip <https://api.github.com/repos/vkbo/novelWriter/zipball/v2.1.1>`__
| **Download:** :octicon:`download` `novelWriter-2.1.1.tar.gz <https://api.github.com/repos/vkbo/novelWriter/tarball/v2.1.1>`__

