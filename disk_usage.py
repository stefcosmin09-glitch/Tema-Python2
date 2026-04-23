import shutil
import os

prag = int(os.environ.get("DISK_THRESHOLD", 90))
total, used, free = shutil.disk_usage("/")

procent = (used / total) * 100

if procent > prag:
    print(f"Disk usage is at {procent:.2f}%, which exceeds the threshold of {prag}%.")
else:
    print(f"Disk usage is at {procent:.2f}%, which is within the threshold of {prag}%.")
