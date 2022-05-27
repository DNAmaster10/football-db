import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns
#Function scrapes table of choice from the Fbref.com site
def scrape_fbref(url, table_number):
    #Defining variables - url to the website + the table of choice (starting from 0 for the first table on the top)
    url = url
    table_number = table_number
    global data
    #Changing Fbref's HTML so all tables are redable by bs4
    html_content = requests.get(url).text.replace('<!--', '').replace('-->', '')
    df = pd.read_html(html_content)
    #Loading DF
    data = df[table_number]
    # Changing column names from tuples to strings 
    column_names = ["_".join(col) for col in data.columns.values]
    column_names = [col.replace("Unnamed: ","").replace('_level_0','') for col in column_names]
    data.columns = column_names
    # If need to drop NaN's from the start, uncomment the code below
#     data = data.dropna()
    data[data.columns[0]]
    if data.columns[0] == "0_Rk":
        data[data['1_Player'] != 'Player']
        del data['0_Rk']
    elif data.columns[0] == '0_Player':
        data[data['0_Player'] != 'Player']

scrape_fbref("https://fbref.com/en/players/532e1e4f/Pau-Torres", 1)
