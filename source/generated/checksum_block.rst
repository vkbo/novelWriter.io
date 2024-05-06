Sha256 Checksums
----------------

* | **Linux AppImage:** novelWriter-2.4.1.AppImage
  | Sha256: ``6af6d24ae7512541af4b17c445b94730e514dab094750da482598cf8aa2fa46c`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.4.1/novelWriter-2.4.1.AppImage.sha256>`__
* | **Debian Package:** novelwriter_2.4.1_all.deb
  | Sha256: ``631481ca7b62ae5d69b6b06b1cb8ce487c9f25888feb6819454c1353bc58ac82`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.4.1/novelwriter_2.4.1_all.deb.sha256>`__
* | **Windows Installer:** novelwriter-2.4.1-amd64-setup.exe
  | Sha256: ``6f743fb47056273bca3db80eb3b241e51cc71f9eebbad2da5e6b39872219727b`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.4.1/novelwriter-2.4.1-amd64-setup.exe.sha256>`__
* | **MacOS DMG Image (Intel):** novelWriter-2.4.1-x86_64.dmg
  | Sha256: ``0f4beb0d626863937005ec3d8fe42b726f1d0112278ec8fa9f477fdce5c3bf84`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.4.1/novelWriter-2.4.1-x86_64.dmg.sha256>`__

.. rubric:: Verify the Checksum

.. tab-set::

   .. tab-item:: Linux

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run one of the commands below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.4.1.AppImage.sha256
         shasum -c novelwriter_2.4.1_all.deb.sha256

   .. tab-item:: Windows

      | :octicon:`chevron-right` Run the following command in PowerShell from the same folder
      | :octicon:`chevron-right` Check the Hash value against the value displayed above

      .. code-block:: powershell

         Get-FileHash -Algorithm SHA256 novelwriter-2.4.1-amd64-setup.exe | Format-List

   .. tab-item:: MacOS

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run the command below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.4.1-x86_64.dmg.sha256
