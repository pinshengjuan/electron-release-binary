import os
import re
import zipfile
import global_var as glb
import project_info as _ProjectInfo

#Consider below struct as example
#  //${Server_Path}/MyAwesomeProject
#  |___MyAwesomeProject_1.0.0.ROM
#  |
#  |___Production
#      |___1.0.0
#          |___MyAwesomeProject(1.0.0)ROM.zip
#          |___MyAwesomeProject_1.0.0.ROM
#          |___Checksum.txt

class ProductionBinary:
  def productionPath(self): #//${Server_Path}/MyAwesomeProject/Production/
    return glb.get('server_path') + 'Production/'

  def productionPathWithVer(self): #//${Server_Path}/MyAwesomeProject/Production/1.0.0/
    ProjInfo = _ProjectInfo.ProjectInfo()
    return self.productionPath()+ProjInfo.projectVersion() + '/'

  def packName(self): #MyAwesomeProject(1.0.0)ROM.zip
    ProjInfo = _ProjectInfo.ProjectInfo()
    #modify project name with "\" and "/" to "_" using RegEx
    modfied_project_name = re.sub(r"[\\\/]", "_", ProjInfo.projectName())
    return modfied_project_name+'('+ProjInfo.projectVersion()+')'+'ROM.zip'

  def checkProductionFolder(self): #Check Production folder exist, if not, make one
    if not os.path.isdir(self.productionPath()):
      os.mkdir(self.productionPath())

  def checkVersionFolder(self): #Check Production/1.0.0 folder exist, if not, make one
    if not os.path.isdir(self.productionPathWithVer()):
      os.mkdir(self.productionPathWithVer())

  def calcRomChecksum(self):
    ProjInfo = _ProjectInfo.ProjectInfo()
    f = open(ProjInfo.romFullPath(), 'rb').read()
    num_checksum = sum(f)&0xffff
    str_checksum = '0x%X' %num_checksum
    return str_checksum

  def makeRomChecksumFile(self): #Checksum.txt
    str_checksum = 'Checksum-16: ' + self.calcRomChecksum()
    checksum_file = self.productionPathWithVer()+'Checksum.txt'
    open(checksum_file,'w+',encoding = 'utf8').writelines(str_checksum)

  def packRom(self): #MyAwesomeProject(1.0.0)ROM.zip
    ProjInfo = _ProjectInfo.ProjectInfo()
    location = self.productionPathWithVer()+self.packName()
    zf = zipfile.ZipFile(location, 'w', zipfile.ZIP_DEFLATED)
    zf.write(ProjInfo.romFullPath(), ProjInfo.romFullPath().replace(ProjInfo.romFolderPath(), ''))
    zf.close()
