.. _main_release_2_6:

**********************
Pre-Release 2.6 Beta 1
**********************

| **Release Date:** November 12, 2024

.. _Issues: https://github.com/vkbo/novelWriter/issues

Release Notes
=============

.. attention::

   This is a pre-release of the next release version, and is intended for testing only. Please be careful when using this version
   on live writing projects, and make sure you take frequent backups.

   You can follow the development progress on the `2.6 RC 1 Milestone <https://github.com/vkbo/novelWriter/milestone/90>`__.


New Manuscript Features
-----------------------

This release has largely focused on the Manuscript Build tool, and a number of new features have been added. The code behind all the
output formats has also been extensively restructured to ensure better consistency between the preview and the various outputs.

The Build Settings dialog has also been redesigned to match other, similar dialogs. All customisation settings, aside from the two
first pages, have been moved into a long, scrollable form with quick-navigations links on the left.

The new features are:

* You can now generate a PDF of your manuscript.
* You can also generate a Microsoft Word (DocX) document. It should have all the same features as the Open Document format (ODT).
  The new DocX format has been validated against the document standard and tested in the online Office 365 version. The format is
  still new, and may have issues, so if you have any problems, please report them on the project's Issues_ page.
* You can now also control the page break and title centring of the main novel title. This is particularly useful if you want to add
  text above the title on the cover page, and want to turn off the automatic page break.
* You can now customise the styling of headings, and even turn them off completely if your manuscript standard calls for headings to
  be styled the same way as plain text. You can also adjust top and bottom margins of heading types and text paragraphs.
* Word count statistics, and other related statics values, can be inserted into the manuscript. The value fields must be added to
  the document itself in the editor, using the new **Insert > Word/Character Count** menu entry. In the document viewer, they are
  shown as 0, but they are set to the correct value in the Manuscript preview.
* If you have enabled the option to ignore line breaks in text paragraphs in your Build Settings, you can still force line breaks in
  the text where you still want them by adding ``[br]`` shortcodes. You can still add a line break after these, for a better visual
  look in the editor. this will not produce double line breaks.
* You now have the option to show page breaks in the Manuscript preview panel. They are enabled by default, but can be disabled with
  a little switch below the preview window.


Tags and References
-------------------

It has always been possible to add a ``@tag`` to your novel documents. However, there was no dedicated keyword to reference these
tags if you needed to cross-reference between novel documents or from notes. You can now do that with the ``@story`` keyword. It
works exactly the same as all other reference keywords.

In addition, a new special ``@mention`` keyword has been added. It is intended for referencing story elements that are not present
in a given chapter or scene, but is discussed. So if your Point-of-View character takes about someone who isn't present in the
scene, you may still want to indicate that they're mentioned so you can go back later and check for story consistency. This is
precisely what the ``@mention`` keyword is for.


Better Dialogue Highlighting
----------------------------

The dialogue highlighting was redesigned for 2.5 to not be mere quotes text highlighting, but also support other dialogue styles
that don't rely on quote symbols like English and other languages do. A few features tailored for Spanish were added in 2.5.

However, the Spanish style did not work for Portuguese and Polish, based on user feedback. In this release, the dialogue
highlighting has been redesigned again to accommodate more style variations. There are now three highlighting settings in
Preferences dedicated to this, and you can play around with them to test it out. They are all intended to be used with dashes, but
you decide what symbols they should detect.

To allow for resolving ambiguities where the syntax highlighter guesses something is dialogue, while the author did not intend it to
be, you can use a horizontal bar as a replacement for long dash. They look more or less identical in most fonts, and horizontal bars
are automatically replaced with long dashes in the manuscript. However, the dialogue highlighting feature sees them as different
symbols. Horizontal bars are inserted automatically in the text when you type 4 hyphens after one another.


User Interface Improvements
---------------------------

There are a few improvements to the overall user interface as well.

* URLs starting with "http" are now clickable in both editor and viewer, and are also exported as links in manuscript documents.
* A new edit button is available from the top-right corner if the document viewer. Clicking it will open the current document in the
  document editor.
* The current open document in the editor is now highlighted in the project tree, just like it is in the novel view.
* You can now resize the two parts of the details panel below the Outline View.
* You can select to show the status label and icon for the entries in the Outline View.


Download Links
==============

.. include:: ../generated/download_pre_release.rst
