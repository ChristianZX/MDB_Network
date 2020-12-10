import pandas.io.sql as sqlio
import psycopg2
import API_Keys

def select_from_db(sql):
    '''
    Sends an SQL Statement to DB
    :param sql: SQL Statement that will be executed by the DB
    :return: Dataframe with Query Result
    '''
    connection = db_connect()
    df = sqlio.read_sql_query(sql, connection)  # stagin table
    db_close(connection)
    return df


def db_connect():
    '''
    :return: psycopg2 connection
    '''
    try:
        connection = psycopg2.connect(user=API_Keys.db_users,
                                      password=API_Keys.db_password,
                                      host=API_Keys.db_host,
                                      port=API_Keys.db_port,
                                      database=API_Keys.db_name)

        cursor = connection.cursor()
        cursor.execute("SELECT version();")
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", str(error))
    return connection


def db_close(connection):
    try:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
    except:
        pass


