import sys
from get_history_context  import getHistoryContent
from get_project_name     import getProjectName
from get_rom_file         import getRomFile
from get_project_path     import getProjectPath
from check_rom_exists     import checkRomExists
from copy_file_to_server  import copyFileToServer
from add_rom_server_path  import addRomServerPath
from add_dear_all         import addDearAll
from add_html_tags        import addHtmlTags
from open_outlook         import openOutlook
from copy_to_clipboard    import copyToClipboard

# This is use to diable stdout buffering
class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def writelines(self, datas):
       self.stream.writelines(datas)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)


def main():

  sys.stdout = Unbuffered(sys.stdout)

  history_path_global = sys.argv[1].replace("\\", "/")
  if(history_path_global == ""):
    raise FileNotFoundError("release_exp: No History.txt input")
  server_path_global  = sys.argv[2].replace("\\", "/").replace("\\\\", "//")
  if(server_path_global == ""):
    raise FileNotFoundError("release_exp: No server location input")
  is_email_global     = sys.argv[3]
  is_clipboard_global = sys.argv[4]
  project_path = ''
  rom_file_name= ''

  # Get history Content
  print("Status_Anchor: Reading history contents")
  history_content = getHistoryContent(history_path_global)

  # Get Project Name
  print("Status_Anchor: Getting Project name from History.txt")
  project_name = getProjectName(history_content)

  # Get rom file
  print("Status_Anchor: Getting ROM file name from History.txt")
  rom_file_name_with_folder = getRomFile(history_content).replace("\\", "/")
  print("[python] rom file name with folder: " + rom_file_name_with_folder)
  # In case rom file is not in root path
  rom_file_name = rom_file_name_with_folder.split("/")[-1]
  print("[python] rom file name without folder: " + rom_file_name)

  # Get Project Path
  print("Status_Anchor: Getting Project root path")
  project_path = getProjectPath(history_path_global)
  print("[python] Project path: " + project_path)

  # Get rom file path without rom name
  rom_file_path = project_path + rom_file_name_with_folder.replace(rom_file_name, '')
  print("[python] rom file path: " + rom_file_path)

  # Get rom file path with rom name
  rom_file_full_path = rom_file_path + rom_file_name
  print("[python] rom file full path: " + rom_file_full_path)

  # Check rom file match History.txt
  print("Status_Anchor: Checking ROM file exists on project root path")
  check_rom_exists_status = checkRomExists(rom_file_name, rom_file_path)
  if not check_rom_exists_status:
    raise FileNotFoundError("release_exp: Please Check History \"image filename\" content matches actual file name")

  # Copy History.txt to server
  print("Status_Anchor: Copying History.txt to server")
  copyFileToServer(history_path_global, server_path_global)

  # Copy rom file to server
  print("Status_Anchor: Copying ROM file to server")
  copyFileToServer(rom_file_full_path, server_path_global)

  if ((is_email_global == 'true') or (is_clipboard_global == 'true')):
    # History Content add rom server path
    print("Status_Anchor: Adding ROM file hyperlink on history contents")
    history_content = addRomServerPath(server_path_global, rom_file_name, history_content)

    # History Content add "Dear All,"
    history_content = addDearAll(history_content)
    # print(history_content)

    # History Content add html tags
    print("Status_Anchor: Adding HTML tags on history contents")
    history_content = addHtmlTags(history_content)

    # Open Outlook
    if(is_email_global == 'true'):
      print("Status_Anchor: Opening Outlook")
      openOutlook(history_content, project_name)

    # Copy modified history content to clipboard
    if(is_clipboard_global == 'true'):
      print("Status_Anchor: Copying history contents to clipboard")
      copyToClipboard(history_content)

if __name__ == '__main__':
    main()