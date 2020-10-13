#!/bin/bash

f_run_install(){
#csf -a 185.37.148.66
#csf -a 94.159.138.226
cd /root/
wget https://github.com/NagiosEnterprises/nrpe/releases/download/nrpe-3.2.1/nrpe-3.2.1.tar.gz
tar -xvzf nrpe-3.2.1.tar.gz
cd nrpe-3.2.1/
useradd nagios
./configure
make all && make install
wget https://nagios-plugins.org/download/nagios-plugins-2.2.1.tar.gz
tar -xvzf nagios-plugins-2.2.1.tar.gz
cd nagios-plugins-2.2.1/
./configure
make && make install
cd /root/nrpe-3.2.1/
chown nagios. /usr/local/nagios
make install-config
if [ -f /usr/local/nagios/etc/nrpe.cfg ]; then
 ln -s /usr/local/nagios/etc/nrpe.cfg /etc/nrpe.cfg
fi

yum install -y xinetd
rm /etc/xinetd.d/*
make install-inetd && ldconfig

wget interhost.co.il/nrpe -P /home/ && mv /home/nrpe /etc/xinetd.d/
wget interhost.co.il/nrpe.cfg /home && mv -f /home/nrpe.cfg /etc/
echo "nrpe            5666/tcp                # NRPE" >> /etc/services
systemctl enable --now xinetd
systemctl status xinetd
if [ $# = 1 ]; then
echo "service didnt start" && exit
fi

echo "**** Installation complete ****"
service nrpe restart
service xinetd restart
}

f_run_install # > /var/log/install_log.log


