
from sklearn.naive_bayes import GaussianNB
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import pandas as pd

data = pd.read_csv("TitanicPreprocessed.csv")
Y = data.values[:, -1]
X = data.values[:, 0:-1]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.7, random_state=42)
clf = GaussianNB()
clf.fit(X=X_train, y=Y_train)
print(clf.score(X=X_test, y=Y_test))

clf2 = MultinomialNB()
clf2.fit(X=X_train, y=Y_train)
print(clf2.score(X=X_test, y=Y_test))

