#!/bin/bash

PROJECT="/opt/display_code"
export PYTHONPATH=$PROJECT
REPO="/opt/pptrepo"
source ~/.bashrc

cd $REPO
git push

cd $PROJECT
git pull
source /opt/PayPerTrade/bin/activate
./scripts/buildconf.sh
alembic upgrade head
./scripts/runprod.sh restart
