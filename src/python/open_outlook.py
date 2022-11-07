import win32com.client as win32
from datetime import date

def openOutlook(history_content, project_name):

  obj = win32.Dispatch('outlook.application')
  mapi = obj.GetNamespace('MAPI')
  newMail = obj.CreateItem(0)
  newMail.GetInspector

  # Edit the Subject
  newMail.Subject = "{:%Y-%b-%d} Binary Release: ".format(date.today()) + project_name

  # Get the Contents
  newMail.HtmlBody = history_content

  # Display the email
  newMail.Display(True)
