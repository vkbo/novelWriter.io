:html_theme.sidebar_secondary.remove:

.. _SignPath.io: https://about.signpath.io/
.. _SignPath Foundation: https://signpath.org/

.. div:: main-page-icon

   .. image:: _static/novelwriter-icon.svg
      :class: dark-light

.. _main_home:

***********
novelWriter
***********

.. toctree::
   :maxdepth: 2
   :caption: Contents
   :hidden:

   features
   about/index
   download/index
   releases/index
   Documentation <docs/index>

.. grid:: 1 1 2 2
   :margin: 4 4 0 0
   :gutter: 0
   :padding: 0

   .. grid-item::
      :padding: 1 0 0 3

      **A plain text editor for novels**

      A markdown-like text editor designed for writing novels and larger projects of many smaller
      plain text documents.

      It is designed to be a simple text editor that allows for easy organisation of text files and
      notes, with a meta data syntax for comments, synopsis, and cross-referencing between files,
      and built on plain text files for robustness.

   .. grid-item::
      :padding: 0 0 4 0

      .. image:: images/screenshot_multi.png
         :class: dark-light
         :width: 100%

.. div:: sd-text-center sd-font-weight-bold

   novelWriter is Free and `Open Source <https://www.gnu.org/licenses/gpl-3.0.en.html>`_, and runs on Linux, Windows and MacOS

.. include:: generated/download_main.rst

\* Code signing on Windows is sponsored by `SignPath.io`_, certificate by the `SignPath Foundation`_.
See the :ref:`main_install_signing`.


Other Install Options
---------------------

.. _PPA: https://launchpad.net/~vkbo/+archive/ubuntu/novelwriter
.. _Pre-Release PPA: https://launchpad.net/~vkbo/+archive/ubuntu/novelwriter-pre
.. _Python Package Index: https://pypi.org/project/novelWriter/

.. |ubuntu-logo| image:: images/ubuntu.svg
   :class: dark-light custom-inline-image-tall

.. |pypi-logo| image:: images/pypi.svg
   :class: dark-light custom-inline-image-tall

.. |fedora-logo| image:: images/fedora.svg
   :class: dark-light custom-inline-image-tall


.. grid:: 2
   :margin: 0
   :gutter: 0
   :padding: 0

   .. grid-item::
      :padding: 0 0 0 2
      :margin: 0

      .. grid:: 1
         :margin: 0
         :gutter: 0
         :padding: 0

         .. grid-item::
            :margin: 0
            :padding: 0

            .. code-block:: bash
               :caption: |ubuntu-logo| Add the Ubuntu PPA_ to your system

               sudo add-apt-repository ppa:vkbo/novelwriter
               sudo apt update
               sudo apt install novelwriter

         .. grid-item::
            :margin: 0
            :padding: 0

            .. code-block:: bash
               :caption: |pypi-logo| Install from the `Python Package Index`_

               pip install --user novelwriter

   .. grid-item::
      :padding: 0 0 2 0
      :margin: 0

      .. grid:: 1
         :margin: 0
         :gutter: 0
         :padding: 0

         .. grid-item::
            :margin: 0
            :padding: 0

            .. code-block:: bash
               :caption: |fedora-logo| Install on Fedora 41+

               sudo dnf install novelwriter

            *Note that the Fedora package is maintained by Fedora package managers and will have a delayed release cycle.*


* For more download options, including pre-releases and checksum files, see the :ref:`main_download` page.
* You can also use the Ubuntu PPA on other Debian-based distros. See :ref:`main_install_linux` for more details.
* Ubuntu pre-releases are available on the `Pre-Release PPA`_, by adding ``ppa:vkbo/novelwriter-pre`` instead.
