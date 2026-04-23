import os
import shutil
import time
import random
import sys

source_dir = sys.argv[1]
destination_dir = sys.argv[2]

os.makedirs(destination_dir, exist_ok=True)

for filename in os.listdir(source_dir):
    src_path = os.path.join(source_dir, filename)
    lock_path = src_path + ".lock"
    dst_path = os.path.join(destination_dir, filename)
    try:
        os.rename(src_path, lock_path)
    except:
        continue


shutil.move(lock_path, dst_path)
print(f"Moved '{filename}'")
time.sleep(random.randint(1, 5))
