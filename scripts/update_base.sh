#!/bin/bash

PROJECT="/opt/display_code"
REPO="/opt/pptrepo"
PIDFILE="$REPO/paster.pid"

cd $REPO
git push

cd $PROJECT
git pull
./scripts/runprod.sh restart
