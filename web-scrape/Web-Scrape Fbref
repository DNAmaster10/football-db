import requests
from bs4 import BeautifulSoup, Comment


url = 'https://fbref.com/en/squads/18bb7c10/Arsenal-Stats'
soup = BeautifulSoup(requests.get(url).content, 'html.parser')

table = soup.select_one('table[id^="stats_standard"]')

#print some information from the table to screen:
for tr in table.select('tr:has(td)'):
    tds = [td.get_text(strip=True) for td in tr.select('td')]
    print('{:<30}{:<20}{:<10}'.format(tds[0], tds[3], tds[5]))

