import requests
from bs4 import BeautifulSoup

def redditSpider():
    URL = 'http://usa.netflixable.com/2017/03/complete-alphabetical-list-wed-mar-15.html'
    source = requests.get(URL)
    Soup = BeautifulSoup(source.text, "html.parser")
    fw = open('movies.txt', 'w')
    for link in Soup.findAll('b'):
        fw.write(str(link.encode('utf-8')))
        fw.write('linebrk')

    fw.close()
redditSpider()

