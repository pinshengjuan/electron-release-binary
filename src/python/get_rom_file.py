def getRomFile(history_content):
  for line in history_content.split('\n'):
    if 'image filename' in line:
      return line.split(":")[1].strip()
  return ""