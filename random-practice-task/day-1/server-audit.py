import subprocess
import datetime


hostname = subprocess.run(['hostname'], capture_output=True, text=True)
current_user = subprocess.run(['whoami'], capture_output=True, text=True)
current_time = datetime.datetime.now()

disk_usage = subprocess.run(['df', '-h', '/'], capture_output=True, text=True)
disk_lines = disk_usage.stdout.splitlines()

top_five_memory_consumption_processes = subprocess.run(['ps', 'aux', '--sort=-%mem'], capture_output=True, text=True)
mem_lines = top_five_memory_consumption_processes.stdout.splitlines()

print("===============SERVER REPORT===============")
print(f"hostname: {hostname.stdout}")
print(f"current User: {current_user.stdout}")
print(f"current_time: {current_time}")
print(f"disk_usage: {disk_lines[1].split()[4]}")
print("Top 5 memory consumption processes:")
for i, line in enumerate(mem_lines[1:6], start=1):
    parts = line.split()
    process_name = parts[10]
    memory_percent = parts[3]
    memory_usage = round(int(parts[5]) / 1024, 1)

    print(f"{i} -> {process_name}: {memory_percent}% : {memory_usage}GB")
