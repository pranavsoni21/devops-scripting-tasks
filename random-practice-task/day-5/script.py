total_servers = 0

healthy_servers = {}
unhealthy_servers = {}

with open('servers.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    total_servers += 1

    parts = line.strip().split(",")
    server_id = parts[0]
    status = parts[1]

    if status.lower() == "healthy":
        healthy_servers[server_id] = status
    else:
        unhealthy_servers[server_id] = status


print(f"Total Servers: {total_servers}\n")
print(f"NO. OF Healthy Servers: {len(healthy_servers)}\n")
print(f"NO. OF Unhealthy Servers: {len(unhealthy_servers)}\n")

print("UNHEALTHY SERVERS:\n")
for key, value in unhealthy_servers.items():
    print(f"{key} ")