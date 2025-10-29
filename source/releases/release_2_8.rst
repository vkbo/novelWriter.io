.. _main_release_2_8:

**********************
Pre-Release 2.8 Beta 1
**********************

| **Release Date:** October 29, 2025


Release Notes
=============

.. attention::

   This is a beta release of the next release version, and is intended for testing purposes. Please be careful when
   using this version on live writing projects, and make sure you take frequent backups.

   You can follow the development progress on the `2.8 RC 1 Milestone <https://github.com/vkbo/novelWriter/milestone/104>`__.


Theme Revamp
------------

The major change in 2.8 is that the colour theme is now uniform for the entire application. You no longer need to select
a separate theme for the app and the documents separately. Instead you can now select your preferred light and dark
theme, and switch between them using a new button on the side bar. You can also set the theme to automatically follow
the light or dark mode choice of your operating system.

In addition to a redesign of the colour theme system, a large number of new colour themes have been added. There are
many new choices for both light and dark themes, and a lot of them come in matching pairs.


Icon and Button Consistency
---------------------------

All buttons now use icons from the selected icon theme, and no longer inherits any icons from your operating system.
This helps keep the icons consistent.

You can also select standard theme colours for your **Status** and **Importance** labels. The **Project Settings** tabs
for these have been redesigned with these additional options. This means that when you switch between light and dark
theme, or to a different colour theme, the **Status** and **Importance** label icons will update too.

.. note::

   Since the **Status** and **Importance** labels have had fixed values in the past, once your project has been opened
   in novelWriter 2.8, you have to go and change the colour for each label icon from "Custom" to your standard theme
   colour of choice. You still have the option to set a fixed colour for these icons if you wish to.


New Features
------------

**Markdown Highlighting**
   You can now use Markdown highlighting tags in the text, like this:

   .. code-block:: md

      Some text with ==this part highlighted==.

   This does the same as the shortcode ``[m][/m]`` tags, but the difference is that the text is visually highlighted
   also in the editor.

**Current Line Highlighted**
   A new setting is available in **Preferences** under **Text Editing** which enables highlighting of the current line.
   That is, the line where the cursor is will have a different background colour.

**Repeatable Annotated Comments**
   Specially annotated comments, like Synopsis, Short Description, Story Structure, and Story Notes, can now be repeated
   under a heading and all comments preserved in the outline and its export.


Other Changes
-------------

* You can now switch to the Project Tree or Outline View using keyboard shortcuts while in Focus Mode.
* When creating a new document from a template, the main title of the template document is replaced with the label
  chosen for the new document.
* The auto-replace feature in the editor is now better at detecting opening and closing quotes when used in relation to
  Markdown style markup.
* The application window is now blocked from resizing itself to a size larger than the screen when opened on a smaller
  screen than it was previously opened on.
* Trailing spaces are no longer highlighted in the editor with an error underline.
* A switch on the **Manuscript Build Settings** dialog now allows for automatic preview of the build when the Apply or
  Save button is clicked.
* The editor now properly supports 4 byte Unicode characters without breaking the syntax highlighting and spell checker.


Download Links
==============

.. include:: ../generated/download_pre_release.rst
