#!/bin/sh
# This is the nemomobile post install script for PinePhone devices!
while true
do
    if id -u "manjaro" >/dev/null 2>&1; then
	gpasswd -a "manjaro" autologin
	break
    else
	sleep 1
    fi
done

chown -R manjaro.users /home/manjaro/

# Disable this service, so it only gets run on first boot
systemctl disable nemomobile-post-install.service

# reboot phone
reboot
