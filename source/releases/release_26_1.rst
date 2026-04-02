.. _main_release_26_1:

*************************
Pre-Release 2026.1 Beta 1
*************************

| **Release Date:** Not yet releases


Release Notes
=============

.. attention::

   This is a beta release of the next release version, and is intended for testing purposes. Please be careful when
   using this version on live writing projects, and make sure you take frequent backups.

   You can follow the development progress on the `26.1 RC 1 Milestone <https://github.com/vkbo/novelWriter/milestone/110>`__.

From this release, novelWriter switches to using the year as the main release version number, starting with 2026.1.


User Interface
--------------

The first release of 2026 adds the Lucide icon theme, which you can select from Preferences. Two new light colour themes
designed specifically for colour blindness have also been added. A new setting in Preferences will add dotted lines
under formatting codes to further distinguish them from the text in order to make them more visible for people who see
fewer colour variations. The various settings pages and dialogs should also respond better to screen readers now,
although there are many further improvements to be made.


Manuscript Features
-------------------

There are several new features and settings for the **Manuscript Build** tool available in the **Manuscript Build**
settings dialog:

* The font size of headings can be adjusted, and a new setting to make them upper case was added.
* It is now possible to use blank lines between paragraphs for office type document manuscripts instead of paragraph
  text margins. This makes more sense for manuscript formatted with fixed width fonts in a typewriter style.
* Some of the settings have been moved and reorganised into different sections.


Text Editor Features
--------------------

Several improvements have been made to the text editor based on user requests.

* The in-editor search feature will now move to the previous document also when searching backwards, if the setting to
  continue searching in the next document is enabled.
* A new option in the right click menu will let you split an open document either at the cursor position, or move a
  section of selected text to a new document. This should make it much easier to split a single document in two.
* If you use a fixed width font in the editor, you may not want headings to have a larger font size than the text. You
  can now turn off the scaling of headings in Preferences.
* Each part of the document bread crumbs path in the editor and viewer header is now clickable, and will highlight the
  relevant document or folder in the project tree.
* The keyboard shortcuts :kbd:`Ctrl+Up` and :kbd:`Ctrl+Down` will now, respectively, move the cursor to the previous or
  next paragraph in your document.


Other Changes
-------------

Minor improvements have been made to navigation by keyboard in the Welcome dialog, and in the project search panel.
Visual improvements with more tooltips labels and icons have been made in various places in the user interface.


Download Links
==============

.. include:: ../generated/download_pre_release.rst
