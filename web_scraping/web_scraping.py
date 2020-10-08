from bs4 import BeautifulSoup
import requests

pages = range(1, 23)

for page in pages:
    source = requests.get('https://pl.trustpilot.com/review/www.allegro.pl?page={}'.format(page)).text
    soup = BeautifulSoup(source, 'lxml')
    # print(soup.prettify())

    for article in soup.find_all('article'):
        star = article.section.div.div.div.div.img
        sentiment = star.get('alt', '')[0]
        print(sentiment)

        # """pierwszy sposób wywala się gdy jest odpowiedź z allegro"""
        # opinion = article.section.div.find('div').find_next_sibling().p.text
        # print(opinion )

        """drugi sposób"""
        try:
            opinion = article.find('div', class_="review-content__body").find('p', class_="review-content__text").text

        except AttributeError as e:
            opinin = None

        print(opinion)
