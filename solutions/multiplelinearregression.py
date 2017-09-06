# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:, :4]

from sklearn.preprocessing import LabelEncoder, OneHotEncoder 
LE_X = LabelEncoder()
X[:, 3] = LE_X.fit_transform(X[:,3])
X = OneHotEncoder(categorical_features=[3]).fit_transform

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(X_train, y_train)

y_pred = reg.predict(X_test)

df = pd.DataFrame(data)
df.plot(kind='density', colormap = 'red')
df.show()