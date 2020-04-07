# Created by: Brian Shortiss
# Created on: 01 April 2020

# Import modules required for the project
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import pandas as pd
import sys
import io

# Reads the contents of 'iris.csv' dataset
iris_df = pd.read_csv('iris.csv')

# Verify the features are of which datatypes
label = "Iris Dataset Information \n "
d = iris_df.info()
buffer = io.StringIO()
iris_df.info(buf=buffer)
s = buffer.getvalue()

# Check for null values
label2 = "Iris Dataset Null Values \n "
e = iris_df.isnull().sum()

# View some basic statistical details like percentile, mean, std etc.
# of the data frame
f = iris_df['sepal length in cm'].describe()
g = iris_df['sepal width in cm'].describe()
h = iris_df['petal length in cm'].describe()
i = iris_df['petal width in cm'].describe()
j = iris_df['class'].describe()

# Output a summary of each variable to text file
filename = open("iris_summary.txt", 'w')
sys.stdout = filename
print(label,s,label2,d, e, f, g, h, i, j)

# k=f
#num_bins = 5
#n, bins, patches = plt.hist(k, num_bins, facecolor='blue', alpha=0.5)
# plt.show()
