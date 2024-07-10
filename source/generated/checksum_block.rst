Sha256 Checksums
----------------

* | **Linux AppImage:** novelWriter-2.5.AppImage
  | Sha256: ``43be11f6a304f86446ab4c9c6be45de43d1b0311db5a1b9f042d249aa7b74175`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.5/novelWriter-2.5.AppImage.sha256>`__
* | **Debian Package:** novelwriter_2.5_all.deb
  | Sha256: ``419b6a0711414a0bfb0ec53d899d778fd9ea03578d4c9e1eca4d511db3814eef`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.5/novelwriter_2.5_all.deb.sha256>`__
* | **Windows Installer:** novelwriter-2.5-amd64-setup.exe
  | Sha256: ``f12ee45a74e31ea933501de72ba9192725faec76012894cf1c008500f710c7e9`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.5/novelwriter-2.5-amd64-setup.exe.sha256>`__
* | **MacOS DMG Image (Intel):** novelWriter-2.5-x86_64.dmg
  | Sha256: ``0ddf08536906308696a2737261692bb6d552b5e9453a083d235ac102bbbd12ec`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.5/novelWriter-2.5-x86_64.dmg.sha256>`__
* | **MacOS DMG Image (M1):** novelWriter-2.5-aarch64.dmg
  | Sha256: ``d1aa6aa1226ad6c0d65dc7649c208306400a3e3d59bdc13f3595a006fd023b71`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.5/novelWriter-2.5-aarch64.dmg.sha256>`__

.. rubric:: Verify the Checksum

.. tab-set::

   .. tab-item:: Linux

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run one of the commands below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.5.AppImage.sha256
         shasum -c novelwriter_2.5_all.deb.sha256

   .. tab-item:: Windows

      | :octicon:`chevron-right` Run the following command in PowerShell from the same folder
      | :octicon:`chevron-right` Check the Hash value against the value displayed above

      .. code-block:: powershell

         Get-FileHash -Algorithm SHA256 novelwriter-2.5-amd64-setup.exe | Format-List

   .. tab-item:: MacOS

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run the command below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.5-x86_64.dmg.sha256
