# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 15:55:23 2017
Class:656A
HW1
@author: sincheng
"""

#Preparation
#1.Check directory
import os;
print (os.getcwd());
      
      

#2.Import the library
import pandas as pd
import seaborn as sns

##Problem 1 - Indicate the number of lines in the file.

    #Read txt file and assign to dataframe
df_income = pd.read_csv('income1data.txt', sep=" ", header=None,
                 names=["annual_income", "sex", "martial_status","age","education",
                 "occupation","living_years","dual_income", "household_no", "household_u18",
                 "household_status","home_type","ethic","language"])
df_income.head()
    #Print the no. of line in dataframe
print(df_income.shape[0])

##Problem 2 -Indicate the number of lines in the file after eliminating those lines that have fields
#           characterized by unavailable (NA) data.

     #Drop the missing value and assign to df_income_cleaned dataframe
df_income_cleaned = df_income.dropna().astype(int)

    #Check the no. of line in cleaned dataframe
print(df_income_cleaned.shape[0])

    #Check if there are missing values still in new cleaned dataframe
print(df_income_cleaned.isnull().sum().sum())

##Problem 3 - Indicate the most common education level (the fifth column corresponds to education
#level).

    #Count frequency on education level
print(df_income_cleaned['education'].value_counts())

    #Plot a histagram to display the count on each education level
sns.countplot(x="education", data=df_income_cleaned)
sns.plt.show()

##Problem 4 - Indicate the level of income for households with some graduate school.
    

    #Select the row with condition where education level is grad school
df_grad = df_income_cleaned.loc[df_income_cleaned['education'] == 6]['annual_income'].reset_index()
    #Count frequency on education level = 6 which equal to grad study
    print(df_grad["annual_income"].value_counts())

    #Plot a histagram to display the level of annual income under education = 6
sns.countplot(x="annual_income", data=df_grad)



