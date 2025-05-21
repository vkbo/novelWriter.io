Sha256 Checksum Files
---------------------

Checksum files are released alongside the packages. These files can be used to verify the downloaded package.

* **Linux AppImage:** :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.6.3/novelWriter-2.6.3.AppImage.sha256>`__
* **Debian Package:** :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.6.3/novelwriter_2.6.3_all.deb.sha256>`__
* **Windows Installer:** :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.6.3/novelwriter-2.6.3-amd64-setup.exe.sha256>`__
* **MacOS DMG Image (Intel):** :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.6.3/novelWriter-2.6.3-x86_64.dmg.sha256>`__
* **MacOS DMG Image (M1):** :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.6.3/novelWriter-2.6.3-aarch64.dmg.sha256>`__

.. rubric:: Verify the Checksum

.. tab-set::

   .. tab-item:: Linux

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run one of the commands below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.6.3.AppImage.sha256
         shasum -c novelwriter_2.6.3_all.deb.sha256

   .. tab-item:: Windows

      | :octicon:`chevron-right` Run the following command in PowerShell from the same folder
      | :octicon:`chevron-right` Check the Hash value against the value displayed above

      .. code-block:: powershell

         Get-FileHash -Algorithm SHA256 novelwriter-2.6.3-amd64-setup.exe | Format-List

   .. tab-item:: MacOS

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run the command below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.6.3-x86_64.dmg.sha256
