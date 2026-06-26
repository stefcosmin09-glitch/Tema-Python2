import hashlib
import shutil
import os
import sys
from datetime import datetime

file_path = sys.argv[1]
backup_dir = "backup"

if not os.path.isfile(file_path):
    print(f"File '{file_path}' does not exist.")
    sys.exit(1)

os.makedirs(backup_dir, exist_ok=True)

current_hash = hashlib.sha256(open(file_path, 'rb').read()).hexdigest()

for filename in os.listdir(backup_dir):
    backup_file_path = os.path.join(backup_dir, filename)
    backup_hash = hashlib.sha256(open(backup_file_path, 'rb').read()).hexdigest()

    if backup_hash == current_hash:
        print(f"File '{file_path}' is identical to backup '{filename}'. No backup created.")
        sys.exit(0)

timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
file_name = os.path.basename(file_path)
backup_name = os.path.join(backup_dir, f"{file_name}_{timestamp}")
shutil.copy2(file_path, backup_name)
print(f"Backup created: '{backup_name}'")