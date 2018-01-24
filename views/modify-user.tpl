
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="../images/favicon.ico">
    
    <title>Add userPage</title>

    <!-- Bootstrap core CSS -->
    <link href="../css/bootstrap.min.css" rel="stylesheet">

  </head>

  <body>

    <div class="container">
      <h2>Modify user data:</h2>
      <form class="form-horizontal" method="post" action="/modify/{{user_id}}">
        <div class="form-group">
           <label for="inputlogin" class="control-label col-sm-2">Login:</label>
           <div class="col-sm-10">
              <input name="user-login" type="text" id="inputlogin" class="form-control" value={{user_login}} required>
           </div>
        </div>
        <div class="form-group">   
           <label for="inputPassword" class="control-label col-sm-2">Password:</label>
           <div class="col-sm-10">
              <input name="user-password" type="text" id="inputPassword" class="form-control" value={{user_password}} required>
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
