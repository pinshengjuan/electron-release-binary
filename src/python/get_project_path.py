def getProjectPath(history_path):
  history_name = history_path.split("/")[-1]
  project_path = history_path.replace(history_name, "")
  return project_path