from bs4 import BeautifulSoup
import urllib2
import re
import json
import csv
from urlparse import urlparse

[{
    "NOTHS": {
        "url": {},
        "target": "",
        "ppp": "180",
        "next_page": ""
    }
}]

class WebScraper:

    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

    def scrape(self, year, url, config):
        product_dictionary = {}
        parsed_uri = urlparse(url)
        domain = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
        while True:
            request = urllib2.Request(url, headers=self.hdr)
            page = urllib2.urlopen(request)
            soup = BeautifulSoup(page, 'html.parser')
            for product in soup.select(config["target"]):
                product_dictionary[product['title']] = year
            try:
                url = domain + soup.select(config["next_page"])[0]['href']
                pages_scraped += 1
            except:
                break
        print 'NOTHS: Year {0} scraped succesfully'.format(year)
        return product_dictionary
