.. _AppImage website: https://appimage.org/
.. _Ubuntu: https://ubuntu.com/
.. _Debian: https://www.debian.org/
.. _Linux Mint: https://linuxmint.com/
.. _novelWriter Repository: https://github.com/vkbo/novelWriter/

| **Release Version:** Version 2.2 Beta 1
| **Release Date:** November 12, 2023
| **Release Page:** :octicon:`mark-github` `GitHub <https://github.com/vkbo/novelWriter/releases/tag/v2.2b1>`__

.. dropdown:: Release Notes
   :animate: fade-in-slide-down
   :icon: info

   This is a beta release of the next release version, and is intended for testing purposes. Please be careful when using this version on live writing projects, and make sure you take frequent backups.

   Please check the changelog for an overview of changes. The full release notes will be added to the final release.

.. dropdown:: Detailed Changelog
   :animate: fade-in-slide-down
   :icon: tasklist

   **Features**

   * novelWriter has a new logo and icon. PR `#1593 <https://github.com/vkbo/novelWriter/issues/1593>`_.
   * The Document Editor is now a true plain text editor. This has a number of benefits and a couple of drawbacks. The most important benefits is that the editor responds a lot faster, and can hold much larger text documents. The big document limit has therefore been removed. It mostly affected automatic spell checking. The syntax highlighter and spell checker are also more efficient, which allows for needed improvements to these. The drawbacks are mainly that the editor now scrolls one line at a time, instead of scrolling pixel by pixel like before. PRs `#1521 <https://github.com/vkbo/novelWriter/issues/1521>`_ and `#1525 <https://github.com/vkbo/novelWriter/issues/1525>`_.
   * Tags and References are now case insensitive. Their display name on the user interface remains the same as the value set for the ``@tag`` entry. Issue `#1313 <https://github.com/vkbo/novelWriter/issues/1313>`_. PRs `#1522 <https://github.com/vkbo/novelWriter/issues/1522>`_ and `#1578 <https://github.com/vkbo/novelWriter/issues/1578>`_.
   * Keywords for Tags and References, and the References themselves, now have an auto-complete menu that pops up in the editor on lines starting with the ``@`` character. It will first suggest what keyword you want to use, and when it has been added, use that keyword to look up suggestions for references to add. The suggestions improve as you type by looking for the characters you've already typed in the tags you've previously defined. Issue `#823 <https://github.com/vkbo/novelWriter/issues/823>`_. PR `#1581 <https://github.com/vkbo/novelWriter/issues/1581>`_.
   * You can now right-click an undefined tag, and a context menu option to create a Project Note for that tag will appear in the menu. On selection, it will create a note in the first root folder of the correct kind, and set the title and tag to match the undefined reference, making it instantly defined. Issues `#1580 <https://github.com/vkbo/novelWriter/issues/1580>`_ and `#823 <https://github.com/vkbo/novelWriter/issues/823>`_. PR `#1582 <https://github.com/vkbo/novelWriter/issues/1582>`_.
   * Shortcodes have been added to the Document Editor. Shorcodes are HTML-like syntax, but uses square brackets instead of angular brackets. So ``[b]text[/b]`` will make the word "text" appear as bold. Shortcodes currently support bold, italic, striketrough, underline, superscript and subscript text. The first three are complimentary to the Markdown-like syntax that. The benefit of the shortcode emphasis syntax, however, is that it does not care about word boundaries, and can therefore be used any place in the text. Including in the middle of words. Issues `#1337 <https://github.com/vkbo/novelWriter/issues/1337>`_ and `#1444 <https://github.com/vkbo/novelWriter/issues/1444>`_. PRs `#1540 <https://github.com/vkbo/novelWriter/issues/1540>`_ and `#1583 <https://github.com/vkbo/novelWriter/issues/1583>`_.
   * A show/hide toolbar has been added to the editor where toolbuttons for formatting options are available. The toolbar is hidden by default, but can be activated from a three dots icon in the top left corner of the editor. Issue `#1585 <https://github.com/vkbo/novelWriter/issues/1585>`_. PR `#1584 <https://github.com/vkbo/novelWriter/issues/1584>`_.
   * Build Definitions in the Manuscript Build tool can now be re-ordered, and the order is preserved when the tool is closed and re-opened. Issue `#1542 <https://github.com/vkbo/novelWriter/issues/1542>`_. PR `#1591 <https://github.com/vkbo/novelWriter/issues/1591>`_.

   **Usability**

   * The Settings menu in the sidebar now always pops out to the right and upwards from the bottom of the icon. The previous behaviour was not guaranteed to stay in the visible area of the screen. PR `#1520 <https://github.com/vkbo/novelWriter/issues/1520>`_.
   * The right click action on a misspelled word now uses the actual spell checker data for lookup. Previously, the spell checker would underline a word that was misspelled, but the right click action actually had no way of reading where the error line was, so it had to guess again what word the user was clicking. Since these two parts of the code used different logic, they sometimes produced different results. The spell checker now saves the location of each spell check error, and the right click action retrieves this data when generating suggestions, which should eliminate the problem of picking the correct word boundaries. Issue `#1532 <https://github.com/vkbo/novelWriter/issues/1532>`_. PR `#1525 <https://github.com/vkbo/novelWriter/issues/1525>`_.
   * The language of a project is not set in the New Project Wizard and in Project Settings. It is no longer defined in the Build Settings panel. Issue `#1588 <https://github.com/vkbo/novelWriter/issues/1588>`_. PR `#1589 <https://github.com/vkbo/novelWriter/issues/1589>`_.
   * The way switching focus and view in the main GUI has changed. Pressing ``Ctrl+T`` will now switch focus to the Project or Novel Tree if focus is elsewhere, or if either have focus already, it will switch view to the other tree. Pressing ``Ctrl+E`` will switch focus and view to the Document Editor. Pressing ``Ctrl+Shift+T`` will do the same for the Outline View. The old Alt-based shortcuts have been removed. Issues `#1310 <https://github.com/vkbo/novelWriter/issues/1310>`_ and `#1291 <https://github.com/vkbo/novelWriter/issues/1291>`_. PR `#1590 <https://github.com/vkbo/novelWriter/issues/1590>`_.

   **User Interface**

   * The labels under the sidebar buttons have been removed. The tool tips have the necessary information. PR `#1520 <https://github.com/vkbo/novelWriter/issues/1520>`_.

   **Other Improvements**

   * Also the Tags and References keywords are now translated into the project language when these are included in Manuscript builds. As long as the phrases have been translated. PR `#1586 <https://github.com/vkbo/novelWriter/issues/1586>`_.

Linux
-----

**AppImage**
   The AppImage should run on any recent Linux distro. See the `AppImage website`_ for more info.

   | **Download:** :octicon:`download` `novelWriter-2.2b1.AppImage <https://github.com/vkbo/novelWriter/releases/download/v2.2b1/novelWriter-2.2b1.AppImage>`__ [ 94.1 MB ]
   | **Checksum:** :octicon:`hash` ``94c96e848aec1ab2c071591f3a0a57bf3205534b11efacb43ab9b923ef154238`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.2b1/novelWriter-2.2b1.AppImage.sha256>`__

**AppImage (Legacy)**
   For older Linux distros you may need to download this AppImage instead.

   | **Download:** :octicon:`download` `novelWriter-2.2b1-oldlinux.AppImage <https://github.com/vkbo/novelWriter/releases/download/v2.2b1/novelWriter-2.2b1-oldlinux.AppImage>`__ [ 94.0 MB ]
   | **Checksum:** :octicon:`hash` ``ef0801e2297e1c9c7549ed1741cca35c123c84cc80beea7753a5a95bcf856909`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.2b1/novelWriter-2.2b1-oldlinux.AppImage.sha256>`__

**Debian Package**
   The package is built for Debian_, but should also work for Ubuntu_ and `Linux Mint`_.

   | **Download:** :octicon:`download` `novelwriter_2.2b1_all.deb <https://github.com/vkbo/novelWriter/releases/download/v2.2b1/novelwriter_2.2b1_all.deb>`__ [ 2.48 MB ]
   | **Checksum:** :octicon:`hash` ``6dc81d9f7dd584d238fb28bce0e8cc663dfa044c648faca3c201e7129fb49210`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.2b1/novelwriter_2.2b1_all.deb.sha256>`__


Windows
-------

**Setup Installer**
   This is a standard setup installer for Windows. It is made for Windows 10 or newer.

   | **Download:** :octicon:`download` `novelwriter-2.2b1-amd64-setup.exe <https://github.com/vkbo/novelWriter/releases/download/v2.2b1/novelwriter-2.2b1-amd64-setup.exe>`__ [ 34.9 MB ]
   | **Checksum:** :octicon:`hash` ``63526f65db243338d8393e8b5a4a5922f2c13c8d9b58cfd61d239438607772fd`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.2b1/novelwriter-2.2b1-amd64-setup.exe.sha256>`__


MacOS
-----

**DMG Image**
   This is a DMG image for MacOS, and should work on MacOS 10 or higher.

   | **Download:** :octicon:`download` `novelWriter-2.2b1.dmg <https://github.com/vkbo/novelWriter/releases/download/v2.2b1/novelWriter-2.2b1.dmg>`__ [ 93.1 MB ]
   | **Checksum:** :octicon:`hash` ``ff3ac71bff951497f4199a287ffd449bed85117aee0995578cc3a4387ce0d308`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.2b1/novelWriter-2.2b1.dmg.sha256>`__


Other Packages
--------------

**Python Wheel**
   The Wheel package can be installed with ``pip install <file_path>``.

   | **Download:** :octicon:`download` `novelWriter-2.2b1-py3-none-any.whl <https://github.com/vkbo/novelWriter/releases/download/v2.2b1/novelWriter-2.2b1-py3-none-any.whl>`__ [ 2.87 MB ]
   | **Checksum:** :octicon:`hash` ``91bada303263a95dedc59edfa2bf2e306cc36dda9b80540a2fe38d3e8ce58fea`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.2b1/novelWriter-2.2b1-py3-none-any.whl.sha256>`__

**Source Code**
The source code packages are archived files of the entire source code. See also the `novelWriter Repository`_.

| **Download:** :octicon:`download` `novelWriter-2.2b1.zip <https://api.github.com/repos/vkbo/novelWriter/zipball/v2.2b1>`__
| **Download:** :octicon:`download` `novelWriter-2.2b1.tar.gz <https://api.github.com/repos/vkbo/novelWriter/tarball/v2.2b1>`__

