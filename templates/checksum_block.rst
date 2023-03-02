Sha256 Checksums
----------------

* | **Linux AppImage:** {appimage_name}
  | Sha256: ``{appimage_shasum}`` :octicon:`download` `ShaSum File <{appimage_shasumfile}>`__
* | **Debian Package:** {debian_name}
  | Sha256: ``{debian_shasum}`` :octicon:`download` `ShaSum File <{debian_shasumfile}>`__
* | **Windows Installer:** {winexe_name}
  | Sha256: ``{winexe_shasum}`` :octicon:`download` `ShaSum File <{winexe_shasumfile}>`__
* | **MacOS DMG Image:** {macdmg_name}
  | Sha256: ``{macdmg_shasum}`` :octicon:`download` `ShaSum File <{macdmg_shasumfile}>`__

.. rubric:: Verify the Checksum

.. tab-set::

   .. tab-item:: Linux

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
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

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run the command below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c {macdmg_name}.sha256
