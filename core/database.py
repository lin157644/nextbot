import mariadb, sys, os
from dotenv import load_dotenv
load_dotenv()
db_user_passwd = os.getenv('DB_PASSWORD')
class Database():
    def __init__():
        # Connect to MariaDB Platform
        try:
            conn = mariadb.connect(
                user='root',
                password = db_user_passwd,
                host="127.0.0.1",
                port=3306,
                database="nextbot"
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

        # Get Cursor
        cur = conn.cursor()

