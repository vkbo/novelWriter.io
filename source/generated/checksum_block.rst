Sha256 Checksums
----------------

* | **Linux AppImage:** novelWriter-2.5.2.AppImage
  | Sha256: ``0448282b3404f1e31bc7e79cf9aa1329758b8352ff8d1729e41b1ae20d8d1703`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.5.2/novelWriter-2.5.2.AppImage.sha256>`__
* | **Debian Package:** novelwriter_2.5.2_all.deb
  | Sha256: ``ccb1c82671d1ce53ced1c05efbe1edf21a0b339d65d4ea3291285762c996f06c`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.5.2/novelwriter_2.5.2_all.deb.sha256>`__
* | **Windows Installer:** novelwriter-2.5.2-amd64-setup.exe
  | Sha256: ``77af1e1220c1fce9571cb3931802e4b479a78e5aa2ceada0a388e3e60c0c8c7d`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.5.2/novelwriter-2.5.2-amd64-setup.exe.sha256>`__
* | **MacOS DMG Image (Intel):** novelWriter-2.5.2-x86_64.dmg
  | Sha256: ``8e9dd98896adfdfc30d9222b4798d86ce6ba82e8eccb319b7e52c40d76448652`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.5.2/novelWriter-2.5.2-x86_64.dmg.sha256>`__
* | **MacOS DMG Image (M1):** novelWriter-2.5.2-aarch64.dmg
  | Sha256: ``3e0c961160af698c82ab7c59d4747b957418b78c8f8741d1dfac306d8eee30c0`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.5.2/novelWriter-2.5.2-aarch64.dmg.sha256>`__

.. rubric:: Verify the Checksum

.. tab-set::

   .. tab-item:: Linux

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run one of the commands below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.5.2.AppImage.sha256
         shasum -c novelwriter_2.5.2_all.deb.sha256

   .. tab-item:: Windows

      | :octicon:`chevron-right` Run the following command in PowerShell from the same folder
      | :octicon:`chevron-right` Check the Hash value against the value displayed above

      .. code-block:: powershell

         Get-FileHash -Algorithm SHA256 novelwriter-2.5.2-amd64-setup.exe | Format-List

   .. tab-item:: MacOS

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run the command below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.5.2-x86_64.dmg.sha256
