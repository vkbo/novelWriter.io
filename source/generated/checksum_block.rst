Sha256 Checksums
----------------

* | **Linux AppImage:** novelWriter-2.5.3.AppImage
  | Sha256: ``0a2be9e3c2363e336005d90bffcef013dee3a077801b9a1a200d33305b8a344c`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.5.3/novelWriter-2.5.3.AppImage.sha256>`__
* | **Debian Package:** novelwriter_2.5.3_all.deb
  | Sha256: ``f8f1e7017da68ad9d5ad979190e565588ddd67ca64c1c139da0840986dd4173b`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.5.3/novelwriter_2.5.3_all.deb.sha256>`__
* | **Windows Installer:** novelwriter-2.5.3-amd64-setup.exe
  | Sha256: ``4cb5d359e4dd17065186e977e3817bf9793c4f2ae71cc218d30dd0284bd8c091`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.5.3/novelwriter-2.5.3-amd64-setup.exe.sha256>`__
* | **MacOS DMG Image (Intel):** novelWriter-2.5.3-x86_64.dmg
  | Sha256: ``9bb2d292ecac9297cf26b2a1eafe969812a34714c6d185d29c116c2464bf51ad`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.5.3/novelWriter-2.5.3-x86_64.dmg.sha256>`__
* | **MacOS DMG Image (M1):** novelWriter-2.5.3-aarch64.dmg
  | Sha256: ``1586d06659f727583a853aae5a6aec371b156879c688a3b5633ad1acb7f906b1`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.5.3/novelWriter-2.5.3-aarch64.dmg.sha256>`__

.. rubric:: Verify the Checksum

.. tab-set::

   .. tab-item:: Linux

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run one of the commands below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.5.3.AppImage.sha256
         shasum -c novelwriter_2.5.3_all.deb.sha256

   .. tab-item:: Windows

      | :octicon:`chevron-right` Run the following command in PowerShell from the same folder
      | :octicon:`chevron-right` Check the Hash value against the value displayed above

      .. code-block:: powershell

         Get-FileHash -Algorithm SHA256 novelwriter-2.5.3-amd64-setup.exe | Format-List

   .. tab-item:: MacOS

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run the command below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.5.3-x86_64.dmg.sha256
