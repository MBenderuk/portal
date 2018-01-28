
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="icon" href="images/favicon.ico">

    <title>Table test page</title>

    <!-- Bootstrap core CSS -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

  </head>

  <body>
    <div class="container">
      <div class="row">
           <div class="col-sm-1 pull-right">
                <a href="/logout/someuser" class="btn pull-right" role="button">Logout</a>
           </div>
           <div class="col-sm-3 pull-right">
                <h5>You are logged in as: some_user </h5>
           </div>
      </div>
      <h3>List of users:</h3>
      <table class="table table-striped">
        <thead>
           <tr>
               <th>ID</th>
               <th>Registration date</th>
               <th>Login</th>
               <th>Action</th>
           </tr>
        </thead>
      <tbody>
      %for line in table:
        <tr>
            %for col in line:
                <td>{{col}}</td>
            %end
                <td>
                     <a href="/modify/{{line[0]}}" class="btn btn-warning" role="button">Modify user</a>
                     <a href="/delete/{{line[0]}}" class="btn btn-danger" role="button">Delete user</a>
                </td>
        </tr>
      %end
      <tfoot>
           <tr>
               <td><a href="/add" class="btn btn-primary" role="button">Add user</a></td>
               <td></td>
               <td></td>
               <td></td>
           </tr>
      </tfoot>
      </tbody>
      </table>
          
          
    </div> <!-- /container -->
  </body>
</html>

