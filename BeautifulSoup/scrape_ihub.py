import requests
from bs4 import BeautifulSoup

url = "https://ihub.co.ke/jobs"
results = requests.get(url)
source = results.content
soup = BeautifulSoup(source, "html.parser")

def show_links():
    links = soup.find_all("a")
    for link in links:
        plain_url = link.get("href")
        texts_of_links = link.text
        print(plain_url, texts_of_links)
        print("*************************************")

def company_job():
    company_name = soup.find_all("h3")
    for name in company_name:
        print(name.text)
show_links()


