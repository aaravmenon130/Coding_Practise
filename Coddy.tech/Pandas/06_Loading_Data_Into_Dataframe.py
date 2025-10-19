'''
Create a function named csv_convertor that accepts a file name, loads it into a dataframe, and finally prints the dataframe.

If the CSV file is empty, print "Empty file".
'''
import pandas as pd
def csv_convertor(filename):
    # Write code here
    
    try:
        df = pd.read_csv(filename)
        if df.empty:
            print('Empty file')
        else:
            print(df)
    except:
        print('Empty file')
