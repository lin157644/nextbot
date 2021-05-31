import mariadb, sys

class Database():
    def __init__(self, db_user, db_passwd):
        self.connect(db_user, db_passwd)
        # Get Cursor
        self.getCursor()
    
    def connect(self, db_user, db_passwd):
        # Connect to MariaDB Platform
        try:
            self.conn = mariadb.connect(
                user = db_user,
                password = db_passwd,
                host="127.0.0.1",
                port=3306,
                database="nextbot"
            )
            self.conn.autocommit = True
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)
    
    def disconnect(self):
        # Close Connection
        self.conn.close()
    
    def getCursor(self):
        self.cur = self.conn.cursor()

