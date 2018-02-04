
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="images/favicon.ico">
    
    <title>Add userPage</title>

    <!-- Bootstrap core CSS -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

  </head>

  <body>

    <div class="container">
      <h2>Enter user data:</h2>
      <form class="form-horizontal" method="post" action="/add">
        <div class="form-group">
           <label for="inputlogin" class="control-label col-sm-2">Login:</label>
           <div class="col-sm-10">
              <input name="new-user-login" type="text" id="inputlogin" class="form-control" placeholder="Enter user login for new user here" required autofocus>
           </div>
        </div>
        <div class="form-group">   
           <label for="inputPassword" class="control-label col-sm-2">Password:</label>
           <div class="col-sm-10">
              <input name="new-user-password" type="text" id="inputPassword" class="form-control" placeholder="Enter password for new user here" required>
           </div>
        </div>
        <div class="form-group">        
            <div class="col-sm-offset-2 col-sm-10">
                <div class="checkbox">
                    <label><input name="new-user-is-admin" type="checkbox" >Admin privileges</label>
                </div>
            </div>
        </div>
      </div>
    </div>
        <div class="form-group">
           <div class="col-sm-offset-2 col-sm-10">
              <button class="btn btn-default" type="submit">Submit</button>
           </div>
        </div>
      </form>
    </div> <!-- /container -->


  </body>
</html>
