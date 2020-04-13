# Created by: Brian Shortiss
# Created on: 01 April 2020

# Import modules required for the project.
# Matplotlib is a library for for creating static, animated or interactive visualisations.
# Numpy library adds support  for large, multi-dimensional arrays and matrices as well as mathematical functions.
# The Pandas library provides ease of use data structures and analysis tools.
# Seaborn is a a Python data visualiization library. It offers an interface for creating informative attractive statistical graphs.
# Sys, his module provides a number of functions and variables that can be used to manipulate different parts of the Python runtime environment.


import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import pandas as pd
import seaborn as sns
import sys

# Reads the contents of 'iris.csv' dataset
# See Readme for source and file description.
iris_df = pd.read_csv('iris.csv')

# Output a summary of the dataset and each variable to text file called "Summary"
sys.stdout = open("iris_summary.txt", 'w')


print ('===============')
print ('First Five Rows')
print (iris_df.head())
print ('===============')
print ('Information on the dataset')
print (iris_df.info())
print ('=============')
print ('Statistical Summary of the dataset')
print (iris_df.describe())
print ('===============')


# The next stage of the project moves on to creating histograms and scattareplots
a = 'sepal length in cm'
b = 'sepal width in cm'
c = 'petal length in cm'
d = 'petal width in cm'

# Creates a histogram of sepal length
sns.set_style('darkgrid')
sns.distplot(iris_df[a])
plt.title('Histogram of Sepal Length')
plt.xlabel('')
plt.ylabel('Frequency')
plt.savefig('histogram_of_sepal_length')
plt.close()

# Creates a histogram of sepal width
sns.set_style('darkgrid')
sns.distplot(iris_df[b])
plt.title('Histogram of Sepal Width')
plt.xlabel('')
plt.ylabel('Frequency')
plt.savefig('histogram_of_sepal_width')
plt.close()

# Creates a histogram of petal length
sns.set_style('darkgrid')
sns.distplot(iris_df[c])
plt.title('Histogram of Petal Length')
plt.xlabel('')
plt.ylabel('Frequency')
plt.savefig('histogram_of_petal_length')
plt.close()

# Creates a histogram of petal width
sns.set_style('darkgrid')
sns.distplot(iris_df[c])
plt.title('Histogram of Petal Width')
plt.xlabel('')
plt.ylabel('Frequency')
plt.savefig('histogram_of_petal_width')
plt.close()



#plt.savefig('sepal length in cm')
#sns.pairplot(iris_df, hue='class')

# plt.show()

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
