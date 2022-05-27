import mariadb
import sys
import "./conn.py"

print ("got to 1")
cur = conn.cursor()
cur.execute("INSERT INTO players (player,club) VALUES ('glen murrey', 'Brighton')")
conn.commit()
cur.close()
print ("got to 2")
