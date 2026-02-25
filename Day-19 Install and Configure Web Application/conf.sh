#!/bin/bash

# -----------------Variables---------------------

APP_SERVER=$1
USER=$2
PASS=$3

# ------------------------------------------------

# ----------------Moving files from jump host to app server----------------------

scp -r /home/thor/apps "$USER"@"$APP_SERVER":/tmp/
scp -r /home/thor/media "$USER"@"$APP_SERVER":/tmp/

# ----------------Configuring server---------------
echo "Configuring $APP_SERVER. Please wait....."
ssh "$USER"@"$APP_SERVER" >> EOF

echo "$PASS" | sudo -S yum install -y httpd
echo "$PASS" | sudo -S systemctl enable httpd

echo "$PASS" | sudo -S sed -i 's/^Listen 80/Listen 5002/' /etc/httpd/conf/httpd.conf
echo "$PASS" | sudo -S systemctl start httpd

echo "$PASS" | sudo -S mv /tmp/media /var/www/html/media
echo "$PASS" | sudo -S mv /tmp/apps /var/www/html/apps

echo "$PASS" | sudo -S chown -R apache:apache /var/www/html/media
echo "$PASS" | sudo -S chown -R apache:apache /var/www/html/apps
echo "$PASS" | sudo -S systemctl restart httpd

EOF

echo "[+] $APP_SERVER setup is done."