import sys
from bs4 import BeautifulSoup
from requests import get
from urllib import parse

def scavenger_hunt(url:str, tag:str, attr_name:str) -> str:
    """Recursively finds tags and attributes to find the final hint

    Args:
        url (str): page url
        tag (str): target tag
        attr_name (str): target attribute

    Returns:
        str: final string
    """
    response = get(url)
    soup = BeautifulSoup(response.text, features="html.parser")
    for t in soup.find_all(tag):
        if t.has_attr(attr_name):
            if attr_name == "final":
                return t[attr_name]
            next_list = t[attr_name].split(",")
            url = next_list[0]
            tag = next_list[1]
            attr_name = next_list[2]
            return scavenger_hunt(url, tag, attr_name)

def main():
    """Takes CLI and writes the solution to a file.
    """
    url = sys.argv[1]
    tag = sys.argv[2]
    attr_name = sys.argv[3]
    output_name = sys.argv[4]
    final_output = scavenger_hunt(url, tag, attr_name)
    with open(output_name, 'w') as file:
        file.write(final_output)


if __name__ == "__main__":
    main()