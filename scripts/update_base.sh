#!/bin/bash

PROJECT="/opt/display_code"
REPO="/opt/pptrepo"
PIDFILE="$REPO/paster.pid"

cd $REPO
git push

cd $PROJECT
git pull
source /opt/PayPerTrade/bin/activate
alembic upgrade head
./scripts/runprod.sh restart
