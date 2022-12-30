import sys
import global_var           as glb
import get_history_content  as historyContent
import project_info         as _ProjectInfo
import handle_html_tag      as _HtmlTag
import production           as _Production
from check_rom_exists       import checkRomExists
from copy_file_to_server    import copyFileToServer
from open_outlook           import openOutlook
from copy_to_clipboard      import copyToClipboard

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

  glb._init()

  history_path_arg = sys.argv[1].replace('\\', '/')
  if(history_path_arg == ''):
    raise FileNotFoundError('release_exp: No History.txt input')
  glb.set('history_path', history_path_arg)

  server_path_arg = sys.argv[2].replace('\\', '/').replace('\\\\', '//')
  if(server_path_arg == '' or server_path_arg == '/'):
    raise FileNotFoundError('release_exp: No server location input')
  glb.set('server_path', server_path_arg)

  is_email_arg = sys.argv[3]
  is_clipboard_arg = sys.argv[4]
  is_production_arg = sys.argv[5]
  glb.set('production', is_production_arg)

  # Get history Content
  print('Status_Anchor: Reading history contents')
  historyContent.setContentToGlobal()
  # print(history_content)

  ProjInfo = _ProjectInfo.ProjectInfo()

  # Get rom file path with rom name
  rom_file_full_path = ProjInfo.romFullPath()
  print('[python] rom file full path: ' + rom_file_full_path)

  # Check rom file match History.txt
  print('Status_Anchor: Checking ROM file exists on project root path')
  check_rom_exists_status = checkRomExists()
  if not check_rom_exists_status:
    raise FileNotFoundError('release_exp: Please Check History \'image filename\' content matches actual file name')

  # Copy History.txt to server
  print('Status_Anchor: Copying History.txt to server')
  copyFileToServer(history_path_arg, server_path_arg)

  # Copy rom file to server
  print('Status_Anchor: Copying ROM file to server')
  copyFileToServer(rom_file_full_path, server_path_arg)

  if ((is_email_arg == 'true') or (is_clipboard_arg == 'true') or (is_production_arg == 'true')):

    # Check if Production
    if(is_production_arg == 'true'):
      Production = _Production.ProductionBinary()
      # Check Production folder exist, if not, make one
      Production.checkProductionFolder()
      # Check Production/${VERSION} folder exist, if not, make one
      Production.checkVersionFolder()

      # Copy rom file to Production folder
      print('Status_Anchor: Copying ROM file to Production folder')
      copyFileToServer(rom_file_full_path, Production.productionPathWithVer())

      # Calculate rom checksum and make Checksum.txt file that checksum value inside
      print('Status_Anchor: Making Checksum file')
      Production.makeRomChecksumFile()

      # Pack rom file .zip
      print('Status_Anchor: Packing ROM in Production folder')
      Production.packRom()

    HtmlTag = _HtmlTag.HandleHtml()

    mail_body = HtmlTag.addTags()

    # Copy modified history content to clipboard
    if(is_clipboard_arg == 'true'):
      print('Status_Anchor: Copying history contents to clipboard')
      copyToClipboard(mail_body)

    # Open Outlook
    if(is_email_arg == 'true'):
      print('Status_Anchor: Opening Outlook')
      openOutlook(mail_body)

if __name__ == '__main__':
  main()