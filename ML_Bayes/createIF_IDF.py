
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier

corpus = [
        'This is the first document.',
         'This document is the second document.',
         'And this is the third one.',
        'Is this the first document?',
    ]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())

print(X)



