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
