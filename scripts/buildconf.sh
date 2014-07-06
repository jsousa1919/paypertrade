#!/bin/bash
PROJECT="$( cd "$( dirname "${BASH_SOURCE[0]}" )"/.. && pwd )"

echo '[DEFAULT]\n' > tmp.ini; cat $PROJECT/servedev.conf|egrep -v '\^#' >> $PROJECT/tmp.ini; cat $PROJECT/development.ini >> tmp.ini;
