Sha256 Checksums
----------------

* | **Linux AppImage:** novelWriter-2.2.AppImage
  | Sha256: ``c6b3549a9ce3271cd4d893b00c6fd7c4064a27e9ae0d5b4d8d379c091957a871`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.2/novelWriter-2.2.AppImage.sha256>`__
* | **Debian Package:** novelwriter_2.2_all.deb
  | Sha256: ``d19b9f63b9c44685d7814db8905a58309acb51ec48874f174c9abeeb40f2b205`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.2/novelwriter_2.2_all.deb.sha256>`__
* | **Windows Installer:** novelwriter-2.2-amd64-setup.exe
  | Sha256: ``9c2abefc726b18754307e574f42460022cbc413d3e264ed56a7dacf3d6e57aff`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.2/novelwriter-2.2-amd64-setup.exe.sha256>`__
* | **MacOS DMG Image:** novelWriter-2.2.dmg
  | Sha256: ``b82894ad03062d7eecf0e2611986e3d92b43a9602b5f9b52fcf584472b607df2`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.2/novelWriter-2.2.dmg.sha256>`__

.. rubric:: Verify the Checksum

.. tab-set::

   .. tab-item:: Linux

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run one of the commands below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.2.AppImage.sha256
         shasum -c novelwriter_2.2_all.deb.sha256

   .. tab-item:: Windows

      | :octicon:`chevron-right` Run the following command in PowerShell from the same folder
      | :octicon:`chevron-right` Check the Hash value against the value displayed above

      .. code-block:: powershell

         Get-FileHash -Algorithm SHA256 novelwriter-2.2-amd64-setup.exe | Format-List

   .. tab-item:: MacOS

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run the command below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.2.dmg.sha256
