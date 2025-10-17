'''
After loading the data into a dataframe, you can access specific data in several ways. To select a column, use brackets and the column name:

column = df['column_name']
The variable column will hold a series. (Remember that every column is a series object?)

To select a row, use the loc or iloc functions. For example:

df.iloc[0] df.loc[0]
Both will return to the first row. We will learn about their differences later in this course.

To fetch a specific cell of the dataframe, add one more number to the iloc (loc does not support this feature). iloc stands for index loc. 

df.iloc[0,1]
This will return row = 0, and column = 1 cell.
'''

'''
Create a function named specific_returner that accepts a filename and a string that represents an index or a column name (if it is an index, convert it to an integer).
If it is an index, return that corresponding row, and if it is a column name, return the corresponding column.
'''
import pandas as pd
def specific_returner(file_name, value):
    p = pd.read_csv(file_name)
    try:
        value = int(value)
        return p.iloc[value]
    except:
        return p[value]
    # Write code here
