#!/bin/sh
# This is the nemomobile post install script for PinePhone devices!
gpasswd -a "manjaro" autologin

# Disable this service, so it only gets run on first boot
systemctl disable nemomobile-post-install.service

# Start lightdm
systemctl restart lightdm