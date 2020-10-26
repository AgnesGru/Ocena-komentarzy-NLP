import pickle
import os

dir_path = os.path.dirname(os.path.realpath(__file__)) # to get full path of script location (not working directory)

# load model
with open(os.path.join(dir_path, 'pickeld_sentiment_classifier.pkl'), 'rb') as f:
    loaded_mnb = pickle.load(f)

with open(os.path.join(dir_path, 'pickeld_vectorizer.pkl'), 'rb') as f:
    loaded_vectorizer = pickle.load(f)

def get_string(opinion):
    opinion = [opinion]
    new_test = loaded_vectorizer.transform(opinion)  # transform into vector
    return loaded_mnb.predict(new_test)[0]  # return loaded_mnb element of the list


def change_into_string(int_sentiment):
    if int_sentiment == 1:
        return "Twoja opinia jest pozytywna"
    else:
        return "Twoja opinia jest negatywna"

