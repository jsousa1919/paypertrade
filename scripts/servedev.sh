#!/bin/bash
PROJECT="$( cd "$( dirname "${BASH_SOURCE[0]}" )"/.. && pwd )"

source $PROJECT/scripts/buildconf.sh
paster serve --reload tmp.ini
