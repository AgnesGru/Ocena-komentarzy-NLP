#!/usr/bin/env python
# coding: utf-8

import pickle
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer

data = pd.read_csv(r'C:\Users\User\GIT\model testing\Ocena-komentarzy-NLP/web_scraping/allegro_scraped1.csv', sep=',',
                   names=['Sentiment', 'Opinion'], encoding='utf-8')
df = pd.DataFrame(data)

# ### How many cells with positive or negative sentiment?
# print(len(df[df.Sentiment == 1])) #514
# print(len(df[df.Sentiment == 5])) #626

df.loc[df['Sentiment'] == 1, 'Sentiment'] = 0
df.loc[df['Sentiment'] == 5, 'Sentiment'] = 1

df_x = df['Opinion']
df_y = df['Sentiment']

vectorizer = CountVectorizer()
x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.25, random_state=10)
x_train_countvectorizer = vectorizer.fit_transform(x_train) # Document Term Matrix
# print(vectorizer.get_feature_names()[1000:1010])

mnb = MultinomialNB()
mnb.fit(x_train_countvectorizer, y_train)
x_test_countvectorizer = vectorizer.transform(x_test)

pred = mnb.predict(x_test_countvectorizer)
rezult = np.array(y_test)

count = 0
for i in range(len(pred)):
    if pred[i] == rezult[i]:
        count += 1

print(count)
print(len(pred))
accuracy = count/len(pred)
print(accuracy) #0.911
# #
# with open(r'C:\Users\User\GIT\model testing\Ocena-komentarzy-NLP\Flask\pickeld_sentiment_classifier.pkl', 'wb') as f:
#     pickle.dump(mnb , f)
#
# with open(r'C:\Users\User\GIT\model testing\Ocena-komentarzy-NLP\Flask\pickeld_vectorizer.pkl', 'wb') as f:
#     pickle.dump(vectorizer , f)

TFIDF
vectorizer = TfidfVectorizer()
# x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.25,
#                                                     random_state=10)
# X = vectorizer.fit_transform(x_train)
# mnb = MultinomialNB()
#
# mnb.fit(X, y_train)
#
# x_test_countvectorizer = vectorizer.transform(x_test)
#
# pred = mnb.predict(x_test_countvectorizer)
#
# rezult = np.array(y_test)
# # print(rezult)
#
# count = 0
# for i in range(len(pred)):
#     if pred[i] == rezult[i]:
#         count += 1
#
# print(count)
# print(len(pred))
# accuracy = count/len(pred)
# print(accuracy) #0.925