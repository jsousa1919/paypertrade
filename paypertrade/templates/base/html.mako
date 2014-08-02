<html ng-app="PayPerTrade">
    <head>
        <title>PayPerTrade :: ${ self.title() }</title>
        <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.js"></script>
        <script src="//ajax.googleapis.com/ajax/libs/angularjs/1.2.21/angular.js"></script>
        <script src="https://plus.google.com/js/client:plusone.js"></script>
        <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.js"></script>
        <script>
            <%include file="../js/consts.js.mako" />
            <%include file="../js/google.js.mako" />
            <%include file="../js/angular_global.js.mako" />
        </script>
        <link href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.css" rel="stylesheet" />
        <style>
            body {
                padding-top: 2em;
            }
            #header {
                background-color: #EEFFFF;
                border-radius: 3em;
                box-shadow: 0 0 1em #DDFFFF;
                height: 3em;
                width: 100%;
            }
            #header .logo {
                font-size: 3em;
                font-weight: bold;
                line-height: 100%;
            }
            #header .headers {
                padding-top: 0.7em;
            }
            #body {
                padding: 2em;
            }
        </style>
        ${ self.head() }
        <script>
            $(document).ready(function () {
                ${ self.ready() }
            });
        </script>
    </head>
    <body ng-controller="GlobalCtrl" class="container col-md-10 col-md-offset-1">
        <div id="header" class="row-fluid">
            <span class="logo col-md-2">
                <a href="{{ urls.base_index }}">PPT</a>
            </span>
            <span class="headers col-md-8">
                <span></span>
                ${ self.headers() }
            </span>
            <span class="headers col-md-2">
                <span ng-show="logged_in">
                    <a href="{{ urls.account_home }}">{{ name || 'Home' }}</a>
                </span>
                <span ng-hide="logged_in">
                    <a href="{{ urls.account_signin }}">Sign in</a>
                </span>
            </span>
        </div>
        <div id="body" class="row-fluid">
            ${ next.body() }
        </div>
    </body>
</html>
<%def name="head()"></%def>
<%def name="title()"></%def>
<%def name="ready()"></%def>
<%def name="headers()"></%def>

