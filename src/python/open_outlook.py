import win32com.client as win32
from datetime import date
import global_var as glb
import project_info as _ProjectInfo

def openOutlook(html_history_content):

  obj = win32.Dispatch('outlook.application')
  mapi = obj.GetNamespace('MAPI')
  new_mail = obj.CreateItem(0)
  new_mail.GetInspector

  ProjInfo = _ProjectInfo.ProjectInfo()

  # Edit the Subject
  if(glb.get('production') == 'true'):
    new_mail.Subject = '[Verify] '+ProjInfo.projectName()+' '+ProjInfo.projectVersion()
  else:
    new_mail.Subject = '{:%Y-%b-%d} [Release] '.format(date.today()) + ProjInfo.projectName()

  # Get the Contents
  new_mail.HtmlBody = html_history_content

  # Display the email
  new_mail.Display(True)
