import pandas as pd
import module1 as mod

N = 30

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
print(' ')

df.to_csv('auto.csv', index= False, header= False, sep= ";")
df.to_excel('auto.xlsx', index= False, header= False)

df = df.sort_values('birth year', ascending= False)
print(df)
print(' ')

df = df.sort_values('weight', ascending= False)
print(df)
print(' ')

df = df.sort_values('height', ascending= False)
print(df)
print(' ')

df = df.sort_values('weight', ascending= False)
print(df)
print(' ')

df = df.sort_index()
manAuto = df[df['sex'] == 'Мужской']
womanAuto = df[df['sex'] == 'Женский']

print(manAuto)
print(' ')
print(womanAuto)
print(' ')
print(df.loc[3])