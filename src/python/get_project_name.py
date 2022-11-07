def getProjectName(history_content):
  for line in history_content.split('\n'):
    if 'Project Name' in line:
      return line.split(":")[1].strip()
  return ""