import os
import project_info as _ProjectInfo

def checkRomExists():
  exist_status = False
  ProjInfo = _ProjectInfo.ProjectInfo()
  rom_file = ProjInfo.romFileWithoutFolder()
  root_path = ProjInfo.romFolderPath()
  for root, dirs, files in os.walk(root_path, topdown=True):
    dirs.clear() 
    if rom_file in files:
      exist_status = True
  return exist_status
