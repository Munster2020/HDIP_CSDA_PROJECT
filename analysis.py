# importing dataset using pandas
# verifying the imported dataset
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

iris_df = pd.read_csv('iris.csv')
f = iris_df['sepal length in cm'].describe()
g = iris_df['sepal width in cm'].describe()
h = iris_df['petal length in cm'].describe()
i = iris_df['petal width in cm'].describe()
j = iris_df['class'].describe()

f.to_csv (r'C:\Users\bshor\Documents\HDIP_CSDA_PROJECT\iris_summary.csv', header=True)
print (f)
#print(f, g, h, i, j)

#savefile = open('iris_summary.txt','w')
#savefile.write(f)
#savefile.close()