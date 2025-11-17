import requests; import bs4
response_object = requests.get("https://fractured-quartz-studios.github.io/website/")
soup_object = bs4.BeautifulSoup(response_object.text, features="html.parser")
print(soup_object.prettify())