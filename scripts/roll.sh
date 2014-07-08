#!/bin/bash
PROJECT="/opt/display_code"

git push
cd $PORJECT
sudo su ubuntu $PROJECT/scripts/update_base.sh
