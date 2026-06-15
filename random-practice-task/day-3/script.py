import subprocess
import datetime

hostname = subprocess.run(["hostname"], capture_output=True, text=True)
current_user = subprocess.run(["whoami"], capture_output=True, text=True)
current_time = datetime.datetime.now()

disk_usage = subprocess.run(["df", "-h", "/"], capture_output=True, text=True)
disk_lines = disk_usage.stdout.splitlines()
exceed_disk_usage = bool
disk_percent = int(disk_lines[1].split()[4].strip("%"))
if disk_percent > 80:
    exceed_disk_usage = True

memory_usage = subprocess.run(["free", "-h"], capture_output=True, text=True)
memory_lines = memory_usage.stdout.splitlines()

with open("server_report.txt", "w") as file:
    file.write(f"=============SERVER REPORT===========\n"
               f"Current user: {current_user.stdout}\n"
               f"Hostname: {hostname.stdout}\n"
               f"current time: {current_time}\n\n"
               f"Disk usage: {disk_lines[1].split()[4]}\n\n"
               f"Memory usage: {memory_lines[1].split()[2]}/{memory_lines[1].split()[1]}\n")

if exceed_disk_usage:
    with open("server_report.txt", "a") as file:
        file.write("\nWARNING: DISK SPACE CRITICAL\n")