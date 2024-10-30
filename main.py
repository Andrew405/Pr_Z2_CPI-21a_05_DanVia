import pandas as pd
import module1 as mod

N = 10

dataSet = {'name': [],
      'birth year': [],
      'sex': [],
      'weight': [],
      'height': [],
      'brand': [],
      'class': [],
      'credit': []}

dataSet = mod.BirthYear(dataSet, N)
dataSet = mod.Sex(dataSet, N)
dataSet = mod.Weight_Height(dataSet, N)
dataSet = mod.Brand(dataSet, N)
dataSet = mod.Class(dataSet, N)
dataSet = mod.Credit(dataSet, N)
dataSet = mod.Name(dataSet, N)

df = pd.DataFrame(dataSet)
print(df)