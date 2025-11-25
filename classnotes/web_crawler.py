import requests
from urllib import parse
from bs4 import BeautifulSoup
from sys import argv
'''
Recursive
Read HTML file
Check robots.txt
Download imgs
Visit other links
Fix links by combining with current url 
Keep track of visited links
'''

visited_links = set()

start_url = "https://wikipedia.org/wiki/Giant_panda"
start_url = "https://calendar.byu.edu/events"
#argv[1] = "pics" #TODO: Remove later

destination = "pics"#argv[1]

def crawl(url):
    #download html
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="html.parser")
    for img in soup.find_all("img"):
        if img.has_attr("src"):
            src = img["src"]
        fixed_src = parse.urljoin(url, src)
        response = requests.get(fixed_src)
        file_name = fixed_src.split('/')[-1]
        full_file_name = f"{destination}\\{file_name}"
        # save picture locally
        with open(full_file_name, "wb") as outfile:
            outfile.write(response.content)

        #for each link
        for a in soup.find_all("a"):
            if a.has_attr("href"):
                href = a["href"]
                fixed_href = parse.urljoin(url, href)
                normalized_url = parse.urlparse(fixed_href)
                normalized_url.query = ""
                normalized_url = str(normalized_url)
                if normalized_url not in visited_links:
                    visited_links.add(fixed_href)
                    crawl(fixed_href)



if __name__ == "__main__":
    crawl(start_url)