'''

Usually, the CSV files contain missing data, incorrect column names, duplicates, incorrect values, and incorrect data types. The Pandas module has all the tools to handle these problems.

Missing Data
To find out if a value is missing or not:

df.isna()
To know how many missing values each column has:

df.isna().sum()
The isna() function converts all values to true or false (missing or not), then applies. sum() will treat true as 1 and false as 0.

To iterate over the columns and their number of missing values, use the items() method just like in a dictionary (although it is a Pandas series object):

for column, missing_num in df.isna().sum().items():
    print(column, missing_num)
To fill in all those missing values for the whole dataframe, use the fillna() method:

df = df.fillna("some value")
To fill in missing values only for a column, use the fillna() function over a column:

df["some_column"] = df["some_column"].fillna("some value")
There is also an option to remove all rows with missing values:

df = df.dropna()

'''
'''
The CSV file missing.csv is messy.

Here is the first 5 lines of the file:

ID,COUNTRY,COLOR,SKILL,SKILL_POINTS,UTILIZATION,IS_VALID
1,France,Signal violet,marksmanship,14,0.1924,1
1,France,Signal violet,marksmanship,14,0.1924,1
2,Solomon Islands,Pearl violet,,4,,1
3,Germany,,calligraphy,12,0.88646,0
Clean the data:

Fill the missing values of all columns with more than 2 missing values with the value Missing
Remove all of the rest of the rows that have missing values.
To see how you progress print the df: print(df)

Store the final result in the df variable.
Don't print the df to pass the test case!
'''
# pandas as pd is already imported
df = pd.read_csv("./missing.csv")
# Write your code below
for colname, num in df.isna().sum().items():
    if num > 2:
        df[colname] = df[colname].fillna('Missing')
df = df.dropna()
