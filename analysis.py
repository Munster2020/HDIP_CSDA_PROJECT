# importing dataset using pandas
# verifying the imported dataset

import pandas as pd
# names = ['sepal length','sepal width','petal length','petal width','class'])
dataset = pd.read_csv('iris.csv')
dataset.describe()
print (dataset.shape)
