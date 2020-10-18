# from model_testing_comments_from_internet import  vectorizer
import pickle
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
# from sklearn.feature_extraction.text import CountVectorizer

# load model
with open(os.path.join(dir_path, 'pickeld_sentiment_classifier.pkl'), 'rb') as f:
    loaded_mnb = pickle.load(f)

with open(os.path.join(dir_path, 'pickeld_vectorizer.pkl'), 'rb') as f:
    loaded_vectorizer = pickle.load(f)

# test_opinion = list(x_test)[0]
# test_sentiment = loaded_mnb.predict(x_test_countvectorizer[0])
# print(test_opinion)
# print(test_sentiment)
# vectorizer = CountVectorizer()
# opinion = input('Wprowadź opinię: ')
def get_string(opinion):
    opinion = [opinion]  # make a list
    new_test = loaded_vectorizer.transform(opinion)  # transform into vector
    return loaded_mnb.predict(new_test)[0]  # return loaded_mnb element of the list

# int_sentiment = get_string(opinion)

def change_into_string(int_sentiment):
    if int_sentiment == 1:
        return "Twoja opinia jest pozywywna"
    else:
        return "Twoja opinia jest negatywna"


# sentiment = get_string(opinion)
# print(sentiment)
# change_sentiment = change_into_string(int_sentiment)
# print(change_sentiment)