# Created by: Brian Shortiss
# Created on: 01 April 2020

# Import modules required for the project.
# Matplotlib is a library for for creating static, animated or interactive visualisations.
# Numpy library adds support  for large, multi-dimensional arrays and matrices as well as mathematical functions.
# The Pandas library provides ease of use data structures and analysis tools.
# Seaborn is a a Python data visualiization library. It offers an interface for creating informative attractive statistical graphs.

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import pandas as pd
import seaborn as sns
import sys # Allows the use of stdout to output a summary of each variable to a text file.

# Output a summary of the dataset and each variable to text file called "Summary"
summary = open("iris_summary.txt", 'w')
sys.stdout = summary

# Reads the contents of 'iris.csv' dataset
# See Readme for source and file description.
iris_df = pd.read_csv('iris.csv')

# Data exploration. This step is to have a quick view of the data before continuing.  
data = iris_df.head()
print (data)

# This step checks if there is any missing values. It also displays information about the dataframe 
# including index dtype and column dtypes, non-null valuesand memory usage.
datatypes = iris_df.info()
print (datatypes)

# View the classification of flowers
species = iris_df['class'].value_counts()
print (species)

# View some basic statistical details like percentile, mean, std etc. of the data frame
f = iris_df['sepal length in cm'].describe()
g = iris_df['sepal width in cm'].describe()
h = iris_df['petal length in cm'].describe()
i = iris_df['petal width in cm'].describe()
j = iris_df['class'].describe()

print (f,g,h,i,j)

# Creates a histogram of sepal length
sns.distplot( iris_df['sepal length in cm'] )
plt.show()



'''
iris_df.describe().plot(kind='area', fontsize=27, figsize = (20,8), table = True,colormap='rainbow')
plt.xlabel ('Statistics' ,)
plt.ylabel ('Value')
plt.title ('General Statistics of Iris Dataset')
plt.show()
# k=f
#num_bins = 5
#n, bins, patches = plt.hist(k, num_bins, facecolor='blue', alpha=0.5)
# plt.show()
'''