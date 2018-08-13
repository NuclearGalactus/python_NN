from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse
from bs4 import BeautifulSoup


class LinkParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (key, value) in attrs:
                if key == 'href':
                    newUrl = parse.urljoin(self.baseUrl, value)
                    self.links = self.links + [newUrl]
    def getLinks(url):
        print("ASDL")
        links = []
        baseUrl = url
        print('askdmasldkm')
        response = urlopen(url)
        print(response.getheader('Content-Type'))
        if 'text/html' in response.getheader('Content-Type'):
            htmlBytes = response.read()
            soup = BeautifulSoup(htmlBytes,'lxml')
            baseUrl = url
            for link in soup.find_all('a'):
                print(link.get('href'))
                newUrl = [parse.urljoin(self.baseUrl,link.get('href'))]
                links = links + newUrl 
            if '/title/' in url:
                print("Movie Found: ", soup.html.title.string)

            return links
        else:
            return "",[]

    def spider(url, word, maxPages):
        pagesToVisit = [url]
        numberVisited = 0
        foundWord = False
        while numberVisited < maxPages and pagesToVisit != [] and not foundWord:      
            url = pagesToVisit[numberVisited]
            numberVisited = numberVisited + 1
            print(numberVisited, "Visiting:", url) 
            links = []
            baseUrl = url
            response = urlopen(url)
            if 'text/html' in response.getheader('Content-Type'):
                htmlBytes = response.read()
                soup = BeautifulSoup(htmlBytes,'lxml')
                baseUrl = url
                for link in soup.find_all('a'):
                    newUrl = parse.urljoin(baseUrl,link.get('href'))
                    links = links + [newUrl] 
                if '/title/' in url:
                    print("Movie Found: ", soup.html.title.string)
            for link in links:
                if link not in pagesToVisit:
                    pagesToVisit = pagesToVisit + [link]
        if foundWord:
            print("The word ", word, " was found at ", url)
        else:
            print("Finished")
LinkParser.spider("https://www.imdb.com/","jeff", 2000)
