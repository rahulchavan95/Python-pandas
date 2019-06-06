import pandas as pd
import matplotlib.pyplot as plt

excel_file='Sample_data.xlsx'
data=pd.read_excel(excel_file)

print("all data from excel file")
print(data)

print("first five rows from excel file")
print(data.head())


print("first three rows from excel file")
print(data.head(3))


print("last five rows from excel file")
print(data.tail())


print("last three rows from excel file")
print(data.tail(3))

print("rows and columns",data.shape)


sorted_data=data.sort_values(['Name'],ascending=True)
print("\nSorted Data\n")
print(sorted_data)


data['Age'].plot(kind="hist")
plt.show()

data['Age'].plot(kind="bar")
plt.show()
