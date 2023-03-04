.. _AppImage website: https://appimage.org/
.. _Ubuntu: https://ubuntu.com/
.. _Debian: https://www.debian.org/
.. _Linux Mint: https://linuxmint.com/
.. _novelWriter Repository: https://github.com/vkbo/novelWriter/

| **Release Version:** Version 2.0.6
| **Release Date:** February 26, 2023
| **Release Page:** :octicon:`mark-github` `GitHub <https://github.com/vkbo/novelWriter/releases/tag/v2.0.6>`__

.. dropdown:: Release Notes
   :animate: fade-in-slide-down
   :icon: info

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

.. tab-set::

   .. tab-item:: Linux

      **AppImage**
         The AppImage should run on any recent Linux distro. See the `AppImage website`_ for more info.

         | **Download:** :octicon:`download` `novelWriter-2.0.6-py3.10-manylinux_2_28_x86_64.AppImage <https://github.com/vkbo/novelWriter/releases/download/v2.0.6/novelWriter-2.0.6-py3.10-manylinux_2_28_x86_64.AppImage>`__ [  98.7 MB ]
         | **Checksum:** :octicon:`hash` ``98380ccd8dee025f4839bddcbf1b0140c57b92c911be9081980d4bfdde10e03c`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.0.6/novelWriter-2.0.6-py3.10-manylinux_2_28_x86_64.AppImage.sha256>`__

      **AppImage (Legacy)**
         You should try the ``manylinux_2_28`` version first. This may not work for older distos, in which case you may want to download the ``manylinux_2_24`` version instead.

         | **Download:** :octicon:`download` `novelWriter-2.0.6-py3.10-manylinux_2_24_x86_64.AppImage <https://github.com/vkbo/novelWriter/releases/download/v2.0.6/novelWriter-2.0.6-py3.10-manylinux_2_24_x86_64.AppImage>`__ [ 100 MB ]
         | **Checksum:** :octicon:`hash` ``d7d99b7b4b598e51044a81edb6c4c17de90823ecfc9cb210df069bb8e88a3f6b`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.0.6/novelWriter-2.0.6-py3.10-manylinux_2_24_x86_64.AppImage.sha256>`__

      **Debian Package**
         The package is built for Debian_, but should also work for Ubuntu_ and `Linux Mint`_.

         | **Download:** :octicon:`download` `novelwriter_2.0.6_all.deb <https://github.com/vkbo/novelWriter/releases/download/v2.0.6/novelwriter_2.0.6_all.deb>`__ [  1.91 MB ]
         | **Checksum:** :octicon:`hash` ``3c64d0b21b23096f0ba3b0d210d947a83c2cc0859f9b53b1a35137c4f2bb66d8`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.0.6/novelwriter_2.0.6_all.deb.sha256>`__


   .. tab-item:: Windows

      **Setup Installer**
         This is a standard setup installer for Windows. It is made for Windows 10 or newer.

         | **Download:** :octicon:`download` `novelwriter-2.0.6-py3.10.10-win10-amd64-setup.exe <https://github.com/vkbo/novelWriter/releases/download/v2.0.6/novelwriter-2.0.6-py3.10.10-win10-amd64-setup.exe>`__ [  33.4 MB ]
         | **Checksum:** :octicon:`hash` ``370ce821eedc01b8173a17c771543a7f62c2d6f5b120b00994fc34dbdca53d1a`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.0.6/novelwriter-2.0.6-py3.10.10-win10-amd64-setup.exe.sha256>`__


   .. tab-item:: MacOS

      **DMG Image**
         This is a DMG image for MacOS, and should work on MacOS 10 or higher.

         | **Download:** :octicon:`download` `novelWriter-2.0.6-macos.dmg <https://github.com/vkbo/novelWriter/releases/download/v2.0.6/novelWriter-2.0.6-macos.dmg>`__ [  95.7 MB ]
         | **Checksum:** :octicon:`hash` ``8e5f12110b5f3b93a6445d34a5b5e45bab0167b3474690f9aa1b8fd5bcfde9c8`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.0.6/novelWriter-2.0.6-macos.dmg.sha256>`__


   .. tab-item:: Other Packages

      **Python Wheel**
         The Wheel package can be installed with ``pip install <file_path>``.

         | **Download:** :octicon:`download` `novelWriter-2.0.6-py3-none-any.whl <https://github.com/vkbo/novelWriter/releases/download/v2.0.6/novelWriter-2.0.6-py3-none-any.whl>`__ [  2.27 MB ]
         | **Checksum:** :octicon:`hash` ``383e8c54ab4395b5c712156dae5aa23a828725689b964f9dd69bf8b9a58befbc`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.0.6/novelWriter-2.0.6-py3-none-any.whl.sha256>`__

      **Source Code**
         The source code packages are archived files of the entire source code. See also the `novelWriter Repository`_.

         | **Download:** :octicon:`download` `novelWriter-2.0.6.zip <https://api.github.com/repos/vkbo/novelWriter/zipball/v2.0.6>`__
         | **Download:** :octicon:`download` `novelWriter-2.0.6.tar.gz <https://api.github.com/repos/vkbo/novelWriter/tarball/v2.0.6>`__

