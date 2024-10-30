import numpy as np
import pandas as pd

def BirthYear(dataSet, N):
    dataSet['birth year'] = np.random.randint(1970, 2006, N)

    return dataSet

def Sex(dataSet, N):
    sexProbability = np.random.uniform(0.0, 1.0, N)
    for i in range(N):
        if sexProbability[i] > 0.5:
            dataSet['sex'].append('Мужской')
        else:
            dataSet['sex'].append('Женский')

    return dataSet

def Weight_Height(dataSet, N):
    for i in range(N):
        if dataSet['sex'][i] == 'Мужской':
            dataSet['weight'].append(abs(np.round(np.random.normal(83.3, 10), 1)))
            dataSet['height'].append(abs(np.round(np.random.normal(176, 20), 1)))
        else:
            dataSet['weight'].append(abs(np.round(np.random.normal(72.5, 7.5), 1)))
            dataSet['height'].append(abs(np.round(np.random.normal(163.7, 15), 1)))
    
    return dataSet

def Brand(dataSet, N):
    brandProbability = np.random.random(N)
    for i in range(N):
        if brandProbability[i] > 0.95:
            dataSet['brand'].append('Kia')
        elif brandProbability[i] > 0.85:
            dataSet['brand'].append('Renault')
        elif brandProbability[i] > 0.65:
            dataSet['brand'].append('Volksvagen')
        elif brandProbability[i] > 0.4:
            dataSet['brand'].append('Hyundai')
        else:
            dataSet['brand'].append('ВАЗ')

    return dataSet

def Class(dataSet, N):
    classProbability = np.random.random(N)
    for i in range(N):
        if classProbability[i] > 0.95:
            dataSet['class'].append('Престиж')
        elif classProbability[i] > 0.75:
            dataSet['class'].append('Средний')
        else:
            dataSet['class'].append('Эконом')

    return dataSet

def Credit(dataSet, N):
    dataSet['credit'] = abs(np.round(np.random.normal(loc= 150000, scale= 80000, size= N), 2))

    return dataSet

def Name(dataSet, N):
    manNames = ('Александр', 'Михаил', 'Максим', 'Лев', 'Марк', 'Артем', 'Иван', 'Матвей', 'Дмитрий', 'Даниил')
    manSurnames = ('Иванов', 'Смирнов', 'Кузнецов', 'Попов', 'Васильев', 'Петров', 'Соколов', 'Михайлов', 'Новиков', 'Федоров')

    womanNames = ('София', 'Анна', 'Мария', 'Ева', 'Виктория', 'Полина', 'Варвара', 'Алиса', 'Василиса', 'Александра')
    womanSurnames = ('Иванова', 'Смирнова', 'Кузнецова', 'Попова', 'Васильева', 'Петрова', 'Соколова', 'Михайлова', 'Новикова', 'Федорова')
    for i in range(N):
        if dataSet['sex'][i] == 'Мужской':
            #dataSet['name'].append(str(input("Введите мужское имя и фамилию: ")))
            dataSet['name'].append(manNames[np.random.randint(0, 9)] + ' ' + manSurnames[np.random.randint(0, 9)])
        else:
            #dataSet['name'].append(str(input("Введите женское имя и фамилию: ")))
            dataSet['name'].append(womanNames[np.random.randint(0, 9)] + ' ' + womanSurnames[np.random.randint(0, 9)])

    return dataSet