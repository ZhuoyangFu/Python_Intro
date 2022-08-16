import urllib.request
import urllib.error
from bs4 import BeautifulSoup

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

for i in range(count):
    html = urllib.request.urlopen(url).read()
    bs = BeautifulSoup(html, 'html.parser')
    tags = bs('a')
    url = tags[position-1].get('href')
    print(url)

