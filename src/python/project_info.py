import global_var as glb

#Consider below struct as example
#  D:\
#  |___ForWork
#      |___MyAwesomeProject
#          |___100
#              |___ROM
#              |   |___MyAwesomeProject_1.0.0.ROM
#              |
#              |___History.txt

# Here we get 
#  1. Project name, base on history content, which is MyAwesomeProject
#  2. Project path, which is D:\ForWork\MyAwesomeProject\100\
#  3. Project version, which is 1.0.0
#  4. ROM name, which is MyAwesomeProject_1.0.0.ROM
#  5. ROM path, which is D:\ForWork\MyAwesomeProject\100\ROM\
#  6. ROM path with ROM name, which is D:\ForWork\MyAwesomeProject\100\ROM\MyAwesomeProject_1.0.0.ROM

class ProjectInfo:
  def projectName(self): #MyAwesomeProject
    for line in glb.get('history_content').split('\n'):
      if 'Project Name' in line:
        return line.split(':')[1].strip()
    return ''

  def projectPath(self): #D:\ForWork\MyAwesomeProject\100\
    history_name = glb.get('history_path').split('/')[-1]
    project_path = glb.get('history_path').replace(history_name, '')
    return project_path

  def projectVersion(self): #1.0.0
    for line in glb.get('history_content').split('\n'):
      if 'Project Version' in line:
        return line.split(':')[1].strip()
    return ''

  def romFileWithFolder(self): #ROM\MyAwesomeProject_1.0.0.ROM
    for line in glb.get('history_content').split('\n'):
      if 'image filename' in line:
        return line.split(':')[1].strip().replace('\\', '/')
    return ''

  def romFileWithoutFolder(self): #MyAwesomeProject_1.0.0.ROM
    return self.romFileWithFolder().split('/')[-1]

  def romFolderPath(self): #D:\ForWork\MyAwesomeProject\100\ROM\
    project_path = self.projectPath()
    rom_file_with_folder = self.romFileWithFolder()
    return project_path+rom_file_with_folder.replace(self.romFileWithoutFolder(), '')

  def romFullPath(self): #D:\ForWork\MyAwesomeProject\100\ROM\MyAwesomeProject_1.0.0.ROM
    return self.romFolderPath() + self.romFileWithoutFolder()