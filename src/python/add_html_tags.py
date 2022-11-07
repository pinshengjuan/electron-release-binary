def addHtmlTags(history_content):
  new_history_content = ''
  for line in history_content.split('\n'):
    if line.strip() == '':
      new_history_content += "<br>"
    elif '//Binary' in line:
      new_history_content = new_history_content + "<font size =3 face = 'Calibri'>"+"<a href=" + "file:///" + line + ">" + line + "</a>" + "</font>" + "<br>"
    else:
      new_history_content = new_history_content + "<font size =3 face = 'Calibri'>" + line +"</font>" + "<br>"
  return new_history_content