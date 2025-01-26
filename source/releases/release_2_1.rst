.. _main_release_2_1:

***********
Release 2.1
***********

| **Release Date:** October 17, 2023
| **Patches:** :ref:`2.1.1 <main_release_2_1_1>`


Release Notes
=============

The primary focus of this release has been a complete redesign of the Build Tool, that is, the tool that assembles your project into
a manuscript document. The new tool, called the "Manuscript Build Tool" allows you to define multiple build definitions for your
project. The build definitions are edited in a new Manuscript Build Settings dialog, with a lot more options than the old tool.

The reason for this redesign is a long list of feature requests that could not easily be accommodated in the old, much simpler tool.
Far from all the features have been added yet, but now that the new tool is in place, they will be gradually added in the coming
releases.

The key feature added in this release is the extended control you now have for selecting exactly what part of your project is
included in a given build definition. You have the same filters for selecting documents and notes, and turning on or off root
folders as before, but you can now easily override on a per-document basis what is included or excluded in addition to the filter.

A second major improvement is a better tool to format your manuscript headings. You no longer have to look up formatting codes and
add them manually. Instead, there is now a heading format editor in the Build Settings dialog for creating the header format, with
syntax highlighting included.


Patch Releases
==============

.. _main_release_2_1_1:

Patch 2.1.1
-----------

**Release Date:** November 5, 2023

This is a patch release that fixes a layout issue and internationalisation issues with the new Manuscript Build tool. It also fixes
a number of issues related to bugs in the underlying Qt framework that affects drag and drop functionality in the project tree.
These issues were mostly only affecting Debian Linux package releases.

Other, minor issues related to updating the editor on colour theme change and project word list changes have been fixed as well.
See the full changelog for more details.


Download Links
==============

Past release packages are available for download on `GitHub <https://github.com/vkbo/novelWriter/releases>`__.

| :octicon:`mark-github` `Download Release 2.1.1 <https://github.com/vkbo/novelWriter/releases/tag/v2.1.1>`__
| :octicon:`mark-github` `Download Release 2.1 <https://github.com/vkbo/novelWriter/releases/tag/v2.1>`__
