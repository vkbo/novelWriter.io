Sha256 Checksums
----------------

* | **Linux AppImage:** novelWriter-2.1.1.AppImage
  | Sha256: ``6a572066fd1d11e115ffe78270be8df7ff8f2d9d005f8f01b3fb4c9ee56e1295`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.1.1/novelWriter-2.1.1.AppImage.sha256>`__
* | **Debian Package:** novelwriter_2.1.1_all.deb
  | Sha256: ``39e328775b5505014527be9df8bdd1b040e160d9db4569cba99cb1d14741b942`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.1.1/novelwriter_2.1.1_all.deb.sha256>`__
* | **Windows Installer:** novelwriter-2.1.1-amd64-setup.exe
  | Sha256: ``a1474c478081bfcdf269cae73ebf92819e4d296b257e7122a783ba0a59048131`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.1.1/novelwriter-2.1.1-amd64-setup.exe.sha256>`__
* | **MacOS DMG Image:** novelWriter-2.1.1.dmg
  | Sha256: ``064f64ba6d579b6680fa0e0b9bc5652bfa8cb57f50114144a8ea032596850282`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.1.1/novelWriter-2.1.1.dmg.sha256>`__

.. rubric:: Verify the Checksum

.. tab-set::

   .. tab-item:: Linux

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run one of the commands below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.1.1.AppImage.sha256
         shasum -c novelwriter_2.1.1_all.deb.sha256

   .. tab-item:: Windows

      | :octicon:`chevron-right` Run the following command in PowerShell from the same folder
      | :octicon:`chevron-right` Check the Hash value against the value displayed above

      .. code-block:: powershell

         Get-FileHash -Algorithm SHA256 novelwriter-2.1.1-amd64-setup.exe | Format-List

   .. tab-item:: MacOS

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run the command below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.1.1.dmg.sha256
