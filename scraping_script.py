#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
from pprint import pprint

result = requests.get("https://www.whitehouse.gov/briefings-statements/")

# print(result.status_code)
# print(result.headers)

source = result.content
soup = BeautifulSoup(source, "html.parser")# Using Bs4
links = soup.find_all("a") # This contains the <a > tags that show there are links

def list_of_links():
    for link in links:
        print(link.get("href"))
        print("***********************")
    # if "About" in link.text:
    #     print(link)
    #     print(link.attrs["href"])


def titles():
    print(soup.title)
    heading_tags = soup.find_all("h2",  )
    for heading in heading_tags:
        print(heading)
        print("===========")

# Calls the defined funcion and runs it
# list_of_links()
titles()


""" Item Description = <span class=
"a-size-medium sc-product-title a-text-bold"> Xiaomi Mi A3 64GB + 4GB RAM, 
Triple Camera, 4G LTE Smartphone - International Global Version (Not just Blue)
                
            
        </span> """
# print([link for link in links], "==============")
# for link in links:
# 	print(link)
# 	print("==============")
