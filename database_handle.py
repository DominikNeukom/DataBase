import psycopg2
import database_properties


# Connect to existing database

class DatabaseHandle(object):
    def __init__(self, database):
        """Creates the connection and curson to the entered Database"""
        self.DBP = database_properties.DatabaseProperties()
        self.database = database
        self.conn = self.create_connection()
        self.cur = self.create_cursor()
        print("Successfully connected to database: ", database)

    def create_connection(self):
        """Opens connection to selected database"""
        try:
            conn = psycopg2.connect(dbname=self.database,
                                    user=self.DBP.user,
                                    host=self.DBP.host,
                                    password=self.DBP.password)
        except ValueError:
            print('Connection attempt failed with properties:',
                  '\nDatabase: ', self.database,
                  '\nUser: ', self.DBP.user,
                  '\nHost: ', self.DBP.host)
            conn = None
            quit()

        return conn

    def create_cursor(self):
        """Opens a cursor to perform databse operations within current connection"""
        # Open a cursor to perform database operations
        cur = self.conn.cursor()

        return cur

    def close_database(self):
        """Closes connection and cursor objects of current stance"""
        self.conn.close()
        self.cur.close()
        pass
