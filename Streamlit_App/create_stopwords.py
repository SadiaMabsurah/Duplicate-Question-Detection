import pickle
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

STOP_WORDS = list(ENGLISH_STOP_WORDS)

with open("stopwords.pkl", "wb") as f:
    pickle.dump(STOP_WORDS, f)

print("stopwords.pkl created successfully")
