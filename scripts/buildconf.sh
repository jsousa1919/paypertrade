#!/bin/bash

if [ ! -e servedev.conf ]; then
    echo "=== FIRST RUN ==="
    echo "================="
    echo "Setting up your servedev.conf..."
    cp servedev.default.conf servedev.conf
    echo "done."
    echo ""
    echo "Please edit servedev.conf with the proper values for each variable, then run this command again."
    echo ""
    echo "================="
    exit 1
fi

export PYTHONPATH=..:$PYTHONPATH
echo '[DEFAULT]\n' > tmp.ini; cat servedev.conf|egrep -v '\^#' >> tmp.ini; cat development.ini >> tmp.ini;
