.. _main_release_2_0:

***********
Release 2.0
***********

| **Release Date:** November 28, 2022
| **Patches:** :ref:`2.0.1 <main_release_2_0_1>`, :ref:`2.0.2 <main_release_2_0_2>`, :ref:`2.0.3 <main_release_2_0_3>`,
  :ref:`2.0.4 <main_release_2_0_4>`, :ref:`2.0.5 <main_release_2_0_5>`, :ref:`2.0.6 <main_release_2_0_6>`,
  :ref:`2.0.7 <main_release_2_0_7>`

Release Notes
=============

This release includes a major update to the way your project is managed. It also modernises the user interface. The project file
format has also been updated, and your projects will be upgraded the first time you open them in this release.

There are some major changes under the hood in this release. A lot of the code has been rewritten and split up into smaller
components. A lot of this is to make it more efficient, but also to make it more modular in preparation for planned future
additions. Most of these changes don't affect you as the user, but there are also a number of big feature changes that you will
notice.

User Interface Changes
----------------------

The tabs used to switch between the Project Tree and Novel Tree, as well as between the Editor and Outline views, have been replaced
with a side bar. The side bar is located on the left side of the main window, and gives you the option to select between
"Project Tree View", "Novel Tree View" and "Outline Tree View". They correspond to the previous tabs.

The side bar also includes a shortcut to the "Build Novel Project" tool. The "Project Details", "Writing Statistics" and "Settings"
buttons that were previously below the project tree are now located at the bottom of the side bar.

All three views have also been given updates. They each have a label and a toolbar. The Project Tree View has a dropdown with quick
links to all your root folders, which should make it easier to navigate a large project tree. You can activate the link menu by
pressing :kbd:`Ctrl+L` while in the Project Tree, so you don't need to move your mouse.

A dropdown menu with all the options for adding new items to your project has also been added to this toolbar. This too can be
activated directly with a shortcut, :kbd:`Ctrl+N`. More options are available under the menu button, and there are also a set of
move up and down buttons for moving items.

The Novel Tree View and Novel Outline View have also received toolbars and controls that let you select which data to show, and
customise the view.

Changes to Project Structure
----------------------------

A number of changes have been made to how you organise your project in the Project Tree View. For instance, you are now allowed to
add as many root folders as you want, and as many of each kind as you want. Several users have asked for the ability to add multiple
Novel folders, so the old restriction of only one of each has been removed.

You can now also move documents freely between all folders. The Status or Importance values will switch place depending on the type
of root folder your document is in, but the other value should be preserved if you move the document back. Previously, they were
saved as the same value in your project, so moving them would imply they were overwritten. The new project file format introduced
with this release has no such restriction.

Your documents are now also able to have other documents as child items. This is another feature added based on feedback. You no
longer need to make a chapter folder and add chapter files inside it together with the scene documents. You can add the scene
documents directly under the chapter document and drop the folder entirely. If needed, you can convert an existing folder into a
document at any time. However, you are not allowed to convert a document into a folder.

The check mark icon that previously indicated whether a document was included or not in a manuscript build has been replaced with an
active/inactive flag. This was done in preparation for changes to the Build Novel Project tool which will come in the next release.
The active/inactive flag is now primarily just an indicator to you as the writer whether the document is to be considered a part of
your project or not. That said, an inactive setting still causes it to be excluded from the Novel Tree View and the Novel Outline
View.

The context (right click) menu for the Project Tree has also been updated. You can make nearly all changes to the item directly from
this menu, with the exception of editing the item label, which still requires a dialog box.

The Split and Merge tools have been rewritten from scratch. You should now have multiple options on how to structure the resulting
document or documents. You can access the new tools from the "Transform" submenu when right-clicking a project item that supports
splitting or merging.

Novel and Outline View
----------------------

The Novel Tree View and Novel Outline View panels have been given a new design. The heading level is now shown as an indent with a
coloured bar that uses the same colour coding as the document icons. They are technically no longer tree views, but rather a Table
of Contents of a specific novel root folder. If you have multiple novel root folders, you can select which one to view.

In the Novel Tree View, you now also have the option to hide or show a third column of data. Currently, you can choose between
"Point of View Character", "Focus Character" and "Novel Plot". If you referenced more than one in the document, the column will only
show the first entry, so make sure the most important one is listed first in your document if you use this feature. An arrow icon
is also visible at the end of each row in the tree, and if you click on it, a tool tip should pop up showing you all the meta data
collected for that specific heading in your text.

Other Changes
-------------

There has been a lot of changes under the hood as well, especially in regards to how the project structure is handled and saved. The
project index has also been almost completely rewritten, and now collects information about your project more efficiently. This
improves the way the project tree determines which document icon to show you, and it also makes the Novel Tree View more informative
as the data there is updated a lot more frequently.

The New Project Wizard has been updated with some new features, and simplified a bit. The Project Settings dialog has been updated
to reflect some of the same changes.


Patch Releases
==============

.. _main_release_2_0_1:

Patch 2.0.1
-----------

**Release Date:** November 29, 2022

This is a patch release that fixes a minor issues with loading custom GUI themes that haven't been updated to include the icon theme
setting. The patch also updates the French translation.

.. _main_release_2_0_2:

Patch 2.0.2
-----------

**Release Date:** December 1, 2022

This is a patch release that fixes a minor issues with syntax highlighting not updating when the highlighting preferences were
changed. It also fixes an issue that broke the FreeBSD release.

.. _main_release_2_0_3:

Patch 2.0.3
-----------

**Release Date:** January 8, 2023

This is a patch release that fixes a few bugs and usability issues. The editing of status and importance labels in Project Settings
should now be a bit more intuitive. Opening a document from the Outline View that is already open in the editor should now switch to
the editor view. The convert folder to note or document feature in the project tree has also been fixed. Some icons have been
updated and a rendering issue with one of them fixed. Chinese, Norwegian, US English, German and Spanish translations have been
updated as well. A new credits tab has been added to the About dialog box, replacing the Credits section on the main About tab.

.. _main_release_2_0_4:

Patch 2.0.4
-----------

**Release Date:** January 29, 2023

This is a patch release that fixes a bug where novelWriter would crash if PyQt5 version 5.15.8 was installed and imported.

.. _main_release_2_0_5:

Patch 2.0.5
-----------

**Release Date:** February 12, 2023

This is a patch release that fixes a number of minor bugs and usability issues.

The Project Details dialog now properly updates when another project is opened, and the "Total editing time" value has a less
ambiguous time format. The editor no longer inserts blank lines if block formats are applied to an empty line. The optional last
column in the Novel Tree will now show all items of the selected type, not only the first, and the column size can be adjusted from
the same menu where the column content is selected. The Open Document build output has been updated to ODF 1.3 extended format, and
passes validation.

An Italian translation has been added, and Russian is currently available for project builds. A full translation into Russian is on
its way.

.. _main_release_2_0_6:

Patch 2.0.6
-----------

**Release Date:** February 26, 2023

This is a patch release that fixes a few minor bugs and a broken feature.

When opening a document from the Novel Tree or Outline View, the Project Tree would receive focus even when it was hidden. This has
been corrected and no focus change is made. The Project Tree now also receives focus automatically when a new Project Item is
created.

The backlinks in the Reference Panel below the Document Viewer were no longer working. They have now been fixed. They were broken
due to a change in the link format in 2.0.

.. _main_release_2_0_7:

Patch 2.0.7
-----------

**Release Date:** April 16, 2023

This is a patch release that fixes a few issues and adds a Japanese translation.

The issues were mostly related to spell checking. In particular, issues with finding the word boundary when using underscore
characters for italics markup. These issues should now be resolved. In addition, escaped markup characters are now rendered properly
in HTML and ODT build formats.

A few usability improvements have also been made. The Add Item menu in the project tree no longer shows the options to create Novel
Documents when an item in the tree is selected that cannot hold such a document. In addition, the "Change Label" context menu entry
has been changed to say "Rename", which is a more logical choice.


Download Links
==============

Past release packages are available for download on `GitHub <https://github.com/vkbo/novelWriter/releases>`__.

| :octicon:`mark-github` `Download Release 2.0.7 <https://github.com/vkbo/novelWriter/releases/tag/v2.0.7>`__
| :octicon:`mark-github` `Download Release 2.0.6 <https://github.com/vkbo/novelWriter/releases/tag/v2.0.6>`__
| :octicon:`mark-github` `Download Release 2.0.5 <https://github.com/vkbo/novelWriter/releases/tag/v2.0.5>`__
| :octicon:`mark-github` `Download Release 2.0.4 <https://github.com/vkbo/novelWriter/releases/tag/v2.0.4>`__
| :octicon:`mark-github` `Download Release 2.0.3 <https://github.com/vkbo/novelWriter/releases/tag/v2.0.3>`__
| :octicon:`mark-github` `Download Release 2.0.2 <https://github.com/vkbo/novelWriter/releases/tag/v2.0.2>`__
| :octicon:`mark-github` `Download Release 2.0.1 <https://github.com/vkbo/novelWriter/releases/tag/v2.0.1>`__
| :octicon:`mark-github` `Download Release 2.0 <https://github.com/vkbo/novelWriter/releases/tag/v2.0>`__
