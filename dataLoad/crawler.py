import requests
from bs4 import BeautifulSoup

def redditSpider():
    URL = 'http://canada.netflixable.com/2016/12/complete-alphabetical-list-thu-dec-15.html'
    source = requests.get(URL)
    Soup = BeautifulSoup(source.text, "html.parser")
    fw = open('movies.txt', 'w')
    for link in Soup.findAll('b'):
        fw.write(str(link.encode('utf-8')))
        fw.write('linebrk')

    fw.close()
redditSpider()

