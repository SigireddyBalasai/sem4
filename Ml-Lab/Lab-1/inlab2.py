import numpy as np
import pandas as pd
data = np.array([[1,2,3],[4,5,6],[7,8,9]])
dataframe = pd.DataFrame(data)
print("The dataframe that we had created is ")
print(dataframe)
row = int(input("Please enter tghe row to be accessed"))
print(dataframe[row][:])
column = int(input("Please entert the column to be accessed"))
print(dataframe[:][column])
row,column  = list(map(int , input("Please enter the element indexes").split()))
print(dataframe[row][column])

