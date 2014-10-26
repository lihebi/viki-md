# BootStrap

## Basic Template

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap 101 Template</title>

    <!-- Bootstrap -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
    <h1>Hello, world!</h1>

    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="js/bootstrap.min.js"></script>
  </body>
</html>
```

## navbar

```html
<nav class="navbar navbar-inverse" ng-controller="NavCtrl" role="navigation">
  <div class="container-fluid">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar-collapse-1">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="#" ng-click="setTab('Home')">WC</a>
    </div>

    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id="navbar-collapse-1">
      <ul class="nav navbar-nav">
        <li ng-class="{active:isSelected('Home')}" ng-click="setTab('Home')"><a ng-href="#/">Home</a></li>
        <li ng-class="{active:isSelected('Tools')}" ng-click="setTab('Tools')"><a ng-href="#/tools">Tools</a></li>
        <li ng-class="{active:isSelected('Settings')}" ng-click="setTab('Settings')"><a ng-href="#/settings">Settings</a></li>
        <li ng-class="{active:isSelected('Blog')}" ng-click="setTab('Blog')"><a ng-href="#/blog">Blog</a></li>
      </ul>
      <ul class="nav navbar-nav navbar-right">
        <li ng-show="isLoggedIn()" ng-class="{active:isSelected('Account')}" ng-click="setTab('Account')"><a ng-href="#/account">{{who().first}}</a></li>
        <li ng-show="isLoggedIn()" ng-click="logout()"><a href>Logout</a></li>
        <li ng-hide="isLoggedIn()" ng-class="{active:isSelected('Login')}" ng-click="setTab('Login')"><a href="#/login">Login</a></li>
        <li ng-hide="isLoggedIn()" ng-class="{active:isSelected('Signup')}" ng-click="setTab('Signup')"><a href="#/signup">Sign Up</a></li>
        <li class="dropdown">
          <a href class="dropdown-toggle" data-toggle="dropdown">Help <span class="caret"></span></a>
          <ul class="dropdown-menu" role="menu">
            <li><a href="#">Getting Start</a></li>
            <li><a href="#">Term of Condition</a></li>
            <li><a href="#">Feedback</a></li>
            <li class="divider"></li>
            <li><a href="#/about">About</a></li>
          </ul>
        </li>
      </ul>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>
```
