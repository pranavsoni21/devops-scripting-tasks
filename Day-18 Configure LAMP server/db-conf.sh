#!/bin/bash

# --------------Variables------------------
DB_SERVER="stdb01"
DB_USER="peter"
DB_PASS="Rc5C9EyvbU"
DB_NAME="kodekloud_db1"
DB_APP_USER="kodekloud_rin"
PASS="Sp!dy"
# -------------------------------------------


#-------------- Configuring DB server---------------

echo "Configuring database server. Please wait...."

# shellcheck disable=SC1009
# shellcheck disable=SC2087
ssh "$DB_USER"@"$DB_SERVER" << EOF
echo "$PASS" | sudo -S yum install -y mariadb-server
echo "$PASS" | sudo -S enable mariadb
echo "$PASS" | sudo -S start mariadb

echo "$PASS" | sudo -S mysql -e "
CREATE DATABASE IF NOT EXISTS $DB_NAME;
CREATE USER IF NOT EXISTS '$DB_APP_USER'@'%' IDENTIFIED BY '$DB_PASS';
GRANT ALL PRIVILEGES ON $DB_NAME.* TO '$DB_APP_USER'@'%';
FLUSH PRIVILEGES;
"

echo "$PASS" | sudo -S sed -i 's/^bind-address.*/bind-address=0.0.0.0/' /etc/my.cnf
echo "$PASS" | sudo -S systemctl restart mariadb
EOF

echo "[+]Successfully configured database server"