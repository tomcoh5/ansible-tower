#!/bin/bash


yum install -y wget vim perl-libwww-perl.noarch perl-Time-HiRes
cd /usr/src/
wget https://download.configserver.com/csf.tgz
tar -xvzf csf.tgz
cd csf
bash install.sh
cd /usr/local/csf/bin/
perl csftest.pl
sleep 2
systemctl stop firewalld
systemctl disable firewalld
cd /etc/csf/
sed -r 's/TESTING = ./TESTING = 0/' csf.conf
systemctl start csf
systemctl enable lfd
echo "Adding allowed IP addresses"
csf -a 94.159.136.163
csf -a 185.18.204.68
csf -a 94.159.138.226
sleep 2
echo "Complete"
~

