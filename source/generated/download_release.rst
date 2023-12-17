.. _AppImage website: https://appimage.org/
.. _Ubuntu: https://ubuntu.com/
.. _Debian: https://www.debian.org/
.. _Linux Mint: https://linuxmint.com/
.. _novelWriter Repository: https://github.com/vkbo/novelWriter/

| **Release Version:** Version 2.2
| **Release Date:** December 17, 2023
| **Release Page:** :octicon:`mark-github` `GitHub <https://github.com/vkbo/novelWriter/releases/tag/v2.2>`__

.. dropdown:: Release Notes
   :animate: fade-in-slide-down
   :icon: info

   This release comes with a number of new features. These are some highlights.

   In addition to the common Markdown style formatting for bold, italic and strike through, a set of new shortcodes have been added. The shortcodes are far more flexible than the Markdown style syntax, and can be used for more complex formatting cases. Like when you need to add multiple, overlapping formats, or add emphasis to just a part of a word. The shortcodes also allow for underline, subscript and superscript, which the Markdown syntax does not. The new formats are available in the "Format" menu, and in a new toolbar in the editor that can be enabled by clicking the three dots in the top--left corner. The shortcode format was chosen because it can later be extended to include other requested features as well. Please have a look at the documentation for more details about the new shortcodes.

   The Tags and References system has been improved. The tags themselves are no longer case sensitive when you use them in references, but they are still displayed as you typed them in the tag definition when they are displayed in the user interface. Starting to type the ``@`` symbol in the text editor, on a new line, will now open an auto-completer menu which will display available options. It may not display all of your tags if you have a lot of them, but starting to type more characters will filter the list down further.

   You can now automatically create a note file for a new tag that you have added to a reference list in a document, but is not yet defined in a project note. So, for instance, if you come up with a new character while writing, and add a new tag to your ``@char`` references, you can right-click the new tag and create a new note for that entry directly. In addition, it is now also possible to right-click a heading in an open document and set the item label in the project tree to match the heading.

   In addition to the changes in the editor, the "References" panel below the document viewer has also been completely redesigned. It now shows all the references to the document you are viewing as a list, with a lot more details than before. In addition, tabs in the panel will appear to show all the tags you have defined in your notes, sorted as one tab per category. Like for instance Characters, Locations, Objects, etc. You can also give each note a short description comment on the same format as the summary comments for chapters and scenes. The short description  comment can be added from the "Insert" menu under "Special Comments".

   The last major change in this release is the new multi-select feature in the project tree. You can now select multiple documents and folders using the mouse while pressing ``Ctrl`` or ``Shift``. By right-clicking the selected items, you can perform a limited set of operations on all of them, like changing active status, and the status or importance labels. You can also drag and drop multiple items under the condition that all the selected items are in the same folder, at the same level. This restriction is in place due to limitations in the framework novelWriter is based on. But this should help in cases where multiple documents need to be moved in and out of folders or between folders. Note that adding the multi-select feature meant that the undo feature of the project tree had to be removed. It may be added back later.

   *These Release Notes also include the changes from the 2.2 Beta 1 and 2.2 RC 1 releases.*

.. dropdown:: Detailed Changelog
   :animate: fade-in-slide-down
   :icon: tasklist

   **Bugfixes**

   * Fix column widths for columns with no text in the viewer panel lists, and fix an issues where icons were not updated on theme switch. Issue `#1627 <https://github.com/vkbo/novelWriter/issues/1627>`_. PR `#1626 <https://github.com/vkbo/novelWriter/issues/1626>`_.
   * Fix auto-selection of words with apostrophes. Issue `#1624 <https://github.com/vkbo/novelWriter/issues/1624>`_. PR `#1632 <https://github.com/vkbo/novelWriter/issues/1632>`_.

   **Usability**

   * Use ``Ctrl+K, H`` for inserting short description comments (alias to synopsis), drop the space after the ``%`` symbol when inserting special comments, add a browse icon to the open open project dialog, and remove the popup warning for Alpha releases. PR `#1626 <https://github.com/vkbo/novelWriter/issues/1626>`_.
   * Menu entries no longer clear the status bar message when they are hovered. This was caused by a status tip feature in Qt, which prints a blank message to the status bar. PR `#1630 <https://github.com/vkbo/novelWriter/issues/1630>`_.
   * The novel view panel now scrolls to bring the current document into view when iteratively searching through documents in the project. Issue `#1555 <https://github.com/vkbo/novelWriter/issues/1555>`_. PR `#1632 <https://github.com/vkbo/novelWriter/issues/1632>`_.
   * The progress bar on the Manuscript Build dialog now stays for 3 seconds after completion instead of 1 second. PR `#1634 <https://github.com/vkbo/novelWriter/issues/1634>`_.
   * The document viewer panel now shows the importance label next to each entry, and double-clicking an entry will open it in the viewer. All entries also now show the content in tooltips so that the columns can be shrunk to only view the icon if there is too little space. Issue `#16220 <https://github.com/vkbo/novelWriter/issues/16220>`_. PR `#1639 <https://github.com/vkbo/novelWriter/issues/1639>`_.
   * The editor toolbar no longer uses the same buttons for markdown and shortcodes style formatting. They have each received their separate buttons. Some additional space has been added between the two types of buttons to visually separate them. Issues `#1636 <https://github.com/vkbo/novelWriter/issues/1636>`_ and `#1637 <https://github.com/vkbo/novelWriter/issues/1637>`_. PR `#1638 <https://github.com/vkbo/novelWriter/issues/1638>`_.
   * Convert the Synopsis and Comment buttons in the document viewer footer to buttons with both icon and text, and drop the label. Issue `#1628 <https://github.com/vkbo/novelWriter/issues/1628>`_. PR `#1638 <https://github.com/vkbo/novelWriter/issues/1638>`_.

   **Internationalisation**

   * Updated US English, Norwegian, Japanese, Latin American Spanish, French, and Italian translations. PRs `#1625 <https://github.com/vkbo/novelWriter/issues/1625>`_ and `#1641 <https://github.com/vkbo/novelWriter/issues/1641>`_.

   **Documentation**

   * The documentation has been updated to cover new features in 2.2. PR `#1640 <https://github.com/vkbo/novelWriter/issues/1640>`_.

   **Code Improvements**

   * Improve memory usage by making sure C++ objects are deleted when they are no longer used. There is an issue between the Python and Qt side of things where objects are left in memory and not properly garbage collected when they run out of scope. A number of deferred delete calls have been added that seems to solve most of these cases. A ``--meminfo`` flag has been added to the command line arguments to provide diagnostic data to help debug such issues. PR `#1629 <https://github.com/vkbo/novelWriter/issues/1629>`_.
   * Improve handling of alert boxes and their memory clean up, and refactor event filters. PR `#1631 <https://github.com/vkbo/novelWriter/issues/1631>`_.
   * Clean up unused methods in GUI extensions. PR `#1634 <https://github.com/vkbo/novelWriter/issues/1634>`_.

Linux
-----

**AppImage**
   The AppImage should run on any recent Linux distro. See the `AppImage website`_ for more info.

   | **Download:** :octicon:`download` `novelWriter-2.2.AppImage <https://github.com/vkbo/novelWriter/releases/download/v2.2/novelWriter-2.2.AppImage>`__ [ 95.3 MB ]
   | **Checksum:** :octicon:`hash` ``c6b3549a9ce3271cd4d893b00c6fd7c4064a27e9ae0d5b4d8d379c091957a871`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.2/novelWriter-2.2.AppImage.sha256>`__

**AppImage (Legacy)**
   For older Linux distros you may need to download this AppImage instead.

   | **Download:** :octicon:`download` `novelWriter-2.2-oldlinux.AppImage <https://github.com/vkbo/novelWriter/releases/download/v2.2/novelWriter-2.2-oldlinux.AppImage>`__ [ 94.4 MB ]
   | **Checksum:** :octicon:`hash` ``4645c3ffafe81129364a29f1fe52e25db98478fbdbcf7a45d501e41507139d3c`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.2/novelWriter-2.2-oldlinux.AppImage.sha256>`__

**Debian Package**
   The package is built for Debian_, but should also work for Ubuntu_ and `Linux Mint`_.

   | **Download:** :octicon:`download` `novelwriter_2.2_all.deb <https://github.com/vkbo/novelWriter/releases/download/v2.2/novelwriter_2.2_all.deb>`__ [ 2.85 MB ]
   | **Checksum:** :octicon:`hash` ``d19b9f63b9c44685d7814db8905a58309acb51ec48874f174c9abeeb40f2b205`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.2/novelwriter_2.2_all.deb.sha256>`__


Windows
-------

**Setup Installer**
   This is a standard setup installer for Windows. It is made for Windows 10 or newer.

   | **Download:** :octicon:`download` `novelwriter-2.2-amd64-setup.exe <https://github.com/vkbo/novelWriter/releases/download/v2.2/novelwriter-2.2-amd64-setup.exe>`__ [ 35.8 MB ]
   | **Checksum:** :octicon:`hash` ``9c2abefc726b18754307e574f42460022cbc413d3e264ed56a7dacf3d6e57aff`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.2/novelwriter-2.2-amd64-setup.exe.sha256>`__


MacOS
-----

**DMG Image**
   This is a DMG image for MacOS, and should work on MacOS 10 or higher.

   | **Download:** :octicon:`download` `novelWriter-2.2.dmg <https://github.com/vkbo/novelWriter/releases/download/v2.2/novelWriter-2.2.dmg>`__ [ 94.2 MB ]
   | **Checksum:** :octicon:`hash` ``b82894ad03062d7eecf0e2611986e3d92b43a9602b5f9b52fcf584472b607df2`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.2/novelWriter-2.2.dmg.sha256>`__


Other Packages
--------------

**Python Wheel**
   The Wheel package can be installed with ``pip install <file_path>``.

   | **Download:** :octicon:`download` `novelWriter-2.2-py3-none-any.whl <https://github.com/vkbo/novelWriter/releases/download/v2.2/novelWriter-2.2-py3-none-any.whl>`__ [ 3.27 MB ]
   | **Checksum:** :octicon:`hash` ``12e01abfa592c2f6f9af070d6802ddfc2ef553f85ab6d5a2075156c61544a4b4`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.2/novelWriter-2.2-py3-none-any.whl.sha256>`__

**Source Code**
The source code packages are archived files of the entire source code. See also the `novelWriter Repository`_.

| **Download:** :octicon:`download` `novelWriter-2.2.zip <https://api.github.com/repos/vkbo/novelWriter/zipball/v2.2>`__
| **Download:** :octicon:`download` `novelWriter-2.2.tar.gz <https://api.github.com/repos/vkbo/novelWriter/tarball/v2.2>`__

