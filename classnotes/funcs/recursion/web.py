import requests
import bs4
from urllib import parse

response = requests.get("https://CS111.byu.edu/robots.txt")
in_txt = response.text.split("\n")
bad_lst = []
for line in in_txt:
    if line.startswith("Disallow: "):
        bad_lst.append(line[10:])
print("Disallowed List:")
output = "\n".join(bad_lst)
print(output)

test_url = "https://CS111.byu.edu/Projects/project04/assets/"

def is_allowed(disallowed_paths,test_url):
    test_path = parse.urlparse(test_url).path
    for url in disallowed_paths:
        if test_path.startswith(disallowed_paths):
            return False
    return True

print(is_allowed(bad_lst, test_url))