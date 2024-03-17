Sha256 Checksums
----------------

* | **Linux AppImage:** novelWriter-2.3.1.AppImage
  | Sha256: ``6774b30b7e9ca76697c54e522a32ca09019f4acac2fcab9a2dc3d8b346a71666`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.3.1/novelWriter-2.3.1.AppImage.sha256>`__
* | **Debian Package:** novelwriter_2.3.1_all.deb
  | Sha256: ``76377a6adaeb7a518b2b5d740c1deed66b0b5b7147431fd30beed0893b59a326`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.3.1/novelwriter_2.3.1_all.deb.sha256>`__
* | **Windows Installer:** novelwriter-2.3.1-amd64-setup.exe
  | Sha256: ``523b1879e778326046199f2b4e990077bd9fc002f5ccdf52f9ddec16d0915c3c`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.3.1/novelwriter-2.3.1-amd64-setup.exe.sha256>`__
* | **MacOS DMG Image:** novelWriter-2.3.1.dmg
  | Sha256: ``350d6d0b055863d6d9846f29c7a7e4e2d666b9c5d42b4190ed568293adc91375`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.3.1/novelWriter-2.3.1.dmg.sha256>`__

.. rubric:: Verify the Checksum

.. tab-set::

   .. tab-item:: Linux

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run one of the commands below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.3.1.AppImage.sha256
         shasum -c novelwriter_2.3.1_all.deb.sha256

   .. tab-item:: Windows

      | :octicon:`chevron-right` Run the following command in PowerShell from the same folder
      | :octicon:`chevron-right` Check the Hash value against the value displayed above

      .. code-block:: powershell

         Get-FileHash -Algorithm SHA256 novelwriter-2.3.1-amd64-setup.exe | Format-List

   .. tab-item:: MacOS

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run the command below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.3.1.dmg.sha256
