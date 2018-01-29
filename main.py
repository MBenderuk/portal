#!/usr/bin/python
import bottle, mysql.connector, uuid
bottle.TEMPLATES.clear()

app = bottle.app()

### Routes --- BEGIN ###
@app.route('/')
def login():
    return bottle.template('login.tpl')

@app.route('/', method="POST")
def login_handler():
    login = bottle.request.forms.get('login')
    password = bottle.request.forms.get('password')
   
    if login_validation(login, password) is True:
	return bottle.redirect('/table')
    else:
        return bottle.template('bad-credentials.tpl')

@app.route('/table')
def table():
    connection, cursor = connect_to_mysql()
    select_query = ("SELECT no, reg_date, login FROM users")
    cursor.execute(select_query)
    table_content=cursor.fetchall()
    cursor.close()
    connection.close()
    return bottle.template('table.tpl', table=table_content)

@app.route('/add')
def add_new_user_form():
    return bottle.template('add-user.tpl')

@app.route('/add', method="POST")
def add_new_user():
    new_user_login = bottle.request.forms.get('new-user-login')
    new_user_password = bottle.request.forms.get('new-user-password')
    
    add_new_user(new_user_login, new_user_password)
    
    return bottle.template('user-successfully-added.tpl')

@app.route('/delete/<user_id:int>')
def delete_user(user_id):
    connection, cursor = connect_to_mysql()
    delete_query=("DELETE FROM users WHERE no = \"%s\"" % user_id)
    cursor.execute(delete_query)
    connection.commit()
    cursor.close()
    connection.close()
    return bottle.redirect('/table')

@app.route('/modify/<user_id:int>')
@app.route('/modify/<user_id:int>', method="POST")
def modify_user_form(user_id):
    connection, cursor = connect_to_mysql()
    if  bottle.request.method == "POST":
        print(user_id)
        modified_user_login = bottle.request.forms.get('user-login')
        print(modified_user_login)
        modified_user_password = bottle.request.forms.get('user-password')
        print(modified_user_password)
        modify_login_query = ("UPDATE users SET login=\"%s\" WHERE no=\"%s\"" % (modified_user_login, user_id))
        cursor.execute(modify_login_query)
        connection.commit()
        modify_password_query = ("UPDATE users SET password=\"%s\" WHERE no=\"%s\"" % (modified_user_password, user_id))
        cursor.execute(modify_password_query)
        connection.commit()
        cursor.close()
        connection.close()
        return bottle.redirect('/table')
    else:
        select_login_guery = ("SELECT login FROM users WHERE no=\"%s\"" % user_id)
        cursor.execute(select_login_guery)
        for row in cursor:
            select_login_guery_result=row[0]
        select_password_guery = ("SELECT password FROM users WHERE no=\"%s\"" % user_id)
        cursor.execute(select_password_guery)
        for row in cursor:
            select_password_guery_result=row[0]
        cursor.close()
        connection.close()
        return bottle.template('modify-user.tpl', user_id=user_id, user_login=select_login_guery_result, user_password=select_password_guery_result)

### Routes --- END ###

### Custom functions --- BEGIN ###

def add_new_user(new_user_login, new_user_password):
    connection, cursor = connect_to_mysql()
    new_user_credentials=(new_user_login, new_user_password)
    insert_query=("INSERT INTO users (reg_date, login, password) "
                  "VALUES (now(), \"%s\", \"%s\")" % new_user_credentials)
    cursor.execute(insert_query)
    connection.commit()
    cursor.close()
    connection.close()

def login_validation(login, password):
    select_login_guery_result=0
    select_password_guery_result=0
    connection, cursor = connect_to_mysql()
    select_login_guery = ("SELECT login FROM users WHERE login=\"%s\"" % login)
    cursor.execute(select_login_guery)
    for row in cursor:
        select_login_guery_result=row[0]
    select_password_guery = ("SELECT password FROM users WHERE password=\"%s\"" % password)
    cursor.execute(select_password_guery)
    for row in cursor:
        select_password_guery_result=row[0]
    if (select_login_guery_result == login) and \
       (select_password_guery_result == password):
        return (True)
    else:
        return (False)
    cursor.close()
    connection.close()

def create_session(user_id):
    connection, cursor = connect_to_mysql()
    session_key = str(uuid.uuid4())
    cursor.execute("INSERT INTO sessions (user_id, session_key) VALUES (\"%s\", \"%s\")" % user_id, session_key))
    connection.commit()
    cursor.close()
    connection.close()
    return session_key

### Custom functions --- END ###

### Connect to MySQL --- BEGIN ###
def connect_to_mysql():
    try:
        connection = mysql.connector.connect(user='portal',
                                    password='portal-secure-pass',
                                    host='10.62.10.196',
                                    port=3306,
                                    database='portaldb')
        cursor = connection.cursor()
    except mysql.connector.Error as err:
        if err:
            print(err)
    return connection, cursor
### Connect to MySQL --- END ###

### Handle static --- BEGIN ###
@app.get("/css/<filepath:re:.*\.css>")
def css(filepath):
    return bottle.static_file(filepath, root="css")

@app.get("/fonts/<filepath:re:.*\.(eot|otf|svg|ttf|woff|woff2?)>")
def font(filepath):
    return bottle.static_file(filepath, root="font")

@app.get("/images/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def images(filepath):
    return bottle.static_file(filepath, root="images")

@app.get("/js/<filepath:re:.*\.js>")
def js(filepath):
    return bottle.static_file(filepath, root="js")
### Handle static --- END ###

### Start the Bottle webapp ###
def main():
    
    bottle.debug(True)
    bottle.run(app=app, host='0.0.0.0', port=8080, reloader=True)

if __name__ == "__main__":
    main()
