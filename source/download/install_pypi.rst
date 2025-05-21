.. _main_install_pypi:

********************
Installing from PyPi
********************

.. _PyPi: https://pypi.org/project/novelWriter/
.. _python.org: https://www.python.org/downloads/

novelWriter is also available on the Python Package Index, or PyPi_. This install method works on
all supported operating systems with a suitable Python environment already installed.

To install from PyPi you must first have the ``python`` and ``pip`` commands available on your
system. You can download Python from `python.org`_. It is recommended that you install the latest
version. If you are on Windows, also make sure to select the "Add Python to PATH" option during
installation.

To install novelWriter from PyPi, use the following command:

.. code-block:: bash

   pip install novelwriter

To upgrade an existing installation, use:

.. code-block:: bash

   pip install --upgrade novelwriter

When installing via pip, novelWriter can be launched from command line with:

.. code-block:: bash

   novelwriter

Make sure the install location for pip is in your PATH variable. This is not always the case by
default, and then you may get a "Not Found" error when running the ``novelwriter`` command.
