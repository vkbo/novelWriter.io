Sha256 Checksums
----------------

* | **Linux AppImage:** novelWriter-2.4.AppImage
  | Sha256: ``743cdc120defe28bbca759b5f19e96f9c69c430026316ecbbc470a1b7cf60e67`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.4/novelWriter-2.4.AppImage.sha256>`__
* | **Debian Package:** novelwriter_2.4_all.deb
  | Sha256: ``a0f343d1494e5d60edcb741e79b0617f9cdb0e195beef10629f04c4cb0667b5f`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.4/novelwriter_2.4_all.deb.sha256>`__
* | **Windows Installer:** novelwriter-2.4-amd64-setup.exe
  | Sha256: ``1589127a67acf41b242338250b7949a08f7510470d430425d96f45968a238068`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.4/novelwriter-2.4-amd64-setup.exe.sha256>`__
* | **MacOS DMG Image (Intel):** novelWriter-2.4-x86_64.dmg
  | Sha256: ``112a43f8614be36b2a59c1ab4d77dee6621603b72c5376dc18bb6ccba8104f94`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.4/novelWriter-2.4-x86_64.dmg.sha256>`__

.. rubric:: Verify the Checksum

.. tab-set::

   .. tab-item:: Linux

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run one of the commands below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.4.AppImage.sha256
         shasum -c novelwriter_2.4_all.deb.sha256

   .. tab-item:: Windows

      | :octicon:`chevron-right` Run the following command in PowerShell from the same folder
      | :octicon:`chevron-right` Check the Hash value against the value displayed above

      .. code-block:: powershell

         Get-FileHash -Algorithm SHA256 novelwriter-2.4-amd64-setup.exe | Format-List

   .. tab-item:: MacOS

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run the command below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.4-x86_64.dmg.sha256
