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
        # print(sentiment.strip())

        # """pierwszy sposób wywala się gdy jest odpowiedź z allegro"""
        # opinion = article.section.div.find('div').find_next_sibling().p.text
        # print(opinion )
        """drugi sposób"""
        try:
            opinion = article.find('div', class_="review-content__body").find('p', class_="review-content__text").text.strip()
        except AttributeError as e:
            article.find('div', class_="review-content__body")
            continue

        try:
            with open('allegro_scraped.csv', 'a', newline = '') as csv_file:
                try:
                    csv_writer = csv.writer(csv_file)
                except UnicodeEncodeError as e:
                    continue
                # # csv_writer.writerow(['Sentiment', 'Opinion'])

                print(sentiment, opinion)
                csv_writer.writerow([sentiment, opinion])
        except UnicodeEncodeError as e:
            continue