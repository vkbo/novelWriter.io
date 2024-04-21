.. _main_release_2_2:

***********
Release 2.2
***********

| **Release Date:** December 17, 2023
| **Patches:** :ref:`2.2.1 <main_release_2_2_1>`

Release Notes
=============

This release comes with a number of new features. These are some highlights.

In addition to the common Markdown style formatting for bold, italic and strike through, a set of new shortcodes have been added.
The shortcodes are far more flexible than the Markdown style syntax, and can be used for more complex formatting cases. Like when
you need to add multiple, overlapping formats, or add emphasis to just a part of a word. The shortcodes also allow for underline,
subscript and superscript, which the Markdown syntax does not. The new formats are available in the "Format" menu, and in a new
toolbar in the editor that can be enabled by clicking the three dots in the top--left corner. The shortcode format was chosen
because it can later be extended to include other requested features as well. Please have a look at the documentation for more
details about the new shortcodes.

The Tags and References system has been improved. The tags themselves are no longer case sensitive when you use them in references,
but they are still displayed as you typed them in the tag definition when they are displayed in the user interface. Starting to type
the ``@`` symbol in the text editor, on a new line, will now open an auto-completer menu which will display available options. It
may not display all of your tags if you have a lot of them, but starting to type more characters will filter the list down further.

You can now automatically create a note file for a new tag that you have added to a reference list in a document, but is not yet
defined in a project note. So, for instance, if you come up with a new character while writing, and add a new tag to your ``@char``
references, you can right-click the new tag and create a new note for that entry directly. In addition, it is now also possible to
right-click a heading in an open document and set the item label in the project tree to match the heading.

In addition to the changes in the editor, the "References" panel below the document viewer has also been completely redesigned. It
now shows all the references to the document you are viewing as a list, with a lot more details than before. In addition, tabs in
the panel will appear to show all the tags you have defined in your notes, sorted as one tab per category. Like for instance
Characters, Locations, Objects, etc. You can also give each note a short description comment on the same format as the summary
comments for chapters and scenes. The short description comment can be added from the "Insert" menu under "Special Comments".

The last major change in this release is the new multi-select feature in the project tree. You can now select multiple documents
and folders using the mouse while pressing :kbd:`Ctrl` or :kbd:`Shift`. By right-clicking the selected items, you can perform a
limited set of operations on all of them, like changing active status, and the status or importance labels. You can also drag and
drop multiple items under the condition that all the selected items are in the same folder, at the same level. This restriction is
in place due to limitations in the framework novelWriter is based on. But this should help in cases where multiple documents need to
be moved in and out of folders or between folders. Note that adding the multi-select feature meant that the undo feature of the
project tree had to be removed. It may be added back later.


Patch Releases
==============

.. _main_release_2_2_1:

Patch 2.2.1
-----------

**Release Date:** January 27, 2024

This is a patch release that fixes an issue where the Project View would sometimes switch to the Novel View when a new item was
created. This patch also includes updated translations for German and Chinese.


Download Links
==============

Past release packages are available for download on `GitHub <https://github.com/vkbo/novelWriter/releases>`__.

| :octicon:`mark-github` `Download Release 2.2.1 <https://github.com/vkbo/novelWriter/releases/tag/v2.2.1>`__
| :octicon:`mark-github` `Download Release 2.2 <https://github.com/vkbo/novelWriter/releases/tag/v2.2>`__
