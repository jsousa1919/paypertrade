#!/bin/bash
PROJECT="/opt/display_code"

git push
cd $PROJECT
sudo su ubuntu $PROJECT/scripts/update_base.sh
