import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = "https://ihub.co.ke/jobs"
results = requests.get(url)
source = results.content
soup = BeautifulSoup(source, "html.parser")
show_links = soup.find_all("a")[0].attrs  #<a href="/jobs/view/4856/technical-drafts-man-required"> Technical Drafts Man Required</a>
# print(show_links)
body_text = soup.find("body").get_text
print(body_text)
# <div class="post-description">
# <a href="/jobs/view/4880/customer-success-manager">
# Social edtech startup: educating the poorest 1 billion children
# Over 600 million children are not achieving minimum proficiency levels in reading and math. With the rapid penetration of smartphones in Africa, for the first time in history, we will be able to reach these children at massive…
# </a>
# </div>


def links_in_page():
    for link in show_links:
        print(link)
        print("=============")

def link_description():
    for link in show_links:
        print(link)
        print("========+===++====+++==================================")

# link_description()
# links_in_page()





