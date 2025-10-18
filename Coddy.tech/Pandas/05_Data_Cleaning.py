'''
Remove Duplicate Values
Duplicate rows are exactly the same. If there is a single difference, it will not be considered a duplicate.

df = df.drop_duplicates()
Rename Columns
Usually, we would like to have a single convention for column names. For that, we can manually rename the columns:

df = df.rename(columns={"old_name": "new_name"})
Change Data Types
df["column name"] = df["column name"].astype(bool)
df["column name"] = df["column name"].astype(int)
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

Remove duplicate rows.
Rename all columns to lower-case letters.
Columns with ones and zeros (Investigate the dataframe to find the right columns.) convert to Boolean columns
To iterate over all columns, you can use the .colunms property:

for column in columns:
    # your code here
To track your progress, print the df:  print(df)

Store the final result in the df variable.
Don't print the df to pass the test case!
'''
import pandas as pd

df = pd.read_csv("./missing.csv")
df = df.drop_duplicates()
df.columns = df.columns.str.lower()
df["is_valid"] = df["is_valid"].astype(bool)
