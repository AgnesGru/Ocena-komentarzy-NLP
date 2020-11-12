#!/usr/bin/env python
# coding: utf-8

import pickle
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

# nltk.download('stopwords')

# raise ValueError('błąd')

data = pd.read_csv(r'C:\Users\User\GIT\model testing\Ocena-komentarzy-NLP/web_scraping/allegro_scraped1.csv', sep=',', names = ['Sentiment', 'Opinion'],  encoding= 'utf-8')
stopwords = pd.read_csv(r'C:\Users\User\GIT\model testing\Ocena-komentarzy-NLP/stopwords.txt', names = ['slowo'], encoding= 'utf-8' )
df_stopwords = [i for i in stopwords['slowo']]
df = pd.DataFrame(data)
# print(df_stopwords)

# ### How many cells with positive sentiment?
# print(len(df[df.Sentiment == 1]))
# print(len(df[df.Sentiment == 5]))

# data cleaning and preprocesing
ps = PorterStemmer()
lem = WordNetLemmatizer()
corpus = []

for i in range(0, len(df)):
    # review = re.sub('[^a-zA-Z]', ' ', df['Opinion'][i]) # does not work in polish
    review = (df['Opinion'][i]).lower()
    review = review.split()
    review = [elem.strip('''!()-[]{};:'"\, <>./?@#$%^&*_~''') for elem in review] # remove some punctuation
    review = [lem.lemmatize(word) for word in review ] # lematyzacja
    # review = [review for i in review if not i in df_stopwords] # delete stopwords, it needs to be corrected yet
    review = ' '.join(review)
    corpus.append(review)
# print(corpus)


cv = CountVectorizer()
X = cv.fit_transform(corpus).toarray()  # changing words into vector
# print(X)

y = pd.get_dummies(data['Sentiment'])
y = y.iloc[:,4].values  # takes elements from 5-th column 0- negative, 1-positive
# print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

sentiment_model = MultinomialNB().fit(X_train, y_train)

y_pred = sentiment_model.predict(X_test)

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
confusion = confusion_matrix(y_test, y_pred)
# print(confusion)
accuracy = accuracy_score(y_test, y_pred)
print(accuracy)
