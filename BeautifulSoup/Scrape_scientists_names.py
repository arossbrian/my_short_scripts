#!/usr/bin/python3
"""
I want to scrape a list of Scientists from a website and store the information
in a DB. I shall decide the nature of the DB
"""
import requests
from bs4 import BeautifulSoup

url =  "http://www.fabpedigree.com/james/mathmen.htm#Legendre"

source = requests.get(url)
results = source.content
soup = BeautifulSoup(results, "html.parser")

# The names are embeded within links so we might need to use the <a> tags and filter with the "href"
a_tags = soup.find_all("a")
for tag in a_tags:
    if tag != "top":
        print(tag.text)

