Sha256 Checksums
----------------

* | **Linux AppImage:** novelWriter-2.5.1.AppImage
  | Sha256: ``8fb1980d47a98f7b165a7d58b1ec1aaac78cb6a5d63e89e42517d3c7fbb3f2a7`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.5.1/novelWriter-2.5.1.AppImage.sha256>`__
* | **Debian Package:** novelwriter_2.5.1_all.deb
  | Sha256: ``44cd31b79e175b9f08c676e97bdb9712e397a0dfc9282b2585722e5fd637c184`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.5.1/novelwriter_2.5.1_all.deb.sha256>`__
* | **Windows Installer:** novelwriter-2.5.1-amd64-setup.exe
  | Sha256: ``be40dd49aeb7863dab86cdf61bee2ebdc58b5fc6cccb62cd09799f03b4a79a79`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.5.1/novelwriter-2.5.1-amd64-setup.exe.sha256>`__
* | **MacOS DMG Image (Intel):** novelWriter-2.5.1-x86_64.dmg
  | Sha256: ``e2e2fd68de4cc196468d00acd16744e875eae1c49936ce20ccf85ae547d4eb5e`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.5.1/novelWriter-2.5.1-x86_64.dmg.sha256>`__
* | **MacOS DMG Image (M1):** novelWriter-2.5.1-aarch64.dmg
  | Sha256: ``8bfbddb76b57439ce44db3931922662e259ed121222ad70fa1c2549ee4c1e2cc`` :octicon:`download` `ShaSum File <https://github.com/vkbo/novelWriter/releases/download/v2.5.1/novelWriter-2.5.1-aarch64.dmg.sha256>`__

.. rubric:: Verify the Checksum

.. tab-set::

   .. tab-item:: Linux

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run one of the commands below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.5.1.AppImage.sha256
         shasum -c novelwriter_2.5.1_all.deb.sha256

   .. tab-item:: Windows

      | :octicon:`chevron-right` Run the following command in PowerShell from the same folder
      | :octicon:`chevron-right` Check the Hash value against the value displayed above

      .. code-block:: powershell

         Get-FileHash -Algorithm SHA256 novelwriter-2.5.1-amd64-setup.exe | Format-List

   .. tab-item:: MacOS

      | :octicon:`chevron-right` Download the corresponding ShaSum File to the same location
      | :octicon:`chevron-right` Run the command below in a terminal window in the same folder

      .. code-block:: bash

         shasum -c novelWriter-2.5.1-x86_64.dmg.sha256
