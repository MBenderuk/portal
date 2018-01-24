
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="images/favicon.ico">
    
    <title>Signin Test Page</title>

    <!-- Bootstrap core CSS -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

  </head>

  <body>

    <div class="container">

      <form class="form-signin" method="post" action="/">
           <h2 class="form-signin-heading">Please sign in</h2>
           <label for="inputlogin" class="sr-only">Login</label>
           <input name="login" type="text" id="inputlogin" class="form-control" placeholder="Type your Login here" required autofocus>
           <label for="inputPassword" class="sr-only">Password</label>
           <input name="password" type="password" id="inputPassword" class="form-control" placeholder="Type your Password here" required>
           <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
      </form>

    </div> <!-- /container -->


  </body>
</html>
