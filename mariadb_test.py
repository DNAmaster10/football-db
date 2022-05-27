import mariadb
import sys
import "./web-scrape/conn.py"

print ("got to 1")
cur = conn.cursor()
cur.execute("INSERT INTO players (player,club) VALUES ('glen murrey', 'Brighton')")
conn.commit()
cur.close()
print ("got to 2")
