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
    print ("Connected")
except mariadb.Error as e:
    print ("Could not connect to the database: " + e)
    sys.exit(1)

while 1 == 1:
    theurl = input ("Enter the link to the team: ")
    tableID = ("stats_standard_11160")
    thepage = urllib.request.urlopen(theurl)
    soup = BeautifulSoup(thepage)
    table = soup.find_all("table", {"id" : tableID})
    for tag in table:
        tdTags = tag.find_all("th", {"class" : "left"})
        for tag in tdTags:
            player = (tag.text)
            print (player)
            player = player.split(" ", 1)
            if (len(player) > 1):
                player_f = player[0]
                player_l = player[1]
                urls = tag.find("a")
                try:
                    full_url = ("https://fbref.com" + urls['href'])
                    print (full_url)
                    try:
                        cur = conn.cursor()
                        statement = "SELECT link FROM player_links WHERE firstName=%s AND lastName=%s"
                        data = (player_f,player_l)
                        conn.commit()
                        cur.execute(statement, data)
                        row = cur.fetchone()
                        if (row == None):
                            statement = "INSERT INTO player_links (link,firstName,lastName) VALUES (%s,%s,%s)"
                            data = (full_url,player_f,player_l)
                            cur.execute(statement, data)
                        else:
                            print ("Player " + player_f + " " + player_l + " already exists in database")
                    except mariadb.Error as e:
                        print (e)
                        print ("An error occured when interacting with the database")
                except mariadb.Error as e:
                    print (e)
                    print (urls)
            else:
                print ("That is not a player")
        
