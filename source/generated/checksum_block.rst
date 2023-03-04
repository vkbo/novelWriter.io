Sha256 Checksums
----------------

* | **Linux AppImage:** novelWriter-2.0.6-py3.10-manylinux_2_28_x86_64.AppImage
  | Sha256: ``98380ccd8dee025f4839bddcbf1b0140c57b92c911be9081980d4bfdde10e03c`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.0.6/novelWriter-2.0.6-py3.10-manylinux_2_28_x86_64.AppImage.sha256>`__
* | **Debian Package:** novelwriter_2.0.6_all.deb
  | Sha256: ``3c64d0b21b23096f0ba3b0d210d947a83c2cc0859f9b53b1a35137c4f2bb66d8`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.0.6/novelwriter_2.0.6_all.deb.sha256>`__
* | **Windows Installer:** novelwriter-2.0.6-py3.10.10-win10-amd64-setup.exe
  | Sha256: ``370ce821eedc01b8173a17c771543a7f62c2d6f5b120b00994fc34dbdca53d1a`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.0.6/novelwriter-2.0.6-py3.10.10-win10-amd64-setup.exe.sha256>`__
* | **MacOS DMG Image:** novelWriter-2.0.6-macos.dmg
  | Sha256: ``8e5f12110b5f3b93a6445d34a5b5e45bab0167b3474690f9aa1b8fd5bcfde9c8`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.0.6/novelWriter-2.0.6-macos.dmg.sha256>`__

.. rubric:: Verify the Checksum

.. tab-set::

   .. tab-item:: Linux

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run one of the commands below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.0.6-py3.10-manylinux_2_28_x86_64.AppImage.sha256
         shasum -c novelwriter_2.0.6_all.deb.sha256

   .. tab-item:: Windows

      | :octicon:`chevron-right` Run the following command in PowerShell from the same folder
      | :octicon:`chevron-right` Check the Hash value against the value displayed above

      .. code-block:: powershell

         Get-FileHash -Algorithm SHA256 novelwriter-2.0.6-py3.10.10-win10-amd64-setup.exe | Format-List

   .. tab-item:: MacOS

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run the command below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.0.6-macos.dmg.sha256
