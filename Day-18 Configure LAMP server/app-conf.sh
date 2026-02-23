#!/bin/bash

# ------------------Variables-----------------

APP_SERVER=$1
USER=$2
PASS=$3

# ----------------------------------------------


# -------------Configuring app server-----------

echo "Configuring $APP_SERVER server. Please wait......"

ssh "$USER"@"$APP_SERVER" >> EOF

echo "$PASS" | sudo -S yum install -y httpd php php-mysqlnd php-gd php-xml php-mbstring
echo "$PASS" | sudo -S sed -i 's/^Listen 80/Listen 8083/' /etc/httpd/conf/httpd.conf
echo "$PASS" | sudo -S systemctl start httpd
echo "$PASS" | sudo -S systemctl enable httpd

EOF

echo "Successfully configured $APP_SERVER server"