# Created by: Brian Shortiss
# Created on: 01 April 2020

# Import modules required for the project.
# Matplotlib is a library for for creating static, animated or interactive visualisations.
# The Pandas library provides ease of use data structures and analysis tools.
# Seaborn is a a Python data visualiization library. It offers an interface for creating informative attractive statistical graphs.
# Sys, his module provides a number of functions and variables that can be used to manipulate different parts of the Python runtime environment.

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import pandas as pd
import seaborn as sns
import sys

# Reads the contents of 'iris.csv' dataset and create column headings
# See Readme for source and file description.
data = pd.read_csv('iris.csv')
iris_df = pd.DataFrame(data, columns=[
                       'sepal length in cm', 'sepal width in cm', 'petal length in cm', 'petal width in cm', 'class'])

# Output a summary of the dataset and each variable to text file called "Summary"

sys.stdout = open("iris_summary.txt", 'w')

# This section explores the dataset
print('===============')
print('First Five Rows')
print('---------------')
print(iris_df.head())
print('===============')
print('Last Five Rows')          
print('---------------')
print(iris_df.tail())
print('===============')
print('Species of Iris')
print('---------------')
print(iris_df['class'].value_counts())
print('==========================')
print('Information on the dataset')
print('--------------------------')
print(iris_df.info())

# The next section generates descriptive statistics on the dataset
print('===================================')
print('Statistical Summary of numeric data')
print('-----------------------------------')
print(iris_df.describe())
print('=======================================')
print('Statistical Summary of non-numeric data')
print('---------------------------------------')
print(iris_df.describe(include=[object]))
print('===============')
print('Dataset Median')
print('--------------')
print(iris_df.median())
print('===============')
print('Dataset Mode')
print('--------------')
print(iris_df.mode(numeric_only=True))
print('===============')
print('Dataset Variance')
print('--------------')
print(iris_df.var())
print('====================================')
print('Dataset Correlation Matrix Of Values')
print('------------------------------------')
print(iris_df.corr())
print('====================================')
print('Dataset Covariance Matrix Of Values')
print('------------------------------------')
print(iris_df.cov())
print('===============')

# The next stage of the project moves on to creating histograms and scatterplots
a = 'sepal length in cm'
b = 'sepal width in cm'
c = 'petal length in cm'
d = 'petal width in cm'
e = 'class'

# Creates a histogram of sepal length
sns.set_style('darkgrid')
plt.figure(figsize=(4.4,2.8))
sns.distplot(iris_df[a])
plt.title('Histogram of Sepal Length')
plt.xlabel('')
plt.ylabel('Frequency')
plt.savefig('histogram_of_sepal_length')
plt.close()

# Creates a histogram of sepal width
sns.set_style('darkgrid')
plt.figure(figsize=(4.4,2.8))
sns.distplot(iris_df[b])
plt.title('Histogram of Sepal Width')
plt.xlabel('')
plt.ylabel('Frequency')
plt.savefig('histogram_of_sepal_width')
plt.close()

# Creates a histogram of petal length
sns.set_style('darkgrid')
plt.figure(figsize=(4.4,2.8))
sns.distplot(iris_df[c])
plt.title('Histogram of Petal Length')
plt.xlabel('')
plt.ylabel('Frequency')
plt.savefig('histogram_of_petal_length')
plt.close()

# Creates a histogram of petal width
sns.set_style('darkgrid')
plt.figure(figsize=(4.4,2.8))
sns.distplot(iris_df[c])
plt.title('Histogram of Petal Width')
plt.xlabel('')
plt.ylabel('Frequency')
plt.savefig('histogram_of_petal_width')
plt.close()

# Create a pairplot of the dataset
sns.set_style('darkgrid')
sns.pairplot(iris_df, hue='class')
plt.savefig('iris dataset pairplot')
plt.close()

# Create scatterplots of the dataset
sns.set_style('darkgrid')
sns.scatterplot(x='sepal length in cm', y='sepal width in cm',
                data=iris_df, hue='class', style='class')
plt.title('Scatter plot between sepal length and sepal width')
plt.savefig('sepal scatterplot')
plt.close()

sns.set_style('darkgrid')
sns.scatterplot(x='petal length in cm', y='petal width in cm',
                data=iris_df, hue='class', style='class')
plt.title('Scatter plot between petal length and petal width')
plt.savefig('petal scatterplot')
plt.close()

# Create boxplot of the dataset
iris_long = pd.melt(iris_df, id_vars='class')
sns.set_style('darkgrid')
sns.boxplot(x='class', y='value', hue='variable', data=iris_long)
plt.title('Boxplot of Class Attributes')
plt.savefig('class boxplot')
plt.close()
