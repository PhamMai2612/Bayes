from __future__ import print_function
import json
import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory.'+ directory)

with open('test.json',encoding="utf8") as json_data:
    articles = json.load(json_data)
    print(len(articles), "Articles loaded successfully")

    list_of_type = {}

    for article in articles:
        types = article['type']
        createFolder('./'+types+'/')

        title = article['title']
        content = ''

        if types not in list_of_type:

            list_of_type[types] = 0
        else:
            list_of_type[types] = list_of_type[types] + 1

        for paragraph in article['content']:
            content = content + " " +paragraph

        completeName = os.path.join('./'+types+'/', str(list_of_type[types]) +'.txt')
        file = open(completeName, "w", encoding="utf8")
        file.write(title+ " "+content)

label = 0
total_filelist = []
total_label = []
for cate in list_of_type.keys():
    file_list = ["./"+cate+"/" + str(i)+".txt" for i in range(0,list_of_type[cate]+1)]
    for i in range(0, list_of_type[cate]+1):
        total_label.append(label)
    label += 1
    total_filelist.extend(file_list)

X = TfidfVectorizer(input= "filename").fit_transform(total_filelist).toarray()


# Splitting the dataset into the Training set and Test set
X_train, X_test, Y_train, Y_test = train_test_split(X, total_label, train_size=0.7, random_state=42)


# Predicting the Test set results
clf = GaussianNB()
clf.fit(X=X_train, y=Y_train)
print(clf.score(X=X_test, y=Y_test))

clf2 = MultinomialNB()
clf2.fit(X=X_train, y=Y_train)
print(clf2.score(X=X_test, y=Y_test))


