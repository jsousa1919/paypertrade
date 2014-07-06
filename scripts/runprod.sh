#!/bin/bash

PROJECT="/opt/display_code"
REPO="/opt/pptrepo"
PIDFILE="$REPO/paster.pid"
LOGFILE="var/log/paypertrade/out.log"
CONFIG="$PROJECT/development.ini"

source /lib/lsb/init-functions

usage() {
    cat << EOF
    Usage: $0 {start|stop|restart} [options]

    Manage paster daemon and associated processes

    OPTIONS:
    -h      Show this message
    -p      Project root folder
    -c      Config file
    -l      Log file
EOF
}

start() {
    paster serve --daemon --pid-file=$PIDFILE --log-file=$LOG $CONFIG start
}

stop() {
    paster serve --stop-daemon --pid-file=$PIDFILE --log-file=$LOG $CONFIG stop
}

status() {
    status_of_proc -p $PIDFILE "paster" paster && exit 0 || exit $?
    status=$?

    if [ $status -eq 0 ]; then
        log_success_msg "paster is running"
    else
        log_failure_msg "paster is not running"
    fi
    exit $status
}

while getopts "h?c:l:p:" OPTION
do
    case $OPTION in
        h)
            usage
            exit 1
            ;;
        c)
            CONFIG=$OPTARG
            ;;
        l)
            LOG=$OPTARG
            ;;
        p)
            PROJECT=$OPTARG
            ;;
        ?)
            usage
            exit 1
            ;;
    esac
done
                                   

cd $PROJECT
case "$1" in
    start)
        start
        exit 1
    ;;
    stop)
        stop
        exit 1
    ;;
    restart)
        stop
        sleep 2
        start
        exit 1
    ;;
    status)
        status
    ;;
    *)
        usage
        exit 1
esac
