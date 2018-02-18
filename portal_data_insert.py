import mysql.connector
from mysql.connector import errorcode

users = (
    "CREATE TABLE IF NOT EXISTS `users` ("
    "  `no` int(10) NOT NULL AUTO_INCREMENT,"
    "  `reg_date` datetime NOT NULL,"
    "  `login` varchar(20) NOT NULL,"
    "  `password` varchar(20) NOT NULL,"
    "  `is_admin` boolean NOT NULL default 0,"
    "  PRIMARY KEY (`no`)"
    ") ENGINE=InnoDB"
)
sessions = ( 
    "CREATE TABLE IF NOT EXISTS `sessions` ("
    "  `user_id` int(10) NOT NULL,"
    "  `session_key` varchar(255) NOT NULL) ENGINE=InnoDB"
)

insert_query = "insert into users (reg_date, login, password, is_admin) " \
               "values (now(), %s, %s, %s)"
insert_data = [('admin', 'admin-pass', '1'),
               ('user1', 'user1-pass', '0'),
               ('user2', 'user2-pass', '0'),
               ('user3', 'user3-pass', '0'),
               ('user4', 'user4-pass', '0')]

try:
    connection = mysql.connector.connect(user='portal',
                                password='portal-secure-pass',
                                host='10.62.10.196',
                                port=3306,
                                database='portaldb')
    cursor = connection.cursor()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    print("Connection works good! ^^")
    cursor.execute(users)
    cursor.execute(sessions)
    #cursor.executemany(insert_query, insert_data)
    print('Data insertion was successful! ^^')
    connection.commit()
finally:
    cursor.close()
    connection.close()
