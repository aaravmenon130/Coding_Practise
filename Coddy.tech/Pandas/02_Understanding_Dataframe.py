'''
head(n): Shows the first n rows
head(): Shows the first 5 rows
describe(): Provide descriptive statistics such as mean, max, min, etc.
info(): Gives a summary of all features (columns).
shape:the shape of the dataframe (how many rows and how many columns). This is a property and not a method.
tail(n): Show the last n rows
tail(): Shows the first 5 rows
'''

'''
In this challenge, you have a CSV file called brands.csv.
Before doing anything, use the .read_csv() to transform the file into a dataframe.
Create a function named information that accepts a string that can hold one of the following values:

"head"
"describe"
"info"
"shape"
"tail"
The function will print the corresponding output of the dataframe.
'''

import pandas as pd
def information(action):
    df = pd.read_csv("brands.csv")
    if action == 'head':
        print(df.head())
    elif action == 'describe':
        print(df.describe())
    elif action == 'info':
        print(df.info())
    elif action == 'shape':
        print(df.shape)
    else:
        print(df.tail())
