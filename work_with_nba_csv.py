'''
www.geeksforgeeks.org/python-extracting-rows-using-pandas-iloc/
www.geeksforgeeks.org/different-ways-to-import-csv-file-in-pandas/
'''

import pandas as pd
import pprint as pp
# making data frame
df = pd.read_csv("nba.csv")
print('all df\n',df,'\n')

print('df.head(10)\n',df.head(10),'\n')

# www.geeksforgeeks.org/python-extracting-rows-using-pandas-iloc/
print('df.iloc[3:8]\n',df.iloc[3:8])
