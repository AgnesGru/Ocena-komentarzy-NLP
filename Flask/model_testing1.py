#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import pickle

# ### Data reading

data = pd.read_csv("Sentiments.csv", sep=';', names = ['Opinion', 'Sentiment'],  encoding= 'unicode_escape')
df = pd.DataFrame(data)
# shows top 10 rows
df.head(10)


# ### How many cells with positive sentiment?

len(df[df.Sentiment == 'positive'])


# ### Change positive to 1 and negative to 0

df.loc[df['Sentiment'] == 'positive', 'Sentiment']=1
df.loc[df['Sentiment'] == 'negative', 'Sentiment']=0

df.head()

# ### Separate Opinion from Sentiment

df_x =df['Opinion']
df_y = df['Sentiment']

df_x

# ### CountVectorizer

vectorizer = CountVectorizer()

# ### Dividing into subsets of training data and test data

x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size = 0.25, random_state = 4)

# ### Changing text into matrix

x_train_countvectorizer = vectorizer.fit_transform(x_train)

# print(x_train[0])
# print(x_train_countvectorizer[0])

x_train_countvectorizer.toarray()

# ### Clasification

mnb = MultinomialNB()

y_train = y_train.astype('int')

# ### Fit vector to sentiment

mnb.fit(x_train_countvectorizer, y_train) 

# ### Change test opinion into wector

x_test_countvectorizer = vectorizer.transform(x_test)

# ### Predict using clasifier test data

pred = mnb.predict(x_test_countvectorizer)

pred

# ### Change into array test sentiments

rezult = np.array(y_test)

rezult

# #### For all predicted data

count = 0

for i in range(len(pred)):
    if pred[i] == rezult[i]:
        count += 1        

count

len(pred)

# #### Precyzja metody pomiaru – stopień zgodności między wynikami uzyskanymi w określonych warunkach z wielokrotnych pomiarów tej samej wielkości.

accuracy = count/len(pred)

accuracy


# ### Ocena komentarzy wpisywanych przez urzytkownika, na podstawie modelu, który stworzyłam!

test_set = ['I do not konow if I like this movie']  # nowy zestaw danych, w takiej postaci można wpisuwać do zmiennej Flaska

new_test = vectorizer.transform(test_set) # transformacja nowego zestawu danych do postaci wektorowej

mnb.predict(new_test) # model przewiduje, czy wpisane zdanie jest positive=1, czy negative=0


# Pickle
with open(r'C:\Users\User\GIT\model testing\Ocena-komentarzy-NLP\Flask\sentiment_classifier.pkl', 'wb') as f:
    pickle.dump(mnb, f)


