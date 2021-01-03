#!/usr/bin/env python
# coding: utf-8

import pickle
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# raise ValueError('błąd')

data = pd.read_csv(r'C:\Users\User\GIT\model testing\Ocena-komentarzy-NLP/web_scraping/allegro_scraped1.csv', sep=',',
                   names=['Sentiment', 'Opinion'], encoding='utf-8')
df = pd.DataFrame(data)

# ### How many cells with positive sentiment?
# print(len(df[df.Sentiment == 1]))
# print(len(df[df.Sentiment == 5]))

df.loc[df['Sentiment'] == 1, 'Sentiment'] = 0
df.loc[df['Sentiment'] == 5, 'Sentiment'] = 1

df_x = df['Opinion']
df_y = df['Sentiment']

vectorizer = CountVectorizer()

x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.25,
                                                    random_state=4)  # tu sobie pozmieniaj na 0.33 i ziarno też zmień

x_train_countvectorizer = vectorizer.fit_transform(x_train)

# print(x_train[0])
# print(x_train_countvectorizer[0])

mnb = MultinomialNB()

mnb.fit(x_train_countvectorizer, y_train)

x_test_countvectorizer = vectorizer.transform(x_test)

pred = mnb.predict(x_test_countvectorizer)
# print(pred)

rezult = np.array(y_test)
# print(rezult)

count = 0

for i in range(len(pred)):
    if pred[i] == rezult[i]:
        count += 1

print(count)
print(len(pred))

accuracy = count/len(pred)
print(accuracy)

# ### The evaluation of coments typed by the user.

# test_set = ['zdecydowanie nie polecam tego gównianego sklepu']
# new_test = vectorizer.transform(test_set)
# mnb.predict(new_test) # model przewiduje, czy wpisane zdanie jest positive=1, czy negative=0

with open(r'C:\Users\User\GIT\model testing\Ocena-komentarzy-NLP\Flask\pickeld_sentiment_classifier.pkl', 'wb') as f:
    pickle.dump(mnb , f)

with open(r'C:\Users\User\GIT\model testing\Ocena-komentarzy-NLP\Flask\pickeld_vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer , f)
