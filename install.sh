#!/usr/bin/env bash

echo "***************** install *********************"

echo "---apt update e upgrade---"

apt-get -y update

echo "---OS dependencies---"

apt-get -y install python3-pip
apt-get -y install python3-dev python3-setuptools
apt-get -y install git
apt-get -y install supervisor
# .....
# .....
# .....
# .....

echo "---install dependencies (including django)  ---"

pip install --upgrade pip
pip install -r requirements.txt

echo "--- Sone Installing Stuff                   ---"

pip freeze