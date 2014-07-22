#!/bin/bash
PROJECT="/opt/display_code"
export PYTHONPATH=$PROJECT
REPO="/opt/pptrepo"

sudo su ubuntu <<EOF
cd $REPO
git pull
cd $PROJECT
./scripts/update_base.sh
EOF

git pull
./scripts/buildconf.sh

