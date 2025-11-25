from urllib.parse import urlparse, urljoin
from requests import *
import bs4
from bs4 import MarkupResemblesLocatorWarning
import warnings

warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)

def get_domain(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        return ""
    parsed = urlparse(url)
    return parsed.scheme +"://"+ parsed.netloc

def combine_paths(url, path):
    return urljoin(url, path)

def combine_urls(url,path):
    return combine_paths(url,path)

def print_pages(url, list_of_paths, output_name):
    out_list = []
    for path in list_of_paths:
        combined_url = combine_paths(url, path)
        url = combined_url
        r_obj = get(combined_url).text
        s_obj = bs4.BeautifulSoup(r_obj, features="html.parser")
        out_list.append(s_obj.get_text(strip=True))
    with open(output_name, 'w') as file:
        for string in out_list:
            file.write(string + "\n")