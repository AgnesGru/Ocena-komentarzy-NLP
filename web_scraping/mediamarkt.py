import requests
from bs4 import BeautifulSoup
import csv

pages = range(1, 5)
for page in pages:
    url = 'https://www.ceneo.pl/sklepy/mediamarkt.pl-s12627/opinie-1'
    r = requests.get(url) # Response object called r.
    soup = BeautifulSoup(r.text, 'lxml') # parser lxml
    csv_file = open('media_scraped.csv', 'a')
    csv_writer = csv.writer(csv_file)

    for elem in soup.find_all(class_='user-post__content'):
        recomendation = elem.span.find_next_sibling().em
        if recomendation == None:
            continue
        else:
            print(recomendation.text.strip())

        opinions = elem.find('div', {'class':'user-post__text'})
        for opinion in opinions:
            print(opinion)

    csv_writer.writerows([recomendation, opinion])