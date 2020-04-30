![GMIT Logo](https://github.com/Munster2020/HDIP_CSDA_PROJECT/blob/master/GMIT_Logo.jpg)
## Higher Diploma in Science in Computing (Data Analytics)
## Programming and Scripting (COMP08049) 
## Project 2020 – Fisher’s Iris Data Set


### Problem Statement
This project deals with Fisher's Iris data set. For the project I had to research the data set and write documentation and code in Python to investigate it.

I used descriptive statistics to answer this problem. This method uses two approaches. Firstly, using quantitative statistics to describe and summarise the data numerically and secondly use visual interpretation to illustrate the data with charts, plots and histograms.

### Summary
The Iris flower data set was compiled by Ronald Fisher in the 1930's. Fisher was born in London in 1890 and went on to become one of the most highly regarded statisticians of the 20th Century. He pioneered the application of statistical procedures to the design of scientific experiments. In tandem with his work in statistics he was also one of the principal founders of population eugenics. His work in biology led to the geneticist and author Richard Dawkins calling him the greatest biologist since Charles Darwin.

Fisher introduced the Iris Flower data set in a paper published in "The Annals of Human Genetics" in 1936 called "The Use of Multiple Measurements in Taxonomic Problems" as an example of linear discriminant analysis. The dataset contains three classes of fifty instances each. Each class refers to a type of iris plant. Each class is linearly separable from the other two classes. The first two species Iris setosa and Iris versicolour, were found growing together in the same colony. The third species called Iris virginica was taken from a different colony.

The data set contains the following attributes.

(1) sepal length in cms

(2) sepal width in cms

(3) petal length in cms

(4) petal width in cms

(5) class:

   * Iris setosa
    
   * Iris versicolour
    
   * Iris virginica

### Software
Below is a list of the software I used for the project.

![logo](https://github.com/Munster2020/HDIP_CSDA_PROJECT/blob/master/Visual%20Studio%20Code.png "Visual Studio Code")  ![Visual Studio Code](https://code.visualstudio.com/)
is a source-code editor developed by Microsoft for Windows, Linux and macOS. It includes embedded Git and support for debugging, syntax highlighting, intelligent code completion, snippets, and code refactoring. It is highly customizable, allowing users to change the theme, keyboard shortcuts, preferences, and install extensions that add additional functionality. The source code is free and open-source, released under the permissive MIT License. The compiled binaries are freeware for any use. (Source:Wikipedia)

![logo](https://github.com/Munster2020/HDIP_CSDA_PROJECT/blob/master/Anaconda.png "Anacondas")
![Anacondas](https://www.anaconda.com/)
is a free and open-source distribution of the Python and R programming languages for scientific computing (data science, machine learning applications, large-scale data processing, predictive analytics, etc.), that aims to simplify package management and deployment. The distribution includes data-science packages suitable for Windows, Linux, and macOS. (Source:Wikipedia)

![logo](https://github.com/Munster2020/HDIP_CSDA_PROJECT/blob/master/cmdr.png "Cmder")
![Cmdr](https://cmder.net/)
provides you with an alternative to the Windows default command prompt utility through a more capable console emulator that also comes packing a good-looking graphical user interface. (Source:downloads.com)
  
### Python Code
### 1. Import modules
The first section of my code imports the modules I required for the project.
[Matplotlib](https://matplotlib.org/) is a library for creating static, animated or interactive visualisations while the [Pandas](https://pandas.pydata.org/) library provides ease of use data structures and analysis tools.
[Seaborn](http://seaborn.pydata.org/) is a Python data visualization library which I used for creating statistical graphs.
The [Sys](https://www.python-course.eu/sys_module.php) module provides a number of functions and variables that can be used to manipulate different parts of the Python runtime environment. I used it in this program to output to a .txt file.
```python
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import pandas as pd
import seaborn as sns
import sys
```
---
### 2. Create dataframe
Next I loaded the data using a pandas dataframe and created column headings. I sourced the dataset from the UCI Machine Learning Repository via [MITOpenCourseWare](https://ocw.mit.edu/courses/sloan-school-of-management/15-097-prediction-machine-learning-and-statistics-spring-2012/datasets/)
```python
iris_df = pd.read_csv('iris.csv')
iris_df = pd.DataFrame(data, columns = ['sepal length in cm', 'sepal width in cm', 
'petal length in cm', 'petal width in cm', 'class'])
```
---
### 3. Redirect to text file
For this project we were asked to output our findings to a text file. In order to do this, I used the below piece of code which uses the Sys module mentioned previously.
```python
sys.stdout = open("iris_summary.txt", 'w')
```
---
### 4. Data exploration
Having obtained the data, the next step was to perform some exploratory data analysis. Looking in more detail at the dataset attributes, classifications of Iris plant and datatypes. The code below confirmed a relatively small dataset with only 150 records (50 in each class) namely Iris Setosa, Iris Versicolour and Iris Virginica. There is four numeric predictive attributes (float64) and the class (object). There are no missing values. 
#### 4.1 pandas.DataFrame.head
[DataFrame.head](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html) This function returns the first n rows for the object based on position. It is useful for quickly testing if your object has the right type of data in it.
```python
print('===============')
print('First Five Rows')
print('---------------')
print(iris_df.head())
```
The head function with no arguments gets the first five rows of data.
```
===============
First Five Rows
---------------
   sepal length in cm  sepal width in cm  petal length in cm  petal width in cm        class
0                 5.1                3.5                 1.4                0.2  Iris-setosa
1                 4.9                3.0                 1.4                0.2  Iris-setosa
2                 4.7                3.2                 1.3                0.2  Iris-setosa
3                 4.6                3.1                 1.5                0.2  Iris-setosa
4                 5.0                3.6                 1.4                0.2  Iris-setosa
```
#### 4.2 pandas.DataFrame.tail
[DataFrame.tail](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.tail.html) This function returns last n rows from the object based on position. It is useful for quickly verifying data, for example, after sorting or appending rows.

```python
print('===============')
print('Last Five Rows')
print('---------------')
print(iris_df.tail())
```
The tail function with no arguments gets the last five rows of data.
```
===============
Last Five Rows
---------------
     sepal length in cm  sepal width in cm  petal length in cm  petal width in cm           class
145                 6.7                3.0                 5.2                2.3  Iris-virginica
146                 6.3                2.5                 5.0                1.9  Iris-virginica
147                 6.5                3.0                 5.2                2.0  Iris-virginica
148                 6.2                3.4                 5.4                2.3  Iris-virginica
149                 5.9                3.0                 5.1                1.8  Iris-virginica
```
#### 4.3 pandas.DataFrame.value_counts
The [DataFrame.value_counts](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html) returns the object in descending order so that the first element is the most frequently-occurring element. Excludes NA values by default.
```python
print('===============')
print('Species of Iris')
print('---------------')
print(iris_df['class'].value_counts())
```
This code shows that all three classes are disributed equally in terms of numbers and indicates a balanced dataset. 
```
===============
Species of Iris
---------------
Iris-setosa        50
Iris-virginica     50
Iris-versicolor    50
Name: class, dtype: int64
```
#### 4.4 pandas.DataFrame.info
[DataFrame.info](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.info.html) prints information about a DataFrame including the index dtype and column dtypes, non-null values and memory usage.
```python
print('===============')
print('Information on the dataset')
print('--------------------------')
print(iris_df.info())
```
This block of code generates the results below. From this we can tell that no data points are missing in any attribute. That the first four attributes are of float64 type and the indexes are in the range 0-149 for 150 records. (Used by Pandas.) The last column is an object type used in class labels. 6KB's of memory is used by the datset. [Kumar.P: Exploratory Data Analysis: Iris Flower Dataset](https://medium.com/analytics-vidhya/exploratory-data-analysis-iris-flower-dataset-a21c368a1f4)
```
==========================
Information on the dataset
--------------------------
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns):
sepal length in cm    150 non-null float64
sepal width in cm     150 non-null float64
petal length in cm    150 non-null float64
petal width in cm     150 non-null float64
class                 150 non-null object
dtypes: float64(4), object(1)
memory usage: 6.0+ KB
None
```
---
### 5. Summary statistics 
Next up was to examine the dataset using some of the built-in functionality of Pandas. First, I used describe() to generate some descriptive statistics of the numeric and non-numeric datatypes, focusing on the central tendency, dispersion and shape of the dataset distribution. I also looked in more detail at the median, mode and variance as well as correlation and covariance.

#### 5.1 pandas.DataFrame.describe
[DataFrame.describe](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html) produces descriptive statistics that include summaries of the central tendency, dispersion and shape of a dataset’s distribution, excluding NaN values.
```python
print ('===================================')
print ('Statistical Summary of numeric data')
print ('-----------------------------------')
print (iris_df.describe())
print('=======================================')
print('Statistical Summary of non-numeric data')
print('---------------------------------------')
print(iris_df.describe(include=[object]))
```
From the analysis generated below it is possible to observe that petal length with a mean value of 3.758667, the variance (spread of distribution) is large at 3.113179. See 5.4 below. This would help explain why our scatterplot of petal length and width are well defined with little overlap between the three species See 6.2. [Hoey, Patrick.S: Statistical Analysis of the Iris Flower Dataset](http://patrickhoey.com/downloads/Computer_Science/03_Patrick_Hoey_Data_Visualization_Dataset_paper.pdf)
```
===================================
Statistical Summary of numeric data
-----------------------------------
       sepal length in cm  sepal width in cm  petal length in cm  petal width in cm
count          150.000000         150.000000          150.000000         150.000000
mean             5.843333           3.054000            3.758667           1.198667
std              0.828066           0.433594            1.764420           0.763161
min              4.300000           2.000000            1.000000           0.100000
25%              5.100000           2.800000            1.600000           0.300000
50%              5.800000           3.000000            4.350000           1.300000
75%              6.400000           3.300000            5.100000           1.800000
max              7.900000           4.400000            6.900000           2.500000

=======================================
Statistical Summary of non-numeric data
---------------------------------------
              class
count           150
unique            3
top     Iris-setosa
freq             50

```
#### 5.2 pandas.DataFrame.median
The [DataFrame.median](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.median.html) returns the median of the values for the requested axis in this case the four numeric attributes. 
```python
print ('===============')
print ('Dataset Median')
print ('--------------')
print (iris_df.median())
```
```
===============
Dataset Median
---------------
sepal length in cm    5.80
sepal width in cm     3.00
petal length in cm    4.35
petal width in cm     1.30
dtype: float64
```
#### 5.3 pandas.DataFrame.mode
[DataFrame.mode](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mode.html) returns a set of values that appears most often. It can be multiple values.

```python
print ('===============')
print ('Dataset Mode')
print ('--------------')
print (iris_df.mode(numeric_only=True))
```
```
===============
Dataset Mode
--------------
   sepal length in cm  sepal width in cm  petal length in cm  petal width in cm
0                 5.0                3.0                 1.5                0.2
```
#### 5.4 pandas.DataFrame.var
[DataFrame.var](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.var.html) returns unbiased variance over requested axis.
```python
print ('===============')
print ('Dataset Variance')
print ('--------------')
print (iris_df.var())
```
```
===============
Dataset Variance
--------------
sepal length in cm    0.685694
sepal width in cm     0.188004
petal length in cm    3.113179
petal width in cm     0.582414
dtype: float64
```
#### 5.5 pandas.DataFrame.corr
[DataFrame.corr](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.corr.html) computes pairwise correlation of columns, excluding NA/null values.
```python
print ('====================================')
print ('Dataset Correlation Matrix Of Values')
print ('------------------------------------')
print (iris_df.corr())
```
```
====================================
Dataset Correlation Matrix Of Values
------------------------------------
                    sepal length in cm  sepal width in cm  petal length in cm  petal width in cm
sepal length in cm            1.000000          -0.109369            0.871754           0.817954
sepal width in cm            -0.109369           1.000000           -0.420516          -0.356544
petal length in cm            0.871754          -0.420516            1.000000           0.962757
petal width in cm             0.817954          -0.356544            0.962757           1.000000
```
#### 5.6 pandas.DataFrame.cov
[DataFrame.cov](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.cov.html) computes the pairwise covariance among the series of a DataFrame. The returned data frame is the covariance matrix of the columns of the DataFrame.
```python
print ('====================================')
print ('Dataset Covariance Matrix Of Values')
print ('------------------------------------')
print (iris_df.cov())
```
```
====================================
Dataset Covariance Matrix Of Values
------------------------------------
                    sepal length in cm  sepal width in cm  petal length in cm  petal width in cm
sepal length in cm            0.685694          -0.039268            1.273682           0.516904
sepal width in cm            -0.039268           0.188004           -0.321713          -0.117981
petal length in cm            1.273682          -0.321713            3.113179           1.296387
petal width in cm             0.516904          -0.117981            1.296387           0.582414
```
---
### 6. Visual interpretation
#### 6.1 Histograms
After gathering some descriptions and summaries of the dataset the next section of code looks at interpreting the data visually.
First, I created histograms to look at each of the numeric attributes’ sepal length and width and petal length and width. Histograms provide a visual interpretation of numerical data by indicating the number of data points that lie within a range of values. These ranges of values are called classes or bins. The frequency of the data that falls in each class is depicted by the use of a bar. The higher that the bar is, the greater the frequency of data values in that bin.

```python
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
```
One of the key elements when analysing a histogram is it's shape. The number of peaks in the histogram determines whether it is classed as Unimodal, Bimodal or Multimodal. They can be further classified by looking at their symmetry [Murphy.P :Introductory Statistics for Science, Social Science, Business & Medicine](http://www.ucd.ie/statdept/classpages/stat_10010.html). From the histograms generated using the code above it's apparent that sepal width is symmetrical. This is evidenced by the descriptive statistics we carried out earlier. This showed that sepal width has a mean of 3.05, a median of 3.00 and a mode of 3.00. See 6.1.2 Histogram of Sepal Width.

##### 6.1.1 Histogram of Sepal Length
![Histogram of Sepal Length](https://github.com/Munster2020/HDIP_CSDA_PROJECT/blob/master/histogram_of_sepal_length.png)

##### 6.1.2 Histogram of Sepal Width
![Histogram of Sepal Width](https://github.com/Munster2020/HDIP_CSDA_PROJECT/blob/master/histogram_of_sepal_width.png)

##### 6.1.3 Histogram of Petal Length
![Histogram of Petal Length](https://github.com/Munster2020/HDIP_CSDA_PROJECT/blob/master/histogram_of_petal_length.png)

##### 6.1.4 Histogram of Petal Width
![Histogram of Petal Width](https://github.com/Munster2020/HDIP_CSDA_PROJECT/blob/master/histogram_of_petal_width.png)

#### 6.2 Scatterplots of width and length for Sepal and Petal
Scatterplots are often used in bivariate analysis as they are very good at visualising and identiying correlations or lack there of. Across their two dimesions scatterplots use dots  representing the values obtained for two different variables. In this project I compared sepal length and sepal width and petal length and petal width. I also used class so I could compare these variables across the different iris flower species.
```python
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
```
In scatterplots you interpet the data by looking for trends in the data as you go from left to right. *''If the data show an uphill pattern as you move from left to right, this indicates a positive relationship between X and Y. As the X-values increase (move right), the Y-values tend to increase (move up).''* If the *''data show a downhill pattern as you move from left to right, this indicates a negative relationship between X and Y. As the X-values increase (move right) the Y-values tend to decrease (move down).''* and finally if the data *''don’t seem to resemble any kind of pattern (even a vague one), then no relationship exists between X and Y.''*

From looking at the scatterplots below it looks like there is a positive relationship between petal length and petal width however in the case of sepal length and sepal width while still positive it is weaker.

![Sepal Scatterplot](https://github.com/Munster2020/HDIP_CSDA_PROJECT/blob/master/sepal%20scatterplot.png)

![Petal Scatterplot](https://github.com/Munster2020/HDIP_CSDA_PROJECT/blob/master/petal%20scatterplot.png)

#### 6.3 Pairplot
Another way of interpreting the dataset is to combine the above histograms and scatterplots which also means less coding which is one of the great features of Python by combining them in a pairplot. However, I changed the histograms to density plots on the diagonal to make it easier to compare distributions between the iris species than stacked bars. In the pairplot below, the density plots on the diagonal allow you to see distribution of a single variable while the scatterplots on the upper and lower triangles show the relationship (or lack of) between two variables. 
```python
# Create a pairplot of the dataset
sns.set_style('darkgrid')
sns.pairplot(iris_df, hue='class')
plt.savefig('iris dataset pairplot')
plt.close()
```
We know from our dataset that it contains four numeric attributes, sepal length and width and petal length and width. *''This means  we have 4C2 plots (shorthand for for the binomial coefficient with parameters 4 and 2). The number of unique ways in which we can choose 2 objects out of a set of 4 objects"*. Therefore, our pairs are:

(1) sepal_length, sepal_width

(2) sepal length, petal length

(3) sepal length, petal width

(4) sepal width, petal length

(5) sepal width, petal width

(6) petal length, petal width)

From the distributions below petal length is separating the iris setosa from the remaining. Therfore if you wanted to know if an Iris was Iris setosa or not, you would only need to know if the petal length was <2.  *''In terms of information theory, that fact has a high information entropy – meaning, it gives us a lot more insight about the dataset.''* [Lai.Nelson: Analysis of the famous Iris Flower dataset (Part 1)](https://wnellie.tumblr.com/post/143155937907/analysis-of-the-famous-iris-flower-dataset-part)

![Pairplot](https://github.com/Munster2020/HDIP_CSDA_PROJECT/blob/master/Iris%20Dataset%20Pairplot.png)


#### 6.4 Boxplot
Boxplots are a convenient way at looking at individual features and a key tool in descriptive statistics. They are a standardised way of displaying the distribution of data based on a *''five number summary, minimum first quartile, median, third quartile and maximum''*. One of the advantages of the boxplot in comparison to say histograms as discussed previously or density plots, is that they take up less space and provide you with a concise overview of your data.
```python
# Create boxplot of the dataset
iris_long = pd.melt(iris_df, id_vars='class')
sns.set_style('darkgrid')
sns.boxplot(x='class', y='value', hue='variable', data=iris_long)
plt.title('Boxplot of Class Attributes')
plt.savefig('class boxplot')
plt.close()
```
Prior to this project I had never used boxplots however they are quite easy to interpret. For instance lets look at the sepal length of Iris-virginica in the top right segment of the chart. The two vertical bars extending from the box capped with short horizontal lines show the maximum and minimum values excluding outliers. In this case the results are 7.92 cms and 5.62 cms. By the way the vertical lines are called whiskers simply because they resemble the whiskers or moustache of a cat. The black diamond shapes represent outliers i.e. values above or below the interquartile range. The top line of the box equates to the upper quartile, the bottom line the lower quartile and the intermediate line is the median.

![Boxplot](https://github.com/Munster2020/HDIP_CSDA_PROJECT/blob/master/class%20boxplot.png)

### Sources
[Code Academy: Seaborn Styling](https://www.codecademy.com/articles/seaborn-design-ii)

[Medium: Basic Analysis of the Iris Data set Using Python](https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342)

[Seaborn: Visualizing the distribution of a dataset](http://seaborn.pydata.org/tutorial/distributions.html)

[University of Warwick: Plotting the Iris Data](https://warwick.ac.uk/fac/sci/moac/people/students/peter_cock/r/iris_plots/)

[GeeksforGeeks: Box plot and Histogram exploration on Iris data](https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/)

[Kaggle: Seaborn Matplotlib plot to visualize Iris data](https://www.kaggle.com/biphili/seaborn-matplotlib-plot-to-visualize-iris-data)

[Pandas: pandas.DataFrame.info](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.info.html)

[Medium: Exploratory Data Analysis : Iris DataSet](https://medium.com/@harimittapalli/exploratory-data-analysis-iris-dataset-9920ea439a3e)

[Stackoverflow: How to redirect the output of print to a TXT file](https://stackoverflow.com/questions/4110891/how-to-redirect-the-output-of-print-to-a-txt-file)

[YouTube: Intermediate Python 7: numpy's loadtxt and savetxt](https://www.youtube.com/watch?v=bqo3BmzyXeI)

[YouTube: Import Data, Analyze, Export and Plot in Python](https://www.youtube.com/watch?v=pQv6zMlYJ0A)

[Stackoverflow: Python, Pandas : write content of DataFrame into text File](https://stackoverflow.com/questions/31247198/python-pandas-write-content-of-dataframe-into-text-file)

[Medium: Exploratory Data Analysis: Iris Flower Dataset](https://medium.com/analytics-vidhya/exploratory-data-analysis-iris-flower-dataset-a21c368a1f4)

[Shane Lynn: Summarising, Aggregating, and Grouping data in Python Pandas](https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/)

[Data to Fish: How to Import a CSV File into Python using Pandas](https://datatofish.com/import-csv-file-python-using-pandas/)

[MIT Open Courseware: Iris Dataset](https://ocw.mit.edu/courses/sloan-school-of-management/15-097-prediction-machine-learning-and-statistics-spring-2012/datasets/)

[CodeSpeedy: Importing dataset using Pandas (Python deep learning library )](https://www.codespeedy.com/importing-dataset-using-pandas-python-deep-learning-library/)

[University of Ljubljana: Classification of Iris data set)](http://lab.fs.uni-lj.si/lasin/wp/IMIT_files/neural/doc/seminar8.pdf)

[WikiMili: Iris flower data set](https://wikimili.com/en/Iris_flower_data_set)

[Medium: Exploratory Data Analysis of IRIS Data Set Using Python](https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d)

[Famous Scientists - The Art of Genius: Ronald Fisher](https://www.famousscientists.org/ronald-fisher/)

[Technopedia: Iris Flower Data Set](https://www.techopedia.com/definition/32880/iris-flower-data-set)

[Real Python: Python Statistics Fundamentals: How to Describe Your Data](https://realpython.com/python-statistics/)

[Chris Albon: Descriptive Statistics For pandas Dataframe](https://chrisalbon.com/python/data_wrangling/pandas_dataframe_descriptive_stats/)

[Dummies: How to Interpret a Scatterplot](https://www.dummies.com/education/math/statistics/how-to-interpret-a-scatterplot/)

[Intellspot: Bivariate Data: Examples, Definition and Analysis](http://intellspot.com/bivariate-data-examples/)

[Foundations of AI & ML: Pairplots](https://mylearningsinaiml.wordpress.com/2018/11/21/pair-plots/)

[Medium: Visualizing Data with Pairs Plots in Python](https://towardsdatascience.com/visualizing-data-with-pair-plots-in-python-f228cf529166)
