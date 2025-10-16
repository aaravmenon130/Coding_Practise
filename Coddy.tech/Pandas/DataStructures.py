'''
A series in Pandas is like a one-dimensional array that holds any data type. 
For example, a series could be a list of integers [4, 3, 8, 5]

import pandas as pd
temp = pd.Series([1, 2, ,3])

data = [{"col1": 22000,'col2': 1500.0},
        {"col1": 25000,'col2': 3000.0},
        {"col1": 23000,'col2': 2500.0}]
df = pd.DataFrame(data)
'''
#Create a function named dataframe_creator that receives data, creates a dataframe from the data, and finally prints the dataframe.
import pandas as pd
def dataframe_creator(data):
    df = pd.DataFrame(data)
    print(df)
