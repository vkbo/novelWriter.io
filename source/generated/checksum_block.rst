Sha256 Checksums
----------------

* | **Linux AppImage:** novelWriter-2.0.7-py3.10-manylinux_2_28_x86_64.AppImage
  | Sha256: ``a493fbdb16f4ee9d63bf42568a0d057f9093fa9c69f9a6ba1d6c043673c3b2a4`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.0.7/novelWriter-2.0.7-py3.10-manylinux_2_28_x86_64.AppImage.sha256>`__
* | **Debian Package:** novelwriter_2.0.7_all.deb
  | Sha256: ``aeaa3e1bc797ea1527313e4b64b691a516b013e0e5d160e4644421881162736f`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.0.7/novelwriter_2.0.7_all.deb.sha256>`__
* | **Windows Installer:** novelwriter-2.0.7-py3.10.11-win10-amd64-setup.exe
  | Sha256: ``342f4257bfbcbfa5fc0655c7f7c980c94fbc94967f0f91d2bc71d8a2b872ac88`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.0.7/novelwriter-2.0.7-py3.10.11-win10-amd64-setup.exe.sha256>`__
* | **MacOS DMG Image:** novelWriter-2.0.7-macos.dmg
  | Sha256: ``9e5fc4fd03e636f64e7b6ae38e52190f21d76b62a4519a746f853d4ebdeec3a0`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.0.7/novelWriter-2.0.7-macos.dmg.sha256>`__

.. rubric:: Verify the Checksum

.. tab-set::

   .. tab-item:: Linux

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run one of the commands below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.0.7-py3.10-manylinux_2_28_x86_64.AppImage.sha256
         shasum -c novelwriter_2.0.7_all.deb.sha256

   .. tab-item:: Windows

      | :octicon:`chevron-right` Run the following command in PowerShell from the same folder
      | :octicon:`chevron-right` Check the Hash value against the value displayed above

      .. code-block:: powershell

         Get-FileHash -Algorithm SHA256 novelwriter-2.0.7-py3.10.11-win10-amd64-setup.exe | Format-List

   .. tab-item:: MacOS

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run the command below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.0.7-macos.dmg.sha256
