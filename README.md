# Higher Diploma in Science in Computing (Data Analytics)
## Programming and Scripting (COMP08049) 
## Project 2020 – Fisher’s Iris Data Set


### Problem Statement
This project deals with Fisher's Iris data set. For the project I had to research the data set and write documentation and code in Python to investigate it.

I used descriptive statistics to answer this problem. This method uses two approaches. Firstly using quantitative statistics to describe and summarise the data numerically and secondly use visual interpretation to illustrate the data with charts, plots and histograms.

![alt text](https://i1.wp.com/dataaspirant.com/wp-content/uploads/2017/01/irises.png?resize=600%2C181 "Iris Flowers")


### Summary
The Iris flower data set was compiled by Ronald Fisher in the 1930's. Fisher was born in London in 1890 and went on to become one of the most highly regarded statisticians of the 20th Century. He pioneered the application of statistical procedures to the dsign of scientific experiments. In tandem with his work in statistics he was also one of the principal founders of population eugenics. His work in biology led to the the geneticist and author Richard Dawkins calling him the greatest biologist since Charles Darwin.

Fisher introduced the Iris Flower data set in a paper published in "The Annals of Human Genetics" in 1936 called "The Use of Multiple Measurements in Taxonomic Problems" as an example of linear discriminant analysis. The dataset cotains three classes of fifty instances each. Each class refers to a type of iris plant. Each class is linearly separable from the other two classes. The first two species Iris setosa and Iris versicolour, were found growing together in the same colony.The third species called Iris virginica was taken from a different colony.

The data set contains the following attributes.

(1) sepal length in cms

(2) sepal width in cms

(3) petal length in cms

(4) petal width in cms

(5) class:

   * Iris setosa
    
   * Iris versicolour
    
   * Iris virginica

### Python Code
### 1. Import modules
The first section of my code imports modules required for the project.
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
### 2. Create dataframe
Next I loaded the data using a pandas dataframe and created column headings. I sourced the dataset from the UCI Machine Learning Repository via [MITOpenCourseWare](https://ocw.mit.edu/courses/sloan-school-of-management/15-097-prediction-machine-learning-and-statistics-spring-2012/datasets/)
```python
iris_df = pd.read_csv('iris.csv')
iris_df = pd.DataFrame(data, columns = ['sepal length in cm', 'sepal width in cm', 
'petal length in cm', 'petal width in cm', 'class'])
```
### 3. Redirect to text file
For this project we were asked to output our findings to a text file. In order to do this I used the below piece of code which uses the Sys module mentioned previously.
```python
sys.stdout = open("iris_summary.txt", 'w')
```
### 4. Data exploration
Having obtained the data the next step was to perform some exploratory data analysis. Looking in more detail at the dataset attributes, classifications of Iris plant and datatypes. The code below confirmed a relatively small dataset with only 150 records (50 in each class) namely Iris Setosa, Iris Versicolour and Iris Virginica. There is four numeric predictive attributes (float64) and the class (object). There is no missing values. 
```python
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
print('===============')
print('Information on the dataset')
print('--------------------------')
print(iris_df.info())
```
### 5. Summary statistics 
Next up was to examine the dataset using some of the built in functionality of Pandas. First I used describe() to generate some descriptive statistics of the numeric and non-numeric datatypes, focusing on the central tendency, dispersion and shape of the dataset distribution. I also looked in more detail at the median, mode and variance as well as correlation and covariance.
```python
print ('===================================')
print ('Statistical Summary of numeric data')
print ('-----------------------------------')
print (iris_df.describe())
print ('=======================================')
print ('Statistical Summary of non-numeric data')
print ('---------------------------------------')
print (iris_df.describe(include=[object]))
print ('===============')
print ('Dataset Median')
print ('--------------')
print (iris_df.median())
print ('===============')
print ('Dataset Mode')
print ('--------------')
print (iris_df.mode(numeric_only=True))
print ('===============')
print ('Dataset Variance')
print ('--------------')
print (iris_df.var())
print ('====================================')
print ('Dataset Correlation Matrix Of Values')
print ('------------------------------------')
print (iris_df.corr())
print ('====================================')
print ('Dataset Covariance Matrix Of Values')
print ('------------------------------------')
print (iris_df.cov())
print ('===============')
```
### 6. Visual interpretation
After gathering some descriptions and summaries of the dataset the next section of code looks at interpreting the data visually.
First I created histograms to look at each of the numeric attributes sepal length and width and petal length and width.

```python
a = 'sepal length in cm'
b = 'sepal width in cm'
c = 'petal length in cm'
d = 'petal width in cm'
e = 'class'

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
```

![Histogram of Sepal Length](https://github.com/Munster2020/HDIP_CSDA_PROJECT/blob/master/histogram_of_sepal_length.png)

![Histogram of Sepal Width](https://github.com/Munster2020/HDIP_CSDA_PROJECT/blob/master/histogram_of_sepal_width.png)

![Histogram of Petal Length](https://github.com/Munster2020/HDIP_CSDA_PROJECT/blob/master/histogram_of_petal_length.png)

![Histogram of Petal Width](https://github.com/Munster2020/HDIP_CSDA_PROJECT/blob/master/histogram_of_petal_width.png)

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
