import pandas as pd

data=[{'Name':'Rahul','RollNo':1,'Fees':1000},{'Name':'Akshay','RollNo':2,'Fees':2000},{'Name':'Mukesh','RollNo':3,'Fees':3000}]
df=pd.DataFrame(data)
print(df)

writer=pd.ExcelWriter('Pandas.xlsx',engine='xlsxwriter')

df.to_excel(writer,sheet_name='sheet1')

writer.save()
