import numpy as np
import pandas as pd

N = 10

def dfGenerate(N):
    df = {#'name': [],
          'birth year': [],
          'sex': [],
          'weight': [],
          'height': [],
          'brand': [],
          'class': [],
          'credit': []}
    
    df['birth year'] = np.random.randint(1970, 2006, N)

    sexProbability = np.random.uniform(0.0, 1.0, N)
    for i in range(N):
        if sexProbability[i] > 0.5:
            df['sex'].append('Мужской')
        else:
            df['sex'].append('Женский')

    for i in range(N):
        if df['sex'][i] == 'Мужской':
            df['weight'].append(np.round(np.random.normal(83.3, 10), 1))
            df['height'].append(np.round(np.random.normal(176, 20), 1))
        else:
            df['weight'].append(np.round(np.random.normal(72.5, 7.5), 1))
            df['height'].append(np.round(np.random.normal(163.7, 15), 1))

    brandProbability = np.random.random(N)
    for i in range(N):
        if brandProbability[i] > 0.95:
            df['brand'].append('Kia')
        elif brandProbability[i] > 0.85:
            df['brand'].append('Renault')
        elif brandProbability[i] > 0.65:
            df['brand'].append('Volksvagen')
        elif brandProbability[i] > 0.4:
            df['brand'].append('Hyundai')
        else:
            df['brand'].append('ВАЗ')

    classProbability = np.random.random(N)
    for i in range(N):
        if classProbability[i] > 0.95:
            df['class'].append('Престиж')
        elif classProbability[i] > 0.75:
            df['class'].append('Средний')
        else:
            df['class'].append('Эконом')

    df['credit'] = np.round(np.random.normal(loc= 150000, scale= 80000, size= N), 2)

    return df

print(pd.DataFrame(dfGenerate(N)))