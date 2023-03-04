:html_theme.sidebar_secondary.remove:

.. div:: main-page-icon

   .. image:: _static/novelwriter-icon.svg
      :class: dark-light

***********
novelWriter
***********

.. toctree::
   :maxdepth: 2
   :caption: Contents
   :hidden:

   features
   download
   about/index
   Documentation <docs/index>

.. grid:: 2
   :margin: 4 4 0 0
   :gutter: 0
   :padding: 0

   .. grid-item::
      :padding: 1 0 0 3

      **A markdown-like editor for novels**

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

.. include:: generated/download_block.rst


Other Install Options
---------------------

.. _PPA: https://launchpad.net/~vkbo/+archive/ubuntu/novelwriter
.. _Python Package Index: https://pypi.org/project/novelWriter/

.. |ubuntu-logo| image:: images/ubuntu.svg
   :class: dark-light custom-inline-image-tall

.. |pypi-logo| image:: images/pypi.svg
   :class: dark-light custom-inline-image-tall


.. grid::
   :margin: 0
   :gutter: 4
   :padding: 0

   .. grid-item::

      .. code-block:: bash
         :caption: |ubuntu-logo| Add the Ubuntu PPA_ to your system:

         sudo add-apt-repository ppa:vkbo/novelwriter
         sudo apt update && sudo apt install novelwriter

   .. grid-item::

      .. code-block:: bash
         :caption: |pypi-logo| Install from the `Python Package Index`_:

         pip install --user novelwriter

For more download options, including pre-releases, see the :ref:`main_download` page.

.. include:: generated/checksum_block.rst
