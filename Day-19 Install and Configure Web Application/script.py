import paramiko

# Server configuration
app_servers = [
    {"host": "stapp01", "username": "tony", "password": "<pass>"},
    {"host": "stapp02", "username": "steve", "password": "<pass>"},
    {"host": "stapp03", "username": "banner", "password": "<pass>"}
]


def run_commands(srvr, commands):
    print(f"Connecting to {srvr['host']}")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(
        srvr["host"],
        username=srvr["username"],
        password=srvr["password"])

    for command in commands:
        print(f"Executing command: {command}")
        stdin, stdout, stderr = ssh.exec_command(command)
        print(stdout.read().decode("utf-8"))
        print(stderr.read().decode("utf-8"))

    ssh.close()
    print(f"Finished with {srvr['host']}")


# App server commands
app_commands = [
    "sudo yum install -y httpd",
    "sudo systemctl enable httpd",
    "sudo -S sed -i 's/^Listen 80/Listen 5002/' /etc/httpd/conf/httpd.conf",
    "sudo -S systemctl start httpd",
    "sudo -S mv /tmp/media /var/www/html/media",
    "sudo -S mv /tmp/apps /var/www/html/apps",
    "sudo -S chown -R apache:apache /var/www/html/media",
    "sudo -S chown -R apache:apache /var/www/html/apps",
    "sudo -S systemctl restart httpd"
]

# Execution
for server in app_servers:
    if server["host"] == "stapp03":
        run_commands(server, app_commands)
    else:
        continue
    
print("[+] Configuration Successful.")
