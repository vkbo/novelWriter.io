Checksum Files
--------------

Checksum files are released alongside the packages. These files can be used to verify the downloaded package.

* **Linux AppImage:** :octicon:`download` `Checksum File <{appimage_shasumfile}>`__
* **Debian Package:** :octicon:`download` `Checksum File <{debian_shasumfile}>`__
* **Windows Installer:** :octicon:`download` `Checksum File <{winexe_shasumfile}>`__
* **MacOS DMG Image (Intel):** :octicon:`download` `Checksum File <{macx86_shasumfile}>`__
* **MacOS DMG Image (M1):** :octicon:`download` `Checksum File <{macarm_shasumfile}>`__

.. rubric:: Verify the Checksum

.. tab-set::

   .. tab-item:: Linux

      | :octicon:`chevron-right` Download the corresponding Checksum File to the same location
      | :octicon:`chevron-right` Run one of the commands below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c {appimage_name}.sha256
         shasum -c {debian_name}.sha256

   .. tab-item:: Windows

      | :octicon:`chevron-right` Run the following command in PowerShell from the same folder
      | :octicon:`chevron-right` Check the Hash value against the value displayed above

      .. code-block:: powershell

         Get-FileHash -Algorithm SHA256 {winexe_name} | Format-List

   .. tab-item:: MacOS

      | :octicon:`chevron-right` Download the corresponding Checksum File to the same location
      | :octicon:`chevron-right` Run the command below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c {macx86_name}.sha256
