Sha256 Checksums
----------------

* | **Linux AppImage:** novelWriter-2.6.3.AppImage
  | Sha256: ``6099b28216eced371faca6d5cd52a31388964a25d0dfdde9cf62438fbbeb0887`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.6.3/novelWriter-2.6.3.AppImage.sha256>`__
* | **Debian Package:** novelwriter_2.6.3_all.deb
  | Sha256: ``490fb0cb37c9bd0d6551ffd8e09d35e9e6d313e02796b69ee68ff60708e6416c`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.6.3/novelwriter_2.6.3_all.deb.sha256>`__
* | **Windows Installer:** novelwriter-2.6.3-amd64-setup.exe
  | Sha256: ``9c52a9cbdd35b12608319d7c3d531fc7f483ea3513dec688c1f839efd80c5460`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.6.3/novelwriter-2.6.3-amd64-setup.exe.sha256>`__
* | **MacOS DMG Image (Intel):** novelWriter-2.6.3-x86_64.dmg
  | Sha256: ``34ba50008b0749d406c63458b68d236011c3031f92a36974be4bae233d48e261`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.6.3/novelWriter-2.6.3-x86_64.dmg.sha256>`__
* | **MacOS DMG Image (M1):** novelWriter-2.6.3-aarch64.dmg
  | Sha256: ``845bee441b92fa4018fb4dc50f3e4411a4f3174f9a30adf0f398256fd83a9487`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.6.3/novelWriter-2.6.3-aarch64.dmg.sha256>`__

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
