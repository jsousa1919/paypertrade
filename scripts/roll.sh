#!/bin/bash

PROJECT="/opt/display_code"

git push
sudo su ubuntu $PROJECT/scripts/update_base.sh
