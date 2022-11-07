def getHistoryContent(history_path):
  history_lines = open(history_path, 'r', encoding= 'utf8').readlines()
  history_length = len(history_lines)-1
  capture_line = ';-----------------------------------------------------------------------;'
  history_content = ''
  for i in range(history_length):
    if capture_line in history_lines[i]:
      for j in range(i, history_length):
        history_content += history_lines[j]
        if capture_line in history_lines[j+1]:
          history_content += capture_line
          history_content += '\n'
          return history_content
  return ""