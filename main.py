import pandas as pd
import module1 as mod
import shutil
import csv
import numpy as np
import module2 as mody

N = 30

dataSet = {'name': [],
      'birth_year': [],
      'sex': [],
      'weight': [],
      'height': [],
      'brand': [],
      'clas': [],
      'credit': []}

dataSet = mod.BirthYear(dataSet, N)
dataSet = mod.Sex(dataSet, N)
dataSet = mod.Weight_Height(dataSet, N)
dataSet = mod.Brand(dataSet, N)
dataSet = mod.Clas(dataSet, N)
dataSet = mod.Credit(dataSet, N)
dataSet = mod.Name(dataSet, N)

df = pd.DataFrame(dataSet)
print(df)
print(' ')

#2.1
df.to_csv('auto.csv', index= False, header= False, sep= ";", encoding='UTF-8')
df.to_excel('auto.xlsx', index= False, header= False)
shutil.copyfile('auto.csv', 'auto_work.csv') # 2.1 дубль

temp_a = ['birth_year', 'weight', 'height', 'credit']
for i in temp_a:
      df = df.sort_values(i, ascending= False)
      print(df)
      print(' ')


## НЕ УДАЛЯТЬ
# df = df.sort_values('weight', ascending= False)
# print(df)
# print(' ')

# df = df.sort_values('height', ascending= False)
# print(df)
# print(' ')

# df = df.sort_values('credit', ascending= False)
# print(df)
# print(' ')

df = df.sort_index()
manAuto = df[df['sex'] == 'Мужской']
womanAuto = df[df['sex'] == 'Женский']

print(manAuto)
print(' ')
print(womanAuto)
print(' ')
print(df.loc[3])
print(' ')

dfset = set(df.loc[5])
print(dfset)
print(' ')
print("2.2")

brand_dict = {"Hyundai" : [],
              "Kia" : [],
              "ВАЗ" : [],
              "Volksvagen" : [],
              "Renault" : []
              }
brand_list = ["Hyundai", "Kia", "ВАЗ", "Volksvagen", "Renault" ]

class_dict = {"Эконом" : [],
              "Средний" : [],
              "Престиж" : []
              }
class_list = ["Средний", "Эконом", "Престиж" ]
for i in range(N):
      temp_a = list()
      for n in range(len(brand_list)):
            temp = tuple(df.loc[i])
            if temp[5] ==  brand_list[n]:
                  temp_a.append(temp)
                  if temp_a not in brand_dict[brand_list[n]]:
                        brand_dict[brand_list[n]] += temp_a


print("name        birth_year sex  weight height brand  class  credit")
#Вывод 2.2.1.2
for n in range(len(brand_list)):
      print(f"-{brand_list[n]}------------------------------------------------------------------")
      mody.sort_brand_export(brand_dict, brand_list[n])

print('')

for i in range(N):
      temp_a = list()
      
      for n in range(len(class_list)):
            temp = tuple(df.loc[i])
            
            if temp[6] ==  class_list[n]:
                  temp_a.append(temp)
                 
                  if temp_a not in class_dict[class_list[n]]:
                        class_dict[class_list[n]] += temp_a

print("name        birth_year sex  weight height brand  class  credit")

for m in range(len(class_list)):
      print("-" + class_list[m] + "------------------------------------------------------------------")
      mody.sort_brand_export(class_dict, class_list[m])

print(' ')

class_brand = {
      "Эконом Hyundai" : [],
      "Средний Hyundai" : [],
      "Престиж Hyundai" : [],
      "Эконом Kia" : [],
      "Средний Kia" : [],
      "Престиж Kia" : [],
      "Эконом ВАЗ" : [],
      "Средний ВАЗ" : [],
      "Престиж ВАЗ" : [],
      "Эконом Volksvagen"  : [],
      "Средний Volksvagen" : [],
      "Престиж Volksvagen" : [],
      "Эконом Renault" : [],
      "Средний Renault" : [],
      "Престиж Renault" : []
}

for i in range(N):
      for m in range(len(class_list)):
            temp_a = list()
            
            for n in range(len(brand_list)):
                  temp = tuple(df.loc[i])
                  
                  if temp[5] ==  brand_list[n] and temp[6] == class_list[m]:
                                    temp_a.append(temp)
                                    
                                    if temp_a not in class_brand[str(class_list[m] + " " + brand_list[n])]:
                                          class_brand[str(class_list[m] + " " + brand_list[n])] += temp_a
#Вывод 2.2.2
print("name        birth_year sex  weight height brand  class  credit")
for m in range(len(class_list)):
      for n in range(len(brand_list)):
            print("-" + class_list[m] +" " + brand_list[n] + "------------------------------------------------------------------")
            mody.sort_brand_export(class_brand, str(class_list[m] + " " + brand_list[n]))

#2.3
print(' ')
print('2.3 ')
sort_ref = [ 'возрасту', 'полу','весу', 'росту' ]

for n in brand_dict:
      q=1
      for m in range(4):
            print("Сортировка " + n + " по " + sort_ref[m]  +" --------------------------")
            m +=1
            brand_dict[n] = sorted(brand_dict[n], key = lambda x: x[q]  )
            q+=1
            for s in brand_dict[n]:
                  mody.nice_export(s)
