import requests
import bs4

def make_bs_obj(url):
    r_obj = requests.get(url).text
    return bs4.BeautifulSoup(r_obj, features="html.parser")

def download(url, output_filename):
    with open(output_filename, 'w') as file:
        file.write(requests.get(url).text)


def make_pretty(url, output_filename):
    with open(output_filename, 'w') as file:
        file.write(make_bs_obj(url).prettify())


def find_paragraphs(url, output_filename):
    s_obj = make_bs_obj(url)
    p_list = s_obj.find_all('p')
    with open(output_filename, 'w') as file:
        for i in list(p_list):
            file.write(str(i)+"\n")


def find_links(url, output_filename):
    s_obj = make_bs_obj(url)
    ref_list = s_obj.find_all("a")
    with open(output_filename, 'w') as file:
        for item in list(ref_list):
            file.write(str(item.get("href")) + "\n")

find_links("https://cs111.byu.edu/articles/pair-programming/", "test.html")