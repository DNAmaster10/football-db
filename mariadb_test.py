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

print ("got to 1")
cur = conn.cursor()
cur.execute("INSERT INTO players (player,club) VALUES ('glen murrey', 'Brighton')")
conn.commit()
cur.close()
print ("got to 2")
