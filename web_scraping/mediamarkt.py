import requests
from bs4 import BeautifulSoup
import csv

pages = range(1, 50)
for page in pages:
    url = 'https://www.ceneo.pl/sklepy/mediamarkt.pl-s12627/opinie-{}'
    r = requests.get(url.format(page)) # Response object called r.
    soup = BeautifulSoup(r.text, 'lxml') # parser lxml

    for elem in soup.find_all(class_='user-post__content'):
        recomendation = elem.span.find_next_sibling().em
        if recomendation == None:
            continue
        else:
            recomendation = recomendation.text.strip().strip()

        opinions = elem.find('div', {'class':'user-post__text'})
        for opinion in opinions:
            opinion = opinion.strip()
        try:
            with open('media_scraped.csv', 'a',  newline = '') as csv_file:
                csv_writer = csv.writer(csv_file)
                print(recomendation, opinion)
                csv_writer.writerow([recomendation, opinion])

        except UnicodeEncodeError as e:
            continue