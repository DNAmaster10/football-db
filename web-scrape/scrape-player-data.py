import urllib.request
from bs4 import BeautifulSoup
import mariadb
import sys

try:
    conn = mariadb.connect(
        user = "kaloro-db",
        password = "password",
        host = "localhost",
        database = "football-stats"
    )
    print ("connected")
except mariadb.Error as e:
    print ("Could not connect to the database")
    sys.exit(1)

cur = conn.cursor()
statement = "SELECT firstname,lastname,link FROM player_links"
conn.commit()
cur.execute(statement)
row = cur.fetchone()
if (row == None):
    print ("No players found in db")
else:
    for (firstName, lastName, link) in cur:
        print (f"First Name: {firstName}, Last Name: {lastName}")
