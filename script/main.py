import urllib.request as urllib2
from urllib.parse import urljoin
from bs4 import BeautifulSoup, SoupStrainer
import requests
import re
import os
import sh
import time
import ssl
import sys

URL_REGEX = "(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}"

class Crawl_stat:
    def __init__(self):
        self._browsed_page = 0
        self._downloaded_page = 0
        self._page_with_error = 0
        self._start_time = time.time()
        self._sum_of_time_page = 0.0

    @property
    def browsed_page(self):
        return self._browsed_page

    @browsed_page.setter
    def browsed_page(self, n):
        self._browsed_page = n

    @property
    def downloaded_page(self):
        return self._downloaded_page

    @downloaded_page.setter
    def downloaded_page(self, n):
        self._downloaded_page = n

    @property
    def page_with_error(self):
        return self._page_with_error

    @page_with_error.setter
    def page_with_error(self, n):
        self._page_with_error = n

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, n):
        self._start_time = n

    @property
    def sum_of_time_page(self):
        return self._sum_of_time_page

    @sum_of_time_page.setter
    def sum_of_time_page(self, n):
        self._sum_of_time_page = n

    def info(self):
        print("Browsed pages: {}".format(self.browsed_page))
        print("Downloaded pages: {}".format(self.downloaded_page))
        print("Errored pages: {}".format(self.page_with_error))
        print("Time of execution: {} seconds".format(time.time() - self.start_time))
        print("Average time browsing page: {}".format(self.sum_of_time_page / self.browsed_page))


class Crawl:
    def __init__(self, link, depth=1):
        self._link = link
        self._depth = depth

    def crawl(self):
        crawl_stat = Crawl_stat()
        pages = {self._link}
        indexed_url = set()
        for i in range(0, self._depth):
            print("depth {}/{}".format(i + 1, self._depth))
            for page in pages:
                time_page = time.time()
                indexed_url.add(page)
                # try:
                c = urllib2.urlopen(page)
                # except:
                #     print("failed to open {}".format(page))
                #     crawl_stat.page_with_error += 1
                #     continue
                crawl_stat.browsed_page += 1
                page_filename = re.sub("http(s)?://", "", page) #remove scheme part of URL
                page_filename = re.sub('/$', '', page_filename) # remove end / if present
                page_filename = page_filename + "/index.html" if "." in page_filename else page_filename # Create index.html to avoid directory and file with the same name
                self.create_path(page_filename)
                try:
                    request = requests.get(page, timeout=10, stream=True)
                    with open("content/" + page_filename, 'wb') as fh:
                        for chunk in request.iter_content(1024 * 1024):
                            fh.write(chunk)
                except:
                    print("failed to retrieve {}".format(page))
                    crawl_stat.page_with_error += 1
                    continue
                crawl_stat.downloaded_page += 1
                for link in BeautifulSoup(c.read(), parse_only=SoupStrainer('a'), features="html.parser", from_encoding="iso-8859-1"):
                    if link.has_attr('href'):
                        url = urljoin(page, link['href'])
                        if url.find("'") != -1:
                                continue
                        url = url.split('#')[0] 
                        if url[0:4] == 'http':
                                indexed_url.add(url)
                sh.sed('-i', 's/href="\(https:\/\)/href="/g', 'content/' + page_filename)
                crawl_stat.sum_of_time_page += (time.time() - time_page)
            pages.clear()
            pages.update(indexed_url)
        crawl_stat.info()
        return int(crawl_stat.page_with_error != 0)        

    def create_path(self, filename, prefix="content/"):
        directory = prefix + re.sub('([^/]+)$', '', filename)
        try:
            os.makedirs(directory, exist_ok = True)
        except OSError as error:
            print("Directory '{}' can not be created".format(directory))

if __name__ == "__main__":
    # if len(sys.argv) == 1:
    #     print("You need to provide the url to crawl\n ex: python3 main.py https://www.orchestra.eu")
    #     sys.exit(3)
    # elif len(sys.argv) > 2:
    #     print("There are too many arguments here")
    #     sys.exit(3)
    # if not re.fullmatch(URL_REGEX, sys.argv[1]):
    #     print("The url doesn't seem to be valid")
    #     sys.exit(3)
    # crawl = Crawl(sys.argv[1], 3)
    # sys.exit(crawl.crawl())
    c = urllib2.urlopen("https://stackoverflow.com")