.. _AppImage: https://appimage.org/
.. _Ubuntu: https://ubuntu.com/
.. _Debian: https://www.debian.org/
.. _Linux Mint: https://linuxmint.com/
.. _novelWriter Repository: https://github.com/vkbo/novelWriter/
.. _SignPath.io: https://about.signpath.io/
.. _SignPath Foundation: https://signpath.org/

| **Release Version:** {release_version}
| **Release Date:** {release_date}
| **Release Notes:** :ref:`{release_ref}`
| **Release Feedback:** :octicon:`comment-discussion` `Discussion <{discuss_url}>`__
| **Release on GitHub:** :octicon:`mark-github` `GitHub <{release_url}>`__


Linux
-----

.. grid:: 2
   :margin: 0
   :padding: 0
   :gutter: 0

   .. grid-item::
      :columns: 2
      :padding: 0 0 0 4

      .. image:: /images/linux.svg
         :class: dark-light

   .. grid-item::
      :columns: 10

      .. grid:: 1
         :margin: 0
         :gutter: 4
         :padding: 0

         .. grid-item-card::
            :class-header: nw-sd-os-card-header

            **AppImage**
            ^^^^^^^^^^^^
            The AppImage_ should run on any recent Linux distro.

            **Download:** :octicon:`download` `{appimage_name} <{appimage_url}>`__ [{appimage_size}]
            :bdg-link-primary-line:`Checksum File <{appimage_shasumfile}>`

         .. grid-item-card::
            :class-header: nw-sd-os-card-header

            **Debian Package (Trixie, Ubuntu 25.10+)**
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            The package is built for Debian_ Trixie, but should also work for newer Ubuntu_, `Linux Mint`_ and other Debian-based releases.

            **Download:** :octicon:`download` `{debian_name} <{debian_url}>`__ [{debian_size}]
            :bdg-link-primary-line:`Checksum File <{debian_shasumfile}>`

         .. grid-item-card::
            :class-header: nw-sd-os-card-header

            **Debian Package (Bookworm, Ubuntu 24.04)**
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            The package is built for Debian_ Bookworm, but should also work for older Ubuntu_, `Linux Mint`_ and other Debian-based releases.

            **Download:** :octicon:`download` `{debian_old_name} <{debian_old_url}>`__ [{debian_old_size}]
            :bdg-link-primary-line:`Checksum File <{debian_old_shasumfile}>`


Windows
-------

.. grid:: 2
   :margin: 0
   :padding: 0
   :gutter: 0

   .. grid-item::
      :columns: 2
      :padding: 0 0 0 4

      .. image:: /images/windows10.svg
         :class: dark-light

   .. grid-item::
      :columns: 10

      .. grid:: 1
         :margin: 0
         :gutter: 4
         :padding: 0

         .. grid-item-card::
            :class-header: nw-sd-os-card-header

            **Setup Installer**
            ^^^^^^^^^^^^^^^^^^^
            This is a standard setup installer for Windows. It is made for Windows 10 or newer.

            **Download:** :octicon:`download` `{winexe_name} <{winexe_url}>`__ [{winexe_size}]
            :bdg-link-primary-line:`Checksum File <{winexe_shasumfile}>`

            Free code signing is provided by `SignPath.io`_, certificate by `SignPath Foundation`_.


MacOS
-----

.. attention::

   The DMG images for MacOS will be discontinued from release 2.9.
   See `this discussion <https://github.com/vkbo/novelWriter/discussions/2618>`__ for more details.

.. grid:: 2
   :margin: 0
   :padding: 0
   :gutter: 0

   .. grid-item::
      :columns: 2
      :padding: 0 0 0 4

      .. image:: /images/macos.svg
         :class: dark-light

   .. grid-item::
      :columns: 10

      .. grid:: 1
         :margin: 0
         :gutter: 4
         :padding: 0

         .. grid-item-card::
            :class-header: nw-sd-os-card-header

            **DMG Image for Intel**
            ^^^^^^^^^^^^^^^^^^^^^^^

            This is a DMG image for MacOS with x86_64 architecture.

            **Download:** :octicon:`download` `{macx86_name} <{macx86_url}>`__ [{macx86_size}]
            :bdg-link-primary-line:`Checksum File <{macx86_shasumfile}>`

         .. grid-item-card::
            :class-header: nw-sd-os-card-header

            **DMG Image for Apple Silicon (M1)**
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

            This is a DMG image for MacOS with aarch64 architecture.

            **Download:** :octicon:`download` `{macarm_name} <{macarm_url}>`__ [{macarm_size}]
            :bdg-link-primary-line:`Checksum File <{macarm_shasumfile}>`


Other Packages
--------------

.. grid:: 2
   :margin: 0
   :padding: 0
   :gutter: 0

   .. grid-item::
      :columns: 2
      :padding: 0 0 0 4

      .. image:: /images/package.png
         :class: dark-light

   .. grid-item::
      :columns: 10

      .. grid:: 1
         :margin: 0
         :gutter: 4
         :padding: 0

         .. grid-item-card::
            :class-header: nw-sd-os-card-header

            **Python Wheel**
            ^^^^^^^^^^^^^^^^

            The Wheel package can be installed with ``pip install <file_path>``.

            **Download:** :octicon:`download` `{wheel_name} <{wheel_url}>`__ [{wheel_size}]
            :bdg-link-primary-line:`Checksum File <{wheel_shasumfile}>`

         .. grid-item-card::
            :class-header: nw-sd-os-card-header

            **Source Code**
            ^^^^^^^^^^^^^^^

            The source code packages are archived files of the entire source code.

            | **Download:** :octicon:`download` `novelWriter-{short_version}.zip <{zip_url}>`__
            | **Download:** :octicon:`download` `novelWriter-{short_version}.tar.gz <{tar_url}>`__
            
            See also the `novelWriter Repository`_.
