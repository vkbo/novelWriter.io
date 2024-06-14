Sha256 Checksums
----------------

* | **Linux AppImage:** novelWriter-2.4.4.AppImage
  | Sha256: ``b6cd5bdb4996d3028eb4653ae9fb5fc07e04dd6385472498afa17a44d2fd8af2`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.4.4/novelWriter-2.4.4.AppImage.sha256>`__
* | **Debian Package:** novelwriter_2.4.4_all.deb
  | Sha256: ``224aa4c3e19c61209c867ccd9479c770516b031a83b66f8ffcbca928ae03132c`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.4.4/novelwriter_2.4.4_all.deb.sha256>`__
* | **Windows Installer:** novelwriter-2.4.4-amd64-setup.exe
  | Sha256: ``2180380227c880753f3b2cd5f36f5a7c1c2c1614f045478d7a0f93df5b6d47e7`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.4.4/novelwriter-2.4.4-amd64-setup.exe.sha256>`__
* | **MacOS DMG Image (Intel):** novelWriter-2.4.4-x86_64.dmg
  | Sha256: ``f52857805363743d7c259a352e256510b55c928ad9ea9df4c5f25764650b345f`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.4.4/novelWriter-2.4.4-x86_64.dmg.sha256>`__

.. rubric:: Verify the Checksum

.. tab-set::

   .. tab-item:: Linux

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run one of the commands below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.4.4.AppImage.sha256
         shasum -c novelwriter_2.4.4_all.deb.sha256

   .. tab-item:: Windows

      | :octicon:`chevron-right` Run the following command in PowerShell from the same folder
      | :octicon:`chevron-right` Check the Hash value against the value displayed above

      .. code-block:: powershell

         Get-FileHash -Algorithm SHA256 novelwriter-2.4.4-amd64-setup.exe | Format-List

   .. tab-item:: MacOS

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run the command below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.4.4-x86_64.dmg.sha256
