import os

def checkRomExists(rom_file, root_path):
  exist_status = False
  for root, dirs, files in os.walk(root_path):
    for filename in files:
      if filename == rom_file:
        exist_status = True
  return exist_status
