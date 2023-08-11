import os

VERSION_FILE = "VERSION"

def get_version() -> str:
  filepath = os.path.join(os.path.dirname(__file__), VERSION_FILE)
  with open(filepath, 'r') as f:
    return f.readline().strip()

version = get_version()
