<html ng-app="PayPerTrade">
    <head>
        <title>PayPerTrade :: ${ self.title() }</title>
        <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.js"></script>
        <script src="//ajax.googleapis.com/ajax/libs/angularjs/1.2.21/angular.js"></script>
        <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.js"></script>
        <script>
            <%include file="../js/consts.js.mako" />
        </script>
        <script src="/js/angular_global.js"></script>
        <script src="/js/google.js"></script>
        <link href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.css" rel="stylesheet" />
        <link href="/css/base.css" rel="stylesheet" />
        <link href="/css/mixins.css" rel="stylesheet" />
        <link href="/css/ie.css" rel="stylesheet" />
        <link href="/css/print.css" rel="stylesheet" />
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
                <a href="/">PPT</a>
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
        <script type="text/javascript">
            (function() {
                var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true;
                po.src = 'https://apis.google.com/js/client:plusone.js';
                    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);
                }
            )();
         </script>
    </body>
</html>
<%def name="head()"></%def>
<%def name="title()"></%def>
<%def name="ready()"></%def>
<%def name="headers()"></%def>

