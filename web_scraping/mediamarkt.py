import requests
from bs4 import BeautifulSoup
import csv

pages = range(1, 40)
for page in pages:
    url = 'https://www.ceneo.pl/sklepy/mediamarkt.pl-s12627/opinie-{}'
    r = requests.get(url.format(page)) # Response object called r.
    soup = BeautifulSoup(r.text, 'lxml') # parser lxml

    for elem in soup.find_all(class_='user-post__content'):
        recomendation = elem.span.find_next_sibling().em
        if recomendation == None:
            continue
        else:
            recomendation
            if recomendation == 'poleceam':
                recomendation.string.replace_with('1')
            else:
                recomendation.string.replace_with('0')
        recomendation = recomendation.text.strip()

        opinions = elem.find('div', {'class':'user-post__text'})
        for opinion in opinions:
            opinion = str(opinion).replace('\n', ' ').strip()
        try:
            with open('allegro_scraped.csv', 'a',  newline = '') as csv_file:
                csv_writer = csv.writer(csv_file)
                print(recomendation, opinion)
                csv_writer.writerow([recomendation, opinion])

        except UnicodeEncodeError as e:
            continue