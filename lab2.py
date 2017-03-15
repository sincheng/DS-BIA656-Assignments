#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 16:49:55 2017

@author: sincheng
"""

#Import library
import pandas as pd
import numpy as np
import pylab as pl

#Load Boston Housing Dataset
from sklearn.datasets import load_boston

boston=load_boston()
print(boston.data.shape)
df = pd.DataFrame(boston.data,columns = boston.feature_names)

#Create a function to convert camel case to snake case
import re

def camel_to_snake(column_name):
    """
    converts a string that is camelCase into snake_case
    Example:
        print camel_to_snake("javaLovesCamelCase")
        > java_loves_camel_case
    See Also:
        http://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-camel-case
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', column_name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

#Create a dateframe with the Boston data
df = pd.DataFrame(boston.data,columns = boston.feature_names)
print(df.head())

#Apply function camel_to_snake to convert column name
snakecase= list(map(camel_to_snake , list(df)))
print(snakecase)
#Assign converted snakecase to column
df.columns = snakecase
print(df.columns)

#Create variable 'price' from boston.target
df['price'] = boston.target
df.head()

#Define feautures 
features = df[['age','lstat','tax']]

#Import Linear Regression
from sklearn.linear_model import LinearRegression

#Fit the model
x = features
y = df['price']
lm = LinearRegression()
lm.fit(x,y)

#Check the predicted values
lm.predict(x)[0:10]

#plot the predicted values against the actual values
import matplotlib.pyplot as plt


plt.scatter( df.price, lm.predict(x), s=5 )
plt.xlabel( "Prices")
plt.ylabel( "Predicted Prices")
plt.title( "Real vs Predicted Housing Prices")