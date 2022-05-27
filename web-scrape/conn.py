import mariadb
import sys

try:
    conn = mariadb.connect(
        user = "kaloro-db",
        password = "password",
        host = "localhost",
        database = "football-stats"
    )
    print ("Connected")
except mariadb.Error as e:
    print ("Could not connect to the database: " + e)
    sys.exit(1)
