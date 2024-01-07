# **Data-cleaning process using Python pandas library**

# Import library

import pandas as pd

# Read csv file

first_df = pd.read_csv("/content/Data-cleaning-for-beginners-using-pandas.csv")
df = first_df.copy()
df

# Converting column names into lower-case

df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" ", "_")
df

# Checking number of null values

df.isnull().sum()

# *Age Column*

# There are 7 null values in age column so, in order to handle it find average age i.e mean

# Mean
avg_age = df["age"].mean()
avg_age

# Filling the missing values with mean

df['age'] = df.age.fillna(avg_age)
df['age'] = df.age.round(decimals = 1)

# Converting float into integer

df['age'] = df['age'].astype(int)
df['age']

# *Rating Column*

# There is only 1 null value in rating column so, in order to handle it find mean

avg_rating = df['rating'].mean()
avg_rating

# Filling the missing value with mean

df['rating'] = df.rating.fillna(avg_rating)
df['rating'] = df.rating.round(decimals = 1)

# Handle negative rating by replacing -1.0 with 1.0

df['rating'] = df['rating'].replace(-1.0,1.0)
df['rating']

# *Salary Column*

# Omitting '$' and convering in thousand

df['salary'] = df['salary'].str.replace('$','')
df['salary'] = df['salary'].str.replace('k','000')
df['salary']

# Splitting salary by '-' into starting and ending salary

df[['starting_salary','ending_salary']] = df['salary'].str.split('-',expand = True)

# Deleting entire salary column
df = df.drop(columns= ['salary'])

# *Easy Apply Column*

# Replacing -1 with false

df['easy_apply'] = df['easy_apply'].replace('-1','FALSE')
df['easy_apply']

# *Established Column*

# Finding mean to replace -1

avg_est = df['established'].mean()
avg_est

# import library

import numpy as np

df['established'] = df['established'].replace(-1,np.nan)
df['established'] = df['established'].replace(np.nan,avg_est)

# Converting data type into integer

df['established'] = df['established'].astype(int)

df['established']

# *Location Column*

df['location'].unique()

df['location'] = df['location'].str.replace(" ",",")
df['location'] = df['location'].str.replace("New,","New ")

# Splitting location by ',' into country and country_ISO_code

df[['country','country_ISO_code']] = df['location'].str.split(",",expand = True)
df

# After splitting the location column into 2 separted column, delete location column

df = df.drop(columns = ['location'])

# Since there is default numbering so delete index column

df = df.drop(columns = ['index'])

# **Final output**

df
