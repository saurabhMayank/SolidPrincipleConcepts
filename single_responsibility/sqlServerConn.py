import config
import mysql.connector
from mysql.connector import errorcode
from sqlalchemy import create_engine

cnx = mysql.connector.connect(
        host = config.host,
        user = config.user,
        password = config.passwd)
print(cnx)
cursor = cnx.cursor()
#insert Database Name
db_name = 'solidprinciplesproject'

#creates db
def create_database(cursor, database):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(database))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)
try:
    cursor.execute("USE {}".format(db_name))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(db_name))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor, db_name)
        print("Database {} created successfully.".format(db_name))
        cnx.database = db_name
    else:
        print(err)
        exit(1)
