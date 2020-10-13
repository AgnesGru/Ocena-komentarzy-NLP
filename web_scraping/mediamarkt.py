import requests
from bs4 import BeautifulSoup
import csv

pages = range(1, 3)
for page in pages:
    url = 'https://www.ceneo.pl/sklepy/mediamarkt.pl-s12627/opinie-1'
    r = requests.get(url) # Response object called r.
    soup = BeautifulSoup(r.text, 'lxml') # parser lxml

    for elem in soup.find_all(class_='user-post__content'):
        recomendation = elem.span.find_next_sibling().em
        if recomendation == None:
            continue
        else:
            recomendation = recomendation.text.strip().lstrip()

        opinions = elem.find('div', {'class':'user-post__text'})
        for opinion in opinions:
            opinion = opinion.strip()

        with open('media_scraped.csv', 'w',  newline = '') as csv_file:
            csv_writer = csv.writer(csv_file)

            print(recomendation, opinion)
            csv_writer.writerow([recomendation, opinion])