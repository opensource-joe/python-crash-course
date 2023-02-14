from pathlib import Path
import json

path = Path('ch10-files/username.json')
contents = path.read_text()
username = json.loads(contents)

print(f"Welcome back, {username}!")