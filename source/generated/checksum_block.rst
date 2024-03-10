Sha256 Checksums
----------------

* | **Linux AppImage:** novelWriter-2.3.AppImage
  | Sha256: ``d1120e0098033ebb73423f93fea80219834f7c366b53dde9419cf8866e16cef8`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.3/novelWriter-2.3.AppImage.sha256>`__
* | **Debian Package:** novelwriter_2.3_all.deb
  | Sha256: ``7dd6ed3ec4b2ee552bee7dd20ed57eae676d8f2b74239f35241d9991dc0137c4`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.3/novelwriter_2.3_all.deb.sha256>`__
* | **Windows Installer:** novelwriter-2.3-amd64-setup.exe
  | Sha256: ``2c0457f16c6d83807108facee65dd55fef2c15049a609ed0ea2c41c144fb4d96`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.3/novelwriter-2.3-amd64-setup.exe.sha256>`__
* | **MacOS DMG Image:** novelWriter-2.3.dmg
  | Sha256: ``fd71e8f3bbac0344d7c86383ca9b693d79b74e76e2cbd77a42ea0d769ed88589`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.3/novelWriter-2.3.dmg.sha256>`__

.. rubric:: Verify the Checksum

.. tab-set::

   .. tab-item:: Linux

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run one of the commands below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.3.AppImage.sha256
         shasum -c novelwriter_2.3_all.deb.sha256

   .. tab-item:: Windows

      | :octicon:`chevron-right` Run the following command in PowerShell from the same folder
      | :octicon:`chevron-right` Check the Hash value against the value displayed above

      .. code-block:: powershell

         Get-FileHash -Algorithm SHA256 novelwriter-2.3-amd64-setup.exe | Format-List

   .. tab-item:: MacOS

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run the command below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.3.dmg.sha256
