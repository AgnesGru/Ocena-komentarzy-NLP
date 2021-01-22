import csv
from sqlalchemy import create_engine, Table, Column, Integer, MetaData, Text

engine = create_engine('sqlite:///sqlalchemy.db', echo=True)

metadata = MetaData()
# Define the table with sqlalchemy:
my_table = Table('MyTable', metadata,
    Column('Sentiment', Integer),
    Column('Opinion', Text),
)
metadata.create_all(engine)
insert_query = my_table.insert()

with open(r'C:\Users\User\GIT\model testing\Ocena-komentarzy-NLP/web_scraping/allegro_scraped1.csv', 'r', encoding="utf-8") as file:
    csv_reader = csv.reader(file, delimiter=',')
    engine.execute(
        insert_query,
        [{"Sentiment": row[0], "Opinion": row[1]}
            for row in csv_reader]
    )

