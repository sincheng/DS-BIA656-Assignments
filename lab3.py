#Import Libraries
import pandas as pd
import numpy as np
import os

#Set directory:
os.chdir('/Users/sincheng/Desktop/Spring2017/BIA656/Python/HW/Lab3')
os.getcwd()

#Read the csv file
df = pd.read_csv("credit-data-post-import.csv")
df.head()

#Split the data into training(75%) and testing(25%)
is_test = np.random.uniform(0, 1, len(df)) > 0.75
train = df[is_test==False]
test = df[is_test==True]

#Check how many records in both files
len(train), len(test)

#Split our data into 2 groups; data containing nulls and data not containing nulls
train_w_monthly_income = train[train.monthly_income.isnull()==False]
train_w_null_monthly_income = train[train.monthly_income.isnull()==True]

#Import random forest regressor
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()

#Train the data not containing nulls on the monthly_income variable
cols = ['number_real_estate_loans_or_lines', 'number_of_open_credit_lines_and_loans']
rf.fit(train_w_monthly_income[cols], train_w_monthly_income.monthly_income)

#Make 'predictions' on the null monthly income data
new_values = rf.predict(train_w_null_monthly_income[cols])
new_values

#Assign the prediction to the train_w_null_monthly_income dataset
train_w_null_monthly_income['monthly_income'] = new_values

#Combine the data back together
train = train_w_monthly_income.append(train_w_null_monthly_income)
len(train)

#Predict monthly income from test dataset
predicted_income= rf.predict(test[cols])
predicted_income

#Assign the prediction to monthly_income_inputed from test dataset
test['monthly_income_imputed'] = predicted_income

#Fill in predicted monthly income if monthly_income is null
test['monthly_income'] = np.where(test.monthly_income.isnull(), test.monthly_income_imputed,
                                  test.monthly_income)

#Ensure no null values in train and test
print (pd.value_counts(train.monthly_income.isnull()))
print (pd.value_counts(test.monthly_income.isnull()))

#Export train and test datasets in the csv files
train.to_csv("credit-data-trainingset.csv", index=False)
test.to_csv("credit-data-testset.csv", index=False)
