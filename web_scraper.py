import os
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

year = 2020
url = "https://www.basketball-reference.com/teams/BRK/{}/gamelog/".format(year)
html = urlopen(url)

soup = BeautifulSoup(html,features="html.parser")
# Extracts the headers of each table
soup.findAll('tr', limit=4)
headers = [th.getText() for th in soup.findAll('tr', limit=2)[1].findAll('th')]
headers = headers[1:]
# Extracts Row Data from table and converts into DF
rows = soup.findAll('tr')[1:]
game_log = [[td.getText() for td in rows[i].findAll('td')] for i in range(len(rows))]
games = pd.DataFrame(game_log, columns = headers)

games.to_csv(r'C:\Users\verga\Documents\Projects\nba_analytics\bkn_2019-2020.csv')
