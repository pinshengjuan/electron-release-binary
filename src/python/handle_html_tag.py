import global_var as glb
import project_info as _ProjectInfo

class HandleHtml:
  def addTags(self):
    history_content = glb.get('history_content')
    mail_body = self.handleDearAll() + self.handleFileHyperlink() + self.handleContent(history_content)
    return mail_body

  def handleDearAll(self):
    dear_all = "<font size =3 face = 'Consolas'>" + "Dear All,\n\n" + "</font>" + "<br><br>"
    return dear_all

  def handleFileHyperlink(self):
    ProjInfo = _ProjectInfo.ProjectInfo()
    if(glb.get('production') == 'true'):
      link = glb.get('server_path')+'Production/'+ProjInfo.projectVersion()+'\n'
    else:
      link = glb.get('server_path')+ProjInfo.romFileWithoutFolder()+'\n'
    file_hyper_link = "<font size =3 face = 'Consolas'>"+"<a href=" + "file:///" + link.replace('/', '\\').replace(' ', '%20') + ">" + link.replace('/', '\\') + "</a>" + "</font>" + "<br><br>"
    return file_hyper_link

  def handleContent(self, history_content):
    new_history_content = ''
    for line in history_content.split('\n'):
      if line.strip() == '':
        new_history_content += "<br>"
      else:
        new_history_content += "<font size =3 face = 'Consolas'>" + line + "</font>" + "<br>"
    return new_history_content