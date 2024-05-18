Sha256 Checksums
----------------

* | **Linux AppImage:** novelWriter-2.4.2.AppImage
  | Sha256: ``0d2ddd08795aa33a0e97bd7ec3b92c5f08d0862ba40d556924a25b5053ab5535`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.4.2/novelWriter-2.4.2.AppImage.sha256>`__
* | **Debian Package:** novelwriter_2.4.2_all.deb
  | Sha256: ``0823bb80b56091c86110cdeb9cf37d4a9de774f35d5a8a8fda65b69186258506`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.4.2/novelwriter_2.4.2_all.deb.sha256>`__
* | **Windows Installer:** novelwriter-2.4.2-amd64-setup.exe
  | Sha256: ``5900d2293fb8f91883a49bcd6f744623ce377de8f0827f7f20e3ad133d33afdd`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.4.2/novelwriter-2.4.2-amd64-setup.exe.sha256>`__
* | **MacOS DMG Image (Intel):** novelWriter-2.4.2-x86_64.dmg
  | Sha256: ``edfc981c757e196451596c654e1713ddd7e439d5c909682a89e5a023c35a381c`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.4.2/novelWriter-2.4.2-x86_64.dmg.sha256>`__

.. rubric:: Verify the Checksum

.. tab-set::

   .. tab-item:: Linux

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run one of the commands below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.4.2.AppImage.sha256
         shasum -c novelwriter_2.4.2_all.deb.sha256

   .. tab-item:: Windows

      | :octicon:`chevron-right` Run the following command in PowerShell from the same folder
      | :octicon:`chevron-right` Check the Hash value against the value displayed above

      .. code-block:: powershell

         Get-FileHash -Algorithm SHA256 novelwriter-2.4.2-amd64-setup.exe | Format-List

   .. tab-item:: MacOS

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run the command below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.4.2-x86_64.dmg.sha256
