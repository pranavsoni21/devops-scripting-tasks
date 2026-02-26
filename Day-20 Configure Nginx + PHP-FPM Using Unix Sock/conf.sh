#!/bin/bash

# Variables
APP_SERVER=$1
USER=$2
PASS=$3


# Configuring server
echo "Configuring $APP_SERVER. Please wait...."

# shellcheck disable=SC2087
ssh "$USER"@"$APP_SERVER" <<EOF

echo "$PASS" | sudo -S yum install -y nginx
echo "$PASS" | sudo -S yum install php php-fpm -y

echo "$PASS" | sudo -S sed -i 's|^listen = .*|listen = /var/run/php-fpm/default.sock|' /etc/php-fpm.d/www.conf
echo "$PASS" | sudo -S sed -i 's|^listen.owner.*|listen.owner = nginx|' /etc/php-fpm.d/www.conf
echo "$PASS" | sudo -S sed -i 's|^listen.group.*|listen.group = nginx|' /etc/php-fpm.d/www.conf

echo "$PASS" | sudo -S mkdir -p /var/run/php-fpm
echo "$PASS" | sudo -S chown nginx:nginx /var/run/php-fpm

echo "$PASS" | sudo -S systemctl start php-fpm
echo "$PASS" | sudo -S systemctl enable php-fpm

echo "$PASS" | sudo -S tee /etc/nginx/conf.d/php_app.conf > /dev/null  <<TEXT
server {
    listen 8096;
    server_name localhost;

    root /var/www/html;
    index index.php index.html;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location ~ \.php$ {
        include fastcgi_params;
        fastcgi_pass unix:/var/run/php-fpm/default.sock;
        fastcgi_index index.php;
        fastcgi_param SCRIPT_FILENAME \$document_root\$fastcgi_script_name;
    }
}
TEXT

echo "$PASS" | sudo -S systemctl start nginx
echo "$PASS" | sudo -S systemctl enable nginx

EOF

echo "[+] Configuration of $APP_SERVER is successfully completed."
