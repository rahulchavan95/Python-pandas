import pandas as pd


df=pd.DataFrame()
print(df)

print("dataframe with list")
data=[1,2,3,4,5]
df=pd.DataFrame(data)

print(df)

print("dataframe with list")
data=[['rahul',1],['akshay',2],['mukesh',3],['sachin',4]]
df=pd.DataFrame(data,columns=['Name','RollNo'])
print(df)


data={'Name':['rahul','akshay','mukesh','sachin'],'RollNo':[1,2,3,4]}
df=pd.DataFrame(data)
print(df)


d={'one':pd.Series([1,2,3],index=['a','b','c']),'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
df=pd.DataFrame(d)
print(df)

print(df['one'])

