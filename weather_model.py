''' Імпортування бібліотек'''

import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

import matplotlib.pyplot as plt 
import seaborn as sns 

'''Кінець блоку шмпортування бібліотек'''





'''Очищення та підготовка датасету'''

df = pd.read_csv("weather_clasification_data.csv")   #відкриваю датасет для читання

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

print(df.info())   #вивід загальної інформації

'''Кінець блоку підготовки датасету'''





'''Підстановка данних'''

x = df.drop("Weather Type", axis=1)
y = df["Weather Type"]

x_train, x_test, y_train, y_test = train_test_split(x, y)    

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

'''Кінець підстановки'''





''' '''

knn = KNeighborsClassifier()
knn.fit(x_train, y_train)
y_pred_knn = knn.predict(x_test)
print(accuracy_score(y_test, y_pred_knn)*100)
print(confusion_matrix(y_test, y_pred_knn))

# tree = DecisionTreeClassifier()
# tree.fit(x_train, y_train)
# y_pred_tree = tree.predict(x_test)
# print(accuracy_score(y_test, y_pred_tree)*100)
# print(confusion_matrix(y_test, y_pred_tree))



# def plot_confusion_matrix(y_test, y_pred, classes, title):
#     cm = confusion_matrix(y_test ,y_pred)

#     accuracy =  accuracy_score(y_test, y_pred)*100

#     plt.figure(figsize=(8,6))
#     sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False, xticklabels=classes, yticklabels=classes)

#     plt.title(f'{title}\nТoчність: {accuracy:.2f}%')
#     plt.xlabel('Прогнозована погода')
#     plt.ylabel('Реальна погода')
#     plt.show()

# classes = ['Rainy', 'Cloudy', 'Sunny', 'Snowy']



# from sklearn.naive_bayes import GaussianNB

# gnb = GaussianNB()
# gnb.fit(x_train, y_train)
# y_pred_gnb = gnb.predict(x_test)
# print(accuracy_score(y_test, y_pred_gnb)*100)
# print(confusion_matrix(y_test, y_pred_gnb))



# from sklearn.ensemble import GradientBoostingClassifier

# gbc = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0,max_depth=5, random_state=0)
# gbc.fit(x_train, y_train)
# y_pred_gbc = gbc.predict(x_test)
# print(accuracy_score(y_test, y_pred_gbc)*100)
# print(confusion_matrix(y_test, y_pred_gbc))



# plot_confusion_matrix(y_test, y_pred_knn, classes, "KNN")
# plot_confusion_matrix(y_test, y_pred_tree, classes, "Decision tree")
# plot_confusion_matrix(y_test, y_pred_gnb, classes, "Naive Bayes")
# plot_confusion_matrix(y_test, y_pred_gbc, classes, "Gradient boosting")

# def plot_cm(y_test, y_pred, class_names, title, ax):
#     cm = confusion_matrix(y_test, y_pred)
#     accuracy = accuracy_score(y_test, y_pred) * 100

#     sns.heatmap(cm, annot=True, fmt='d', ax=ax, cmap='Reds', xticklabels=class_names, yticklabels=class_names)
#     ax.set_title(f'{title}\nТочність: {accuracy:.2f}%')

# fig, axes = plt.subplots(2, 2, figsize=(12,8))
# axes = axes.flatten()

# plot_cm(y_test, y_pred_knn, classes, 'KNN Confusion Matrix', axes[0])
# plot_cm(y_test, y_pred_tree, classes, 'Decision Tree Confusion Matrix', axes[1])
# plot_cm(y_test, y_pred_gnb, classes, 'Naive Bayes classifier Confusion Matrix', axes[2])
# plot_cm(y_test, y_pred_gbc, classes, 'Gradient boosting classifier Confusion Matrix', axes[3])

# plt.tight_layout()
# plt.show()
