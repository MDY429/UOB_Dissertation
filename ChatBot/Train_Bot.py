### import keras
from keras.optimizers import SGD
from keras.layers import Dense, Activation, Dropout
from keras.models import Sequential

### import nltk
import nltk
from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()
# print(wnl.lemmatize("cats","n"))

import numpy as np
import json
import pickle
import random

words = []
classes = []
documents = []
ignore_words = ['?', '!']
data_file = open('intents.json').read()
intents = json.loads(data_file)
# print(intents)

for intent in intents['intents']:
    for pattern in intent['patterns']:

        # Tokenize every words in pattern.
        w = nltk.word_tokenize(pattern)
        words.extend(w)

        # Add pattern words with corresponding tag.
        documents.append((w, intent['tag']))
        
        # Add tag to classes
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# Lemmatize and lower words
words = [wnl.lemmatize(w.lower()) for w in words if w not in ignore_words]
# Remove duplicated words
words = sorted(list(set(words)))

classes = sorted(list(set(classes)))

# documents = tag and pattern words
print(len(documents), "documents")

# classes = tag
print(len(classes), "classes", classes)

# words = every signal word.
print(len(words), "unique lemmatized words", words)

pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

