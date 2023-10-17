Sha256 Checksums
----------------

* | **Linux AppImage:** novelWriter-2.1.AppImage
  | Sha256: ``bdae7c23920097ff360b64937b999f8aaf42fa94c561dc6ffe2d80116ff21fb5`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.1/novelWriter-2.1.AppImage.sha256>`__
* | **Debian Package:** novelwriter_2.1_all.deb
  | Sha256: ``66c4b1c0ca3c227c3f903cbb02b61024d0e5cc3846995d75f12c819e93e0c3b1`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.1/novelwriter_2.1_all.deb.sha256>`__
* | **Windows Installer:** novelwriter-2.1-amd64-setup.exe
  | Sha256: ``cc96f2fafc1c5210949c70e0e9bf2b5ed7fdc133880228441a5377876978a478`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.1/novelwriter-2.1-amd64-setup.exe.sha256>`__
* | **MacOS DMG Image:** novelWriter-2.1.dmg
  | Sha256: ``e6d7cc7ef7ae84e8d23ec7c5d637752bf81a5224af5ebf748b1fb35e89bdcf7b`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.1/novelWriter-2.1.dmg.sha256>`__

.. rubric:: Verify the Checksum

.. tab-set::

   .. tab-item:: Linux

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run one of the commands below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.1.AppImage.sha256
         shasum -c novelwriter_2.1_all.deb.sha256

   .. tab-item:: Windows

      | :octicon:`chevron-right` Run the following command in PowerShell from the same folder
      | :octicon:`chevron-right` Check the Hash value against the value displayed above

      .. code-block:: powershell

         Get-FileHash -Algorithm SHA256 novelwriter-2.1-amd64-setup.exe | Format-List

   .. tab-item:: MacOS

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run the command below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.1.dmg.sha256
