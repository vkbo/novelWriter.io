Sha256 Checksums
----------------

* | **Linux AppImage:** novelWriter-2.4.3.AppImage
  | Sha256: ``f5dc307f0aa0c193afc158d0187ba5d601caac69823486f50306c9a06ed4a424`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.4.3/novelWriter-2.4.3.AppImage.sha256>`__
* | **Debian Package:** novelwriter_2.4.3_all.deb
  | Sha256: ``6b188c7c01fff17bf9aa5be3e9e373a96ee75db5b2b518c5438a615359b3dd2a`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.4.3/novelwriter_2.4.3_all.deb.sha256>`__
* | **Windows Installer:** novelwriter-2.4.3-amd64-setup.exe
  | Sha256: ``a28217577ec47de488adc8518718d74102d1ce2af70678dec964dbcb429aa180`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.4.3/novelwriter-2.4.3-amd64-setup.exe.sha256>`__
* | **MacOS DMG Image (Intel):** novelWriter-2.4.3-x86_64.dmg
  | Sha256: ``5db5b58154970d9246854d2492ad67df148eb5d938fc629076f090f5a5763f40`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.4.3/novelWriter-2.4.3-x86_64.dmg.sha256>`__

.. rubric:: Verify the Checksum

.. tab-set::

   .. tab-item:: Linux

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run one of the commands below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.4.3.AppImage.sha256
         shasum -c novelwriter_2.4.3_all.deb.sha256

   .. tab-item:: Windows

      | :octicon:`chevron-right` Run the following command in PowerShell from the same folder
      | :octicon:`chevron-right` Check the Hash value against the value displayed above

      .. code-block:: powershell

         Get-FileHash -Algorithm SHA256 novelwriter-2.4.3-amd64-setup.exe | Format-List

   .. tab-item:: MacOS

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run the command below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.4.3-x86_64.dmg.sha256
