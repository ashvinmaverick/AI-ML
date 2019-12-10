#!/usr/bin/env python3

import pandas as pd

data = pd.read_csv('People Charm case.csv')

import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix


#LOGISTIC REGRESSION

new_data = pd.get_dummies(data, drop_first = True)
columns_list = list(new_data.columns)
print(columns_list)

features = list(set(columns_list)-set(['left']))

y = new_data['left'].values
print(y)

x = new_data[features].values
print(x)

train_x, test_x, train_y, test_y = train_test_split(x,y, test_size = 0.25, random_state = 2)

logistic = LogisticRegression()

logistic.fit(train_x, train_y)

prediction = logistic.predict(test_x)

confusion_matrix = confusion_matrix(test_y, prediction)
print(confusion_matrix)

accuracy_score = accuracy_score(test_y, prediction)
print(accuracy_score)

print('Misclassified Samples: %d' % (test_y != prediction).sum())
