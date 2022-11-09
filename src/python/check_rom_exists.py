import os

def checkRomExists(rom_file, root_path):
  exist_status = False
  for root, dirs, files in os.walk(root_path, topdown=True):
    dirs.clear() 
    if rom_file in files:
      exist_status = True
  return exist_status
