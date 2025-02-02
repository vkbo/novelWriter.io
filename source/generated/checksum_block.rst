Sha256 Checksums
----------------

* | **Linux AppImage:** novelWriter-2.6.1.AppImage
  | Sha256: ``bc173f93be03c7566bcbd2aaf01bfef689db601d46da8e524cc28c8d89310cd1`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.6.1/novelWriter-2.6.1.AppImage.sha256>`__
* | **Debian Package:** novelwriter_2.6.1_all.deb
  | Sha256: ``e840e16ae1e99f67800ac269604e373fb409b9647e89bef31bb6d8e9c2271b4f`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.6.1/novelwriter_2.6.1_all.deb.sha256>`__
* | **Windows Installer:** novelwriter-2.6.1-amd64-setup.exe
  | Sha256: ``1bf0f01d1cc7ee59d415b18e1b82c352f9bffdf7d5db44aa46f05b1be33e2780`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.6.1/novelwriter-2.6.1-amd64-setup.exe.sha256>`__
* | **MacOS DMG Image (Intel):** novelWriter-2.6.1-x86_64.dmg
  | Sha256: ``a501901a1049e032c9f726e154ffac83e54cd858127650ff0a8c87e2305c367f`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.6.1/novelWriter-2.6.1-x86_64.dmg.sha256>`__
* | **MacOS DMG Image (M1):** novelWriter-2.6.1-aarch64.dmg
  | Sha256: ``ace2e1cd3333cf4bb7b9c69cbf8763627a984106fa697e1f1cc42e617aafe973`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.6.1/novelWriter-2.6.1-aarch64.dmg.sha256>`__

.. rubric:: Verify the Checksum

.. tab-set::

   .. tab-item:: Linux

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run one of the commands below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.6.1.AppImage.sha256
         shasum -c novelwriter_2.6.1_all.deb.sha256

   .. tab-item:: Windows

      | :octicon:`chevron-right` Run the following command in PowerShell from the same folder
      | :octicon:`chevron-right` Check the Hash value against the value displayed above

      .. code-block:: powershell

         Get-FileHash -Algorithm SHA256 novelwriter-2.6.1-amd64-setup.exe | Format-List

   .. tab-item:: MacOS

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run the command below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.6.1-x86_64.dmg.sha256
