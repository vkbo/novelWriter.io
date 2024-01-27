Sha256 Checksums
----------------

* | **Linux AppImage:** novelWriter-2.2.1.AppImage
  | Sha256: ``a1a54ad99b4f7de351b99089b5f6cfc6cb7effa0aff3165ecc3125f1c81614ae`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.2.1/novelWriter-2.2.1.AppImage.sha256>`__
* | **Debian Package:** novelwriter_2.2.1_all.deb
  | Sha256: ``756e74b2945b866512c93fcf867a457e72db7722b36d9f8d8978c962be468a8a`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.2.1/novelwriter_2.2.1_all.deb.sha256>`__
* | **Windows Installer:** novelwriter-2.2.1-amd64-setup.exe
  | Sha256: ``79e0701d75ed0ae2690acd1fca03d46b6dbcf68722405212ab76b3605ee1bf75`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.2.1/novelwriter-2.2.1-amd64-setup.exe.sha256>`__
* | **MacOS DMG Image:** novelWriter-2.2.1.dmg
  | Sha256: ``b67101db1d0f358664370a40d1f7cfe25d02f160849d0de87261af3e7c0a6b96`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.2.1/novelWriter-2.2.1.dmg.sha256>`__

.. rubric:: Verify the Checksum

.. tab-set::

   .. tab-item:: Linux

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run one of the commands below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.2.1.AppImage.sha256
         shasum -c novelwriter_2.2.1_all.deb.sha256

   .. tab-item:: Windows

      | :octicon:`chevron-right` Run the following command in PowerShell from the same folder
      | :octicon:`chevron-right` Check the Hash value against the value displayed above

      .. code-block:: powershell

         Get-FileHash -Algorithm SHA256 novelwriter-2.2.1-amd64-setup.exe | Format-List

   .. tab-item:: MacOS

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run the command below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.2.1.dmg.sha256
