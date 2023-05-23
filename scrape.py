import requests
from bs4 import BeautifulSoup




# request URL to grab data from
res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.tiitleline')
votes = soup.select('.score')
print(votes[0])