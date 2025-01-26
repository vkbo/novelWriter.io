Sha256 Checksums
----------------

* | **Linux AppImage:** novelWriter-2.6.AppImage
  | Sha256: ``9e1a73ccbdee5f9e56350ae6babd72daa626dc5913a520608732485d58c4d05b`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.6/novelWriter-2.6.AppImage.sha256>`__
* | **Debian Package:** novelwriter_2.6_all.deb
  | Sha256: ``589e17e39c0a070d59d39d45f52bd3e0f0b42746fff509c970b0e1f3d3d8338d`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.6/novelwriter_2.6_all.deb.sha256>`__
* | **Windows Installer:** novelwriter-2.6-amd64-setup.exe
  | Sha256: ``4b2e0201cd1beac746ba08b705ac25f48b331a636c4d01e2ca21abade981d130`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.6/novelwriter-2.6-amd64-setup.exe.sha256>`__
* | **MacOS DMG Image (Intel):** novelWriter-2.6-x86_64.dmg
  | Sha256: ``5212c6e986976301e6b5eb7c29416d5cb63c40d21733f054ab40f75e8376bf8e`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.6/novelWriter-2.6-x86_64.dmg.sha256>`__
* | **MacOS DMG Image (M1):** novelWriter-2.6-aarch64.dmg
  | Sha256: ``488da1be890a0a38acc07fea743791e3624863f079d94b2cff7049919df922ab`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.6/novelWriter-2.6-aarch64.dmg.sha256>`__

.. rubric:: Verify the Checksum

.. tab-set::

   .. tab-item:: Linux

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run one of the commands below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.6.AppImage.sha256
         shasum -c novelwriter_2.6_all.deb.sha256

   .. tab-item:: Windows

      | :octicon:`chevron-right` Run the following command in PowerShell from the same folder
      | :octicon:`chevron-right` Check the Hash value against the value displayed above

      .. code-block:: powershell

         Get-FileHash -Algorithm SHA256 novelwriter-2.6-amd64-setup.exe | Format-List

   .. tab-item:: MacOS

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run the command below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.6-x86_64.dmg.sha256
