#!/usr/bin/python
import bottle, mysql.connector, uuid
bottle.TEMPLATES.clear()

app = bottle.app()
cookie_name="session_id"
user_login=""

### Routes --- BEGIN ###
@app.route('/')
def login():
    offered_session_key=bottle.request.get_cookie(cookie_name)
    if check_session(offered_session_key) is True:
        return bottle.redirect('/table')
    else:
        return bottle.template('login.tpl')

@app.route('/', method="POST")
def login_handler():
    login = bottle.request.forms.get('login')
    password = bottle.request.forms.get('password')
       
    if login_validation(login, password) is True:
        global user_login
        user_login=login
        connection, cursor = connect_to_mysql()
        cursor.execute("SELECT no FROM users WHERE login=\"%s\"" % login)
        for row in cursor:
            select_user_id_result=row[0]
        cursor.close()
        connection.close()
        bottle.response.set_cookie(cookie_name, create_session(select_user_id_result), max_age=366666600)
	return bottle.redirect('/table')
    else:
        return bottle.template('bad-credentials.tpl')

@app.route('/table')
def table():
    offered_session_key=bottle.request.get_cookie(cookie_name)
    if check_session(offered_session_key) is True:
        global user_login
        login=user_login
        connection, cursor = connect_to_mysql()
        cursor.execute("SELECT no FROM users WHERE login=\"%s\"" % login)
        user_id=cursor.fetchone()
        cursor.execute("SELECT is_admin FROM users WHERE login=\"%s\"" % login)
        admin=cursor.fetchone()
        cursor.execute("SELECT no, reg_date, login FROM users")
        table_content=cursor.fetchall()
        cursor.close()
        connection.close()
        return bottle.template('table.tpl', user_name=login, user_id=user_id[0], table=table_content, is_admin=admin[0])
    else:
        return bottle.template('login-required.tpl')

@app.route('/add')
def add_new_user_form():
    offered_session_key=bottle.request.get_cookie(cookie_name)
    if check_session(offered_session_key) is True:
        return bottle.template('add-user.tpl')
    else:
        return bottle.template('login-required.tpl')

@app.route('/add', method="POST")
def add_new_user():
    offered_session_key=bottle.request.get_cookie(cookie_name)
    if check_session(offered_session_key) is True:
        new_user_login = bottle.request.forms.get('new-user-login')
        new_user_password = bottle.request.forms.get('new-user-password')
        if bottle.request.forms.get('new-user-is-admin') == 'on':
            new_user_is_admin = 1
        else: new_user_is_admin = 0
        add_new_user(new_user_login, new_user_password, new_user_is_admin)
        return bottle.template('user-successfully-added.tpl')
    else:
        return bottle.template('login-required.tpl')

@app.route('/delete/<user_id:int>')
def delete_user(user_id):
    offered_session_key=bottle.request.get_cookie(cookie_name)
    if check_session(offered_session_key) is True:
        connection, cursor = connect_to_mysql()
        cursor.execute("DELETE FROM users WHERE no = \"%s\"" % user_id)
        connection.commit()
        cursor.close()
        connection.close()
        return bottle.redirect('/table')
    else:
        return bottle.template('login-required.tpl')

@app.route('/modify/<user_id:int>')
@app.route('/modify/<user_id:int>', method="POST")
def modify_user_form(user_id):
    offered_session_key=bottle.request.get_cookie(cookie_name)
    if check_session(offered_session_key) is True:
        connection, cursor = connect_to_mysql()
        cursor.execute("SELECT is_admin FROM users WHERE no=\"%s\"" % user_id)
        admin=cursor.fetchone()
        if  bottle.request.method == "POST":
            modified_user_login = bottle.request.forms.get('user-login')
            modified_user_password = bottle.request.forms.get('user-password')
            if bottle.request.forms.get('user-is-admin') == 'on':
                modified_is_admin = 1
            else: modified_is_admin = 0
            cursor.execute("UPDATE users SET login=\"%s\", password=\"%s\", is_admin=\"%s\" WHERE no=\"%s\"" % (modified_user_login, modified_user_password, modified_is_admin, user_id))
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
            return bottle.template('modify-user.tpl', user_id=user_id, user_login=select_login_guery_result, user_password=select_password_guery_result, is_admin=admin[0])
    else:
        return bottle.template('login-required.tpl')

@app.route('/logout/<user_id:int>')
def logout_user(user_id):
    offered_session_key=bottle.request.get_cookie(cookie_name)
    if check_session(offered_session_key) is True:
        connection, cursor = connect_to_mysql()
        cursor.execute("DELETE FROM sessions WHERE user_id = \"%s\"" % user_id)
        connection.commit()
        cursor.close()
        connection.close()
        return bottle.redirect('/')
    else:
        return bottle.template('login-required.tpl')

### Routes --- END ###

### Custom functions --- BEGIN ###

def add_new_user(new_user_login, new_user_password, new_user_is_admin):
    connection, cursor = connect_to_mysql()
    new_user_credentials=(new_user_login, new_user_password, new_user_is_admin)
    insert_query=("INSERT INTO users (reg_date, login, password, is_admin) "
                  "VALUES (now(), \"%s\", \"%s\", \"%s\")" % new_user_credentials)
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
    cursor.execute("INSERT INTO sessions (user_id, session_key) VALUES (\"%s\", \"%s\")" % (user_id, session_key))
    connection.commit()
    cursor.close()
    connection.close()
    return session_key

def delete_session(user_id):
    connection, cursor = connect_to_mysql()
    cursor.execute("DELETE FROM sessions WHERE user_id=\"%s\"" % user_id)
    connection.commit()
    cursor.close()
    connection.close()

def check_session(offered_session_key):
    connection, cursor = connect_to_mysql()
    cursor.execute("SELECT user_id, session_key FROM sessions WHERE session_key=\"%s\"" % offered_session_key)
    real_session_key=0
    for row in cursor:
        real_session_key=row[1]
    cursor.close()
    connection.close()
    if (offered_session_key == real_session_key):
        return (True)
    else:
        return (False)

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
    
    #bottle.debug(True)
    bottle.run(app=app, host='0.0.0.0', port=8080, reloader=True)

if __name__ == "__main__":
    main()
