import urllib.request
from bs4 import BeautifulSoup
import mariadb
import sys
import time

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
try:
    if (row == None):
        print ("No players found in db")
    else:
        for (firstName, lastName, link) in cur.fetchall():
            time.sleep(3)
            theurl = link
            thepage = urllib.request.urlopen(theurl)
            soup = BeautifulSoup(thepage)
            for strong in soup.find_all("strong", string="Club:"):
                parent_tag = strong.parent
                for a in parent_tag.find_all("a"):
                    club = a.encode_contents()
                    club = str(club)
                    club = club.replace("b", "", 1)
                    club = club.replace("'", "")
            for img in soup.find_all("img", alt=f"{firstName} {lastName} headshot"):
                imgsrc = img["src"]
            statement = "SELECT firstname,lastname FROM players WHERE firstname=%s AND lastname=%s"
            data = (firstName, lastName)
            cur.execute(statement, data)
            rowt = cur.fetchone()
            if (rowt == None):
                statement = "INSERT INTO players (club,firstname,lastname,image) VALUES (%s,%s,%s,%s)"
                data = (club,firstName,lastName,imgsrc)
                try:
                    cur.execute(statement, data)
                    conn.commit()
                    print (f"Insert: {firstName} {lastName}, club = {club}")
                    print (statement)
                    print (imgsrc)
                except mariadb.Error as e:
                    print (e)
            else:
                statement = "UPDATE players SET club=%s,image=%s WHERE firstname=%s AND lastname=%s"
                data = (club,imgsrc,firstName,lastName)
                try:
                    cur.execute(statement, data)
                    conn.commit()
                    print (f"Update: {firstName} {lastName}, club = {club}")
                    print (statement)
                except mariadb.Error as e:
                    print (e)
except:
    print ("An error occured")
    cur.close()
    conn.close()
finally:
    cur.close()
    conn.close()
