Sha256 Checksums
----------------

* | **Linux AppImage:** novelWriter-2.6.2.AppImage
  | Sha256: ``cf80158f4c4ea5361ac9ec1d8eb2574edd185c805a44150b1beb2df8af616c5a`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.6.2/novelWriter-2.6.2.AppImage.sha256>`__
* | **Debian Package:** novelwriter_2.6.2_all.deb
  | Sha256: ``696425752efbfb2980178ce780f952a17abe439e560e799c8e5166c0ef57365e`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.6.2/novelwriter_2.6.2_all.deb.sha256>`__
* | **Windows Installer:** novelwriter-2.6.2-amd64-setup.exe
  | Sha256: ``b6822aee7a9b54a3cac3ea459d25c64986ba8e5c33068c0298f4721f3f5b3bcc`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.6.2/novelwriter-2.6.2-amd64-setup.exe.sha256>`__
* | **MacOS DMG Image (Intel):** novelWriter-2.6.2-x86_64.dmg
  | Sha256: ``9d82940eb0fc8ff1ca011a1107631696f74220fd48b0c0e89787c91f88854446`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.6.2/novelWriter-2.6.2-x86_64.dmg.sha256>`__
* | **MacOS DMG Image (M1):** novelWriter-2.6.2-aarch64.dmg
  | Sha256: ``28d3aff17c2af5d2cb9b4fccd15a034d204154a50c2379c1b9f7ce1697d05492`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.6.2/novelWriter-2.6.2-aarch64.dmg.sha256>`__

.. rubric:: Verify the Checksum

.. tab-set::

   .. tab-item:: Linux

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run one of the commands below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.6.2.AppImage.sha256
         shasum -c novelwriter_2.6.2_all.deb.sha256

   .. tab-item:: Windows

      | :octicon:`chevron-right` Run the following command in PowerShell from the same folder
      | :octicon:`chevron-right` Check the Hash value against the value displayed above

      .. code-block:: powershell

         Get-FileHash -Algorithm SHA256 novelwriter-2.6.2-amd64-setup.exe | Format-List

   .. tab-item:: MacOS

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run the command below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.6.2-x86_64.dmg.sha256
