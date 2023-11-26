.. _AppImage website: https://appimage.org/
.. _Ubuntu: https://ubuntu.com/
.. _Debian: https://www.debian.org/
.. _Linux Mint: https://linuxmint.com/
.. _novelWriter Repository: https://github.com/vkbo/novelWriter/

| **Release Version:** Version 2.2 RC 1
| **Release Date:** November 26, 2023
| **Release Page:** :octicon:`mark-github` `GitHub <https://github.com/vkbo/novelWriter/releases/tag/v2.2rc1>`__

.. dropdown:: Release Notes
   :animate: fade-in-slide-down
   :icon: info

   This is a release candidate of the next release version, and is intended for testing purposes. Please be careful when using this version on live writing projects, and make sure you take frequent backups.

   Please check the changelog for an overview of changes. The full release notes will be added to the final release.

.. dropdown:: Detailed Changelog
   :animate: fade-in-slide-down
   :icon: tasklist

   **Bugfixes**

   * Revert the change of keyboard shortcut to delete a project tree item made in 2.2 Beta 1 as it blocks certain features in the editor. This is a regression. PR 1616.

   **Features**

   * The old References panel under the Document Viewer has been replaced with a completely new widget with a lot more features. The Back-references panel is still there, but is now a scrollable list with a lot more information. In addition, tabs for each category of tags are available when there are tags defined for them. These panels list all available tags, with a good deal of information about them that may be useful to the writer, as well as buttons to open them in the viewer or editor. Issues `#925 <https://github.com/vkbo/novelWriter/issues/925>`_ and `#998 <https://github.com/vkbo/novelWriter/issues/998>`_. PR `#1606 <https://github.com/vkbo/novelWriter/issues/1606>`_.
   * Multi-select is now possible in the project tree, with some limitations. Drag and drop is only permitted if the selected items have the same parent item. Any other drag and drop selection will be cancelled and the user notified. A new context menu has been added for the case when multiple items are selected, with a reduced set of options that can be collectively applied to them. Issues `#1549 <https://github.com/vkbo/novelWriter/issues/1549>`_ and `#1592 <https://github.com/vkbo/novelWriter/issues/1592>`_. PR `#1612 <https://github.com/vkbo/novelWriter/issues/1612>`_.
   * The "Scroll Past End" setting in Preferences has been added back in. It is slightly different than the old one, as this one uses the Qt Plain Text Editor implementation, which has some side effects some users may want to avoid. Issue `#1602 <https://github.com/vkbo/novelWriter/issues/1602>`_. PR `#1605 <https://github.com/vkbo/novelWriter/issues/1605>`_.
   * For Windows users, there is now an "Add Dictionaries" tool in the Tools menu where new spell check dictionaries can be added. Links are provided to sources for these dictionaries, and a file selector tool to import the files into novelWriter. Issue `#982 <https://github.com/vkbo/novelWriter/issues/982>`_. PR `#1611 <https://github.com/vkbo/novelWriter/issues/1611>`_.
   * You can now update the name of a document by right-clicking on any heading inside the document and select "Set as Document Name". This will open the Rename dialog with the text of the heading pre-filled. Issue `#1503 <https://github.com/vkbo/novelWriter/issues/1503>`_. PR `#1614 <https://github.com/vkbo/novelWriter/issues/1614>`_.
   * A new special comment, called "Short" can be added to Project Notes. They are identical to Synopsis comments, and are in fact just an alias for them. The "Short Description" will be displayed alongside the tags in the new panel under the Document Viewer. Issues `#1617 <https://github.com/vkbo/novelWriter/issues/1617>`_ and `#1621 <https://github.com/vkbo/novelWriter/issues/1621>`_. PRs `#1617 <https://github.com/vkbo/novelWriter/issues/1617>`_, `#1619 <https://github.com/vkbo/novelWriter/issues/1619>`_ and `#1622 <https://github.com/vkbo/novelWriter/issues/1622>`_.

   **Usability**

   * The feature to auto select word under cursor no longer uses the default Qt implementation, and has instead been implemented by iterating backward and forward in the text to find the nearest word boundaries. It will stop on characters that aren't Unicode alphanumeric as per Python's definition. Toggling markup will also move the cursor to after the markup if it was already at the end of the word. Otherwise it remains within the word at the same position. The word is not selected after formatting if it wasn't selected before. If no selection was made, and no word is auto selected, the formatting tags are inserted in-place with the cursor in the middle. Issues `#1333 <https://github.com/vkbo/novelWriter/issues/1333>`_ and `#1598 <https://github.com/vkbo/novelWriter/issues/1598>`_. PR `#1600 <https://github.com/vkbo/novelWriter/issues/1600>`_.
   * The auto complete context menu is now only triggered on actual user input consisting of adding or removing a single character. PR `#1601 <https://github.com/vkbo/novelWriter/issues/1601>`_.
   * Various improvements to the visibility of the cursor when the dimensions of the editor changes have been added. Like for instance keeping the cursor visible when opening or closing the Viewer panel, or toggling Focus Mode. Issues `#1302 <https://github.com/vkbo/novelWriter/issues/1302>`_ and `#1478 <https://github.com/vkbo/novelWriter/issues/1478>`_. PR `#1608 <https://github.com/vkbo/novelWriter/issues/1608>`_.
   * The Manuscript Build dialog now has a button to open the output folder. Issue `#1554 <https://github.com/vkbo/novelWriter/issues/1554>`_. PR `#1613 <https://github.com/vkbo/novelWriter/issues/1613>`_.

   **Code Improvements**

   * Improve test coverage. PR `#1607 <https://github.com/vkbo/novelWriter/issues/1607>`_.

Linux
-----

**AppImage**
   The AppImage should run on any recent Linux distro. See the `AppImage website`_ for more info.

   | **Download:** :octicon:`download` `novelWriter-2.2rc1.AppImage <https://github.com/vkbo/novelWriter/releases/download/v2.2rc1/novelWriter-2.2rc1.AppImage>`__ [ 94.2 MB ]
   | **Checksum:** :octicon:`hash` ``05e52b5b80b85083f49266f5f907bf3ec4d3f46f080128c2ed5abca73ef2c4d8`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.2rc1/novelWriter-2.2rc1.AppImage.sha256>`__

**AppImage (Legacy)**
   For older Linux distros you may need to download this AppImage instead.

   | **Download:** :octicon:`download` `novelWriter-2.2rc1-oldlinux.AppImage <https://github.com/vkbo/novelWriter/releases/download/v2.2rc1/novelWriter-2.2rc1-oldlinux.AppImage>`__ [ 94.1 MB ]
   | **Checksum:** :octicon:`hash` ``b111f7ac1d6f74a1ad9c824ab8a99b91177db67508bbff8fab1fdf8633e4b934`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.2rc1/novelWriter-2.2rc1-oldlinux.AppImage.sha256>`__

**Debian Package**
   The package is built for Debian_, but should also work for Ubuntu_ and `Linux Mint`_.

   | **Download:** :octicon:`download` `novelwriter_2.2rc1_all.deb <https://github.com/vkbo/novelWriter/releases/download/v2.2rc1/novelwriter_2.2rc1_all.deb>`__ [ 2.52 MB ]
   | **Checksum:** :octicon:`hash` ``2e83b06c90cc95a2c7381dbbe165164ce23211a7e2436b59a2cea2cfe07619e6`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.2rc1/novelwriter_2.2rc1_all.deb.sha256>`__


Windows
-------

**Setup Installer**
   This is a standard setup installer for Windows. It is made for Windows 10 or newer.

   | **Download:** :octicon:`download` `novelwriter-2.2rc1-amd64-setup.exe <https://github.com/vkbo/novelWriter/releases/download/v2.2rc1/novelwriter-2.2rc1-amd64-setup.exe>`__ [ 35.1 MB ]
   | **Checksum:** :octicon:`hash` ``1b6b0caafdd15e07d0f5ba5fcc8a4451d98ec7bcc7ba80113792a76ae3eaa19d`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.2rc1/novelwriter-2.2rc1-amd64-setup.exe.sha256>`__


MacOS
-----

**DMG Image**
   This is a DMG image for MacOS, and should work on MacOS 10 or higher.

   | **Download:** :octicon:`download` `novelWriter-2.2rc1.dmg <https://github.com/vkbo/novelWriter/releases/download/v2.2rc1/novelWriter-2.2rc1.dmg>`__ [ 93.5 MB ]
   | **Checksum:** :octicon:`hash` ``1bf6b2fd616d3edd03021b394ce6c417a3056e06b0e1a63b32f0b68e353efeaf`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.2rc1/novelWriter-2.2rc1.dmg.sha256>`__


Other Packages
--------------

**Python Wheel**
   The Wheel package can be installed with ``pip install <file_path>``.

   | **Download:** :octicon:`download` `novelWriter-2.2rc1-py3-none-any.whl <https://github.com/vkbo/novelWriter/releases/download/v2.2rc1/novelWriter-2.2rc1-py3-none-any.whl>`__ [ 2.93 MB ]
   | **Checksum:** :octicon:`hash` ``69d6a28a314f16f903cc8e38ef82f091b3a772762d4992b822a4be5691e627f2`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.2rc1/novelWriter-2.2rc1-py3-none-any.whl.sha256>`__

**Source Code**
The source code packages are archived files of the entire source code. See also the `novelWriter Repository`_.

| **Download:** :octicon:`download` `novelWriter-2.2rc1.zip <https://api.github.com/repos/vkbo/novelWriter/zipball/v2.2rc1>`__
| **Download:** :octicon:`download` `novelWriter-2.2rc1.tar.gz <https://api.github.com/repos/vkbo/novelWriter/tarball/v2.2rc1>`__

