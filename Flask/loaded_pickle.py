from model_testing1 import x_test, x_test_countvectorizer, vectorizer, mnb
import pickle

# load model
with open(r'C:\Users\User\GIT\model testing\Ocena-komentarzy-NLP\Flask\sentiment_classifier.pkl', 'rb') as f:
    loaded_mnb = pickle.load(f)

# test_opinion = list(x_test)[0]
# test_sentiment = loaded_mnb.predict(x_test_countvectorizer[0])
# print(sentiment)
# print(test_opinion)
# print(test_sentiment)

# opinion = input('Wprowadź opinię: ')
def get_string(opinion):
    opinion = [opinion]
    new_test = vectorizer.transform(opinion)
    return loaded_mnb.predict(new_test)[0]
#
# int_sentiment = get_string(opinion)

def change_into_string(int_sentiment):
    if int_sentiment == 1:
        return "positive"
    else:
        return "negative"


# sentiment = get_string(opinion)
# change_sentiment = change_into_string(int_sentiment)
# print(change_sentiment)
