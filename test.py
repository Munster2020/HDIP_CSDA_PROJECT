import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import pandas as pd
import seaborn as sns
import sys

data = pd.read_csv('iris.csv')

iris_df = pd.DataFrame(data, columns = ['sepal length in cm', 'sepal width in cm', 'petal length in cm', 'petal width in cm', 'class'])

print (iris_df)

(iris_df.describe(include=[object]))

print (iris_df)