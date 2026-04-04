''' Імпортування бібліотек'''

import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
import os


from sklearn.metrics import accuracy_score

import matplotlib.pyplot as plt 
import seaborn as sns 

'''Кінець блоку імпортування бібліотек'''




def train_model():
    '''Очищення та підготовка датасету'''
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), "weather_clasification_data.csv"))   #відкриваю датасет для читання

    df.drop(["Visibility (km)"], axis=1, inplace=True)  #видалення непотрібних колонок
    df.drop(["UV Index"], axis=1, inplace=True)

    def transform_cloudy(row):
        if row == "overcast":
            return 1
        elif row == "partly cloud":
            return 2
        elif row == "clear":
            return 3
        return 4

    def transform_season(row):
        if row == "Winter":
            return 1
        elif row == "Spring":
            return 2
        elif row == "Autumn":
            return 3
        return 4

    def transform_location(row):
        if row == "inland":
            return 1
        elif row == "mountain":
            return 2
        return 3

    def transform_type(row):
        if row == "Rainy":
            return 1
        elif row == "Cloudy":
            return 2
        elif row == "Sunny":
            return 3
        return 4

    df["Cloud Cover"] = df["Cloud Cover"].apply(transform_cloudy)   #застосовую функції
    df["Season"] = df["Season"].apply(transform_season)
    df["Location"] = df["Location"].apply(transform_location)
    df["Weather Type"] = df["Weather Type"].apply(transform_type)

    '''Кінець блоку підготовки датасету'''

    x = df.drop("Weather Type", axis=1)   #'''Підстановка данних'''
    y = df["Weather Type"]

    x_train, x_test, y_train, y_test = train_test_split(x, y)    
    sc = StandardScaler()
    x = sc.fit_transform(x)
    

    model_knn = KNeighborsClassifier()
    model_knn.fit(x, y)
    
    return model_knn, sc
