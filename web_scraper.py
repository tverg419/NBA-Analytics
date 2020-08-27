import os
from urllib.request import urlopen

from bs4 import BeautifulSoup
import pandas as pd
# First url is customizable but it extracted data from the first table but the
# desried table was table 4
year = 2019
# url = "https://www.basketball-reference.com/teams/BRK/{}.html".format(year)
url = "https://www.basketball-reference.com/teams/NJN/stats_basic_totals.html"
html = urlopen(url)

soup = BeautifulSoup(html,features="html.parser")

soup.findAll('tr', limit=2)
headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
headers = headers[1:]
print(headers)

rows = soup.findAll('tr')[1:]
team_stats = [[td.getText() for td in rows[i].findAll('td')] for i in range(len(rows))]
totals = pd.DataFrame(team_stats, columns = headers)
totals.head(10)
print(team_stats[20])

totals.to_csv('BKN_1967-2019.csv')
