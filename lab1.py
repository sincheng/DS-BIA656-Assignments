#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 14:27:39 2017

@author: sincheng
"""

#Import Library
import pandas as pd
import pylab as pl
import numpy as np
import re
import os


#Modify the path:
path ="/Users/sincheng/Desktop/Spring2017/BIA656/Python"    
os.chdir(path)

#Read dataset
df = pd.read_csv("./data/credit-training.csv")
df.head()

#1. Generate a table with number of null values by variable and assign to df_nullcount
df_nullcount = df.isnull().sum()


#2. Convert column names from camelCase into snake_case:
    #a.Create a function to convert string from camel case to snake case
def convert(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    #b.Test the function
convert('NumberOfTime30-59DaysPastDueNotWorse')
    #c.Get column name and store in a list
camelcase = list(df)
camelcase
    #d.Apply convert function to each column name
snakecase= list(map(convert , camelcase))
snakecase
    #e.Rename column name to snake case
df.columns = snakecase
    #f.Check converted column name
df.columns

#3. Count the number of cases with the following characteristics
    #a.people 35 or older
age35up = df['age'].loc[df['age'] >= 35].count()
print ("Number of people age>=35: " + str(age35up))
    #b.who have not been delinquent in the past 2 years
not_delinquent = df['serious_dlqin2yrs'].loc[df['serious_dlqin2yrs'] == 0].count()
print ("Number of people who have not been delinquent in the past 2 years: " + str(not_delinquent))
    #c.who have less than 10 open credit lines/loans
credit10 = df['number_of_open_credit_lines_and_loans'].loc[df['number_of_open_credit_lines_and_loans']<10].count()
print ("umber of people who have less than 10 open credit lines/loans: " +str(credit10))

#4. Repeat the exercise with these restrictions:
#   people who have been delinquent in the past 2 years
#   are in the 90th percentile for monthly_income

#Find 90th percentile monthly_income valie
income90= df['monthly_income'].quantile(0.9)
income90
#Create two restrictions boolean variable
restriction1 = df['serious_dlqin2yrs']==1
restriction2 = df['monthly_income'] <= income90
# Select all casess where under restriction 1 and restriction2 and assign to df_restriction dataframe
df_restriction = df[restriction1 & restriction2]
df_restriction.shape
#Repeat question 3
    #a.people 35 or older
print ("Number of people age>=35: " + str(df_restriction['age'].loc[df_restriction['age'] >= 35].count()))
    #b.who have not been delinquent in the past 2 years
print ("Number of people who have not been delinquent in the past 2 years: " + 
       str(df_restriction['serious_dlqin2yrs'].loc[df_restriction['serious_dlqin2yrs'] == 0].count()))
    #c.who have less than 10 open credit lines/loans

print ("umber of people who have less than 10 open credit lines/loans: " 
       +str(df_restriction['number_of_open_credit_lines_and_loans'].loc[df_restriction['number_of_open_credit_lines_and_loans']<10].count()
))