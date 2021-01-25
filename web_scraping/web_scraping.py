from bs4 import BeautifulSoup
import requests
import csv

pages = range(1, 24)

for page in pages:
    url = 'https://pl.trustpilot.com/review/www.allegro.pl?page={}'
    source = requests.get(url.format(page)).text
    soup = BeautifulSoup(source, 'lxml')

    for article in soup.find_all('article'):
        star = article.section.div.div.div.div.img
        sentiment = star.get('alt', '')[0]
        sentiment.strip()

        try:
            opinion = article.find('div', class_="review-content__body").find('p', class_="review-content__text").text.strip()
        except AttributeError as e:
            article.find('div', class_="review-content__body")
            continue

        with open('allegro_scraped1.csv', 'a', newline='', encoding="utf-8") as csv_file:
            try:
                csv_writer = csv.writer(csv_file)
            except UnicodeEncodeError as e:
                continue

            print(sentiment, opinion)
            csv_writer.writerow([sentiment, opinion])