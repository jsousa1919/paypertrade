paypertrade
===========

IN ORDER TO USE GOOGLE OAUTH:
    create an app in the google dev console
    get a client id for an oauth web application in this app
    make sure the callback url is attached to this id
    make sure to use https on the server
    alter the consent screen for the app to add an email address and company name
    set your machine's hosts to map paypertrade.com to your hosts address
    or just use mine with the servedev.conf.default client_id/app_host and point paypertrade.com at your webserver in your local machines hosts file


'HTTPFound' object has no attribute 'exception'
Downgrade WebOb below 1.4 to 1.3.1
