import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site
        self.links = set()
        self.celebs = {}

    def get_links(self, number_of_pages):
        for i in range(1, number_of_pages):
            response = urllib.request.urlopen(self.site + str(i))
            soup = BeautifulSoup(response, "html.parser")
            for a in soup.find_all('a', href=True):
                link = a['href']
                if '-net-worth/' in link:
                    self.links.add(link)

    def scrape_networth(self, number_of_pages):
        self.get_links(number_of_pages)
        for link in self.links:
            response = urllib.request.urlopen(link)
            soup = BeautifulSoup(response.read(), "html.parser")
            try:
                name = soup.findAll("div", {"class": "title"})[0].text
                networth = soup.findAll("div", {"class": "value"})[0].text
                self.celebs[name] = networth
            except IndexError:
                pass
        print(self.celebs)

scraper = Scraper('https://www.celebritynetworth.com/category/richest-celebrities/page/')
scraper.scrape_networth(3)
