#!/bin/bash

PROJECT="/opt/display_code"
PYTHONPATH=$PROJECT
REPO="/opt/pptrepo"
PIDFILE="$REPO/paster.pid"

cd $REPO
git push

cd $PROJECT
git pull
source /opt/PayPerTrade/bin/activate
./scripts/buildconf.sh
alembic upgrade head
echo start
echo $PYTHONPATH
echo end
./scripts/runprod.sh restart
