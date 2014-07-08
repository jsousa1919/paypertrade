#!/bin/bash

sudo apt-get install `cat requirements`
sudo pip install -r dev-requirements.pip
sudo su postgres <<EOF
psql -c "create database paypertrade";
psql -c "create user paypertrade with password 'paypertrade'";
psql -c "grant all on database paypertrade to paypertrade";   
EOF
cp servedev.conf.default servedev.conf
scripts/buildconf.sh
echo "export PYTHONPATH=$PYTHONPATH:`pwd`" >> ~/.bashrc
source ~/.bashrc
alembic upgrade head
scripts/servedev.sh
