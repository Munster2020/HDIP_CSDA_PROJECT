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
```import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import pandas as pd
import seaborn as sns
import sys
```

```iris_df = pd.read_csv('iris.csv')
```

```sys.stdout = open("iris_summary.txt", 'w')
```

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
