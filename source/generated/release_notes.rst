.. rubric:: Release Notes

This is a patch release that fixes a few minor bugs and a broken feature.

When opening a document from the Novel Tree or Outline View, the Project Tree would receive focus even when it was hidden. This has been corrected and no focus change is made. The Project Tree now also receives focus automatically when a new Project Item is created.

The backlinks in the Reference Panel below the Document Viewer were no longer working. They have now been fixed. They were broken due to a change in the link format in 2.0.

.. rubric:: Detailed Changelog

**Bugfixes**

* The Reference Panel link would no longer recognise the new, shorter links after the 2.0 project index change. The explicit check has now been made more lenient and will accept any link that is at least 13 characters long (the length of a document handle). Test coverage has been added for handling Reference Panel links. Issue `#1378 <https://github.com/vkbo/novelWriter/issues/1378>`_. PR `#1379 <https://github.com/vkbo/novelWriter/issues/1379>`_.
* The ``setSelectedItem`` method of the project tree class had a ``setFocus()`` call. It should not do this as global focus is handled by the main GUI class, and doing this explicitly in the ``setSelectedItem`` method is presumptuous. Issue `#1369 <https://github.com/vkbo/novelWriter/issues/1369>`_. PR `#1379 <https://github.com/vkbo/novelWriter/issues/1379>`_.

**Usability Fixes**

* When creating new items in the project tree via shortcuts, the project tree receives focus. Since these actions can be accessed when the project tree does not have focus, a user would have to switch focus to be able to open new items. The tree now automatically receives focus when a new item is created. Issue `#1376 <https://github.com/vkbo/novelWriter/issues/1376>`_. PR `#1379 <https://github.com/vkbo/novelWriter/issues/1379>`_.