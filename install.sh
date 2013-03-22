#! /bin/bash
wget http://apt.puppetlabs.com/puppetlabs-release-quantal.deb
dpkg -i puppetlabs-release-quantal.deb
apt-get update -y
apt-get install -y build-essential python-dev python-pip facter libjson-ruby openssh-server
pip install pymongo
wget https://github.com/ajgbangug/commander-client/archive/master.zip
unzip master.zip
mkdir /opt/commander
ln -s /home/commander/commander-client-master/client.py /opt/commander/
