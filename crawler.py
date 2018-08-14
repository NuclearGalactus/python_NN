from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse
from bs4 import BeautifulSoup

class LinkParser(HTMLParser): 
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

    def spider(url, maxPages):
        f= open("movies.txt","w+")
        pagesToVisit = [url]
        numberVisited = 0
        while numberVisited < maxPages and pagesToVisit != []:      
            url = pagesToVisit[numberVisited]
            numberVisited = numberVisited + 1
            print(numberVisited, "Visiting:", url) 
            links = []
            baseUrl = url
            try:
                response = urlopen(url)
            except:
                print("Bad URL")
                continue
            if 'text/html' in response.getheader('Content-Type'):
                htmlBytes = response.read()
                soup = BeautifulSoup(htmlBytes,'lxml')
                if '/title/' in url:
                    f.write("Movie Found: " +  soup.html.title.string + "\n")
                baseUrl = url
                for link in soup.find_all('a'):
                    newUrl = parse.urljoin(baseUrl,link.get('href'))
                    if '/offsite/' in newUrl:
                        continue
                    refpos = newUrl.find('?')
                    #print(refpos)
                    if refpos > -1:
                        linkcat = newUrl[:refpos]
                        if linkcat not in pagesToVisit:                        
                            pagesToVisit = pagesToVisit + [linkcat]
        print("Finished")
LinkParser.spider("https://www.imdb.com/title/tt2231461/?ref_=fn_al_tt_1", 2000)
