.. _main_install_pypi:

********************
Installing from PyPi
********************

.. _PyPi: https://pypi.org/project/novelWriter/
.. _python.org: https://www.python.org/downloads/
.. _pipx installation: https://pipx.pypa.io/latest/installation/

novelWriter is also available on the Python Package Index, or PyPi_. This install method works on
all supported operating systems with a suitable Python environment already installed.

To install from PyPi you must first have the ``python`` and ``pip`` commands available on your
system. You can download Python from `python.org`_. It is recommended that you install the latest
version. If you are on Windows, also make sure to select the "Add Python to PATH" option during
installation.

It is recommended to install novelWriter as a tool using ``pipx``. See the `pipx installation`
documentation for more details.

To install novelWriter from PyPi, use the following command:

.. code-block:: bash

   pipx install novelwriter

To upgrade an existing installation, use:

.. code-block:: bash

   pipx install --upgrade novelwriter

When installed, novelWriter can be launched from the command line with:

.. code-block:: bash

   novelwriter
