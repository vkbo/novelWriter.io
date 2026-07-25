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

.. |linux-logo| image:: ../images/linux.svg
   :class: dark-light custom-inline-image-title

.. |windows10-logo| image:: ../images/windows10.svg
   :class: dark-light custom-inline-image-title

.. |package-logo| image:: ../images/package.png
   :class: dark-light custom-inline-image-title


Linux |linux-logo|
------------------

AppImage
^^^^^^^^

.. card::

   The AppImage_ should run on any recent Linux distro.

   :octicon:`download` `{appimage_name} <{appimage_url}>`__ [{appimage_size}]
   :bdg-link-primary-line:`Checksum File <{appimage_shasumfile}>`


Debian Package
^^^^^^^^^^^^^^

.. card::

   These packages are built for Debian_, but should also work for newer Ubuntu_, `Linux Mint`_ and other Debian-based
   distros. The "oldstable" version is needed for Debian Bookworm, Ubuntu 24.04, and distros of a similar age.

   | :octicon:`download` `{debian_name} <{debian_url}>`__ [{debian_size}]
     :bdg-link-primary-line:`Checksum File <{debian_shasumfile}>` :bdg-warning-line:`Trixie, Ubuntu 25.10+`
   | :octicon:`download` `{debian_old_name} <{debian_old_url}>`__ [{debian_old_size}]
     :bdg-link-primary-line:`Checksum File <{debian_old_shasumfile}>` :bdg-warning-line:`Bookworm, Ubuntu 24.04`


Windows |windows10-logo|
------------------------

Setup Installer
^^^^^^^^^^^^^^^

.. card::

   This is a standard setup installer for Windows. It is made for Windows 10 or newer.

   :octicon:`download` `{winexe_name} <{winexe_url}>`__ [{winexe_size}]
   :bdg-link-primary-line:`Checksum File <{winexe_shasumfile}>`

   Free code signing is provided by `SignPath.io`_, certificate by `SignPath Foundation`_.


Other Packages |package-logo|
-----------------------------

Python Wheel
^^^^^^^^^^^^

.. card::

   A standard Python wheel package is available for installation via pip.

   :octicon:`download` `{wheel_name} <{wheel_url}>`__ [{wheel_size}]
   :bdg-link-primary-line:`Checksum File <{wheel_shasumfile}>`


Source Code
^^^^^^^^^^^

.. card::

   The source code packages are archived files of the entire source code.

   | :octicon:`download` `novelWriter-{short_version}.zip <{zip_url}>`__
   | :octicon:`download` `novelWriter-{short_version}.tar.gz <{tar_url}>`__

   See also the `novelWriter Repository`_.

.. note::

   For the time being, the MacOS releases have been discontinued. There is currently no one available to maintain these
   releases. This is an open source project, and it depends on volunteers and contributors to run.
   See `this discussion <https://github.com/vkbo/novelWriter/discussions/2618>`__ for more details.

   If you own a Mac and have a Python environment set up, you can still install the Python package of novelWriter and
   run the latest release. See :ref:`main_install_pypi` for more details.
