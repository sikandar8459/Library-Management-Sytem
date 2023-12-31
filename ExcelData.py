# import pandas
import pandas as pd
import sqlite3

conn = sqlite3.connect("LibraryMS.db")
cur = conn.cursor()

cur.execute("select * from ProgrammingBooksDetails")
result = cur.fetchall()

# dataframe with Name and Age columns
df = pd.DataFrame(result)

# rankings_pd = pd.DataFrame(rankings) 
  
# Before renaming the columns 
# print(rankings_pd) 
  
# pd.rename(columns = {'test':'TEST'}, inplace = True) 
# create a Pandas Excel writer object using XlsxWriter as the engine
writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')

# write data to the excel sheet
df.to_excel(writer, sheet_name='Sheet1', index=False)


# print(df.index)
# RangeIndex(start=0, stop=3, step=1)
print(df.rename(index=str).index)
# Index(['0', '1', '2'], dtype='object')
# close file
writer.close()