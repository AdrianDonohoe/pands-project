## pands-project

# Basic Outline
what is data set about ?
Who is Ronald Fisher ?
Describe the data set .
how was it collected.
I think the conclusions that Fisher makes would be interesting to know.

High level about the data set - number of rows, columns 
what do the columns look like ? average petal length of a satosa ...
Pick out relevant and interesting stuff

One of the types can be separated easily from the other two

Add tables and graphs

Explain the python script. Read in the file, do some calculations, averages, standard deviations. Make some plots.

References: Make sure to reference everything.

Worth a look : UC Irvine Machine Learning Repository. Iris data set.
http://archive.ics.uci.edu/ml/datasets/Iris.



# Introduction
https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.names
This is perhaps the best known database to be found in the pattern recognition literature.  Fisher's paper is a classic in the field and is referenced frequently to this day.  (See Duda & Hart, for example.)  The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant.  One class is linearly separable from the other 2; the latter are NOT linearly separable from each other. 

https://www.kaggle.com/jchen2186/machine-learning-with-iris-dataset
There are 150 observations with 4 features each (sepal length, sepal width, petal length, petal width).
There are no null values, so we don't have to worry about that.
There are 50 observations of each species (setosa, versicolor, virginica).
The Iris dataset was used in R.A. Fisher's classic 1936 paper, The Use of Multiple Measurements in Taxonomic Problems, and can also be found on the UCI Machine Learning Repository.


https://www.kaggle.com/arshid/iris-flower-dataset
The Iris flower data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems. It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. The data set consists of 50 samples from each of three species of Iris (Iris Setosa, Iris virginica, and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters.

This dataset became a typical test case for many statistical classification techniques in machine learning such as support vector machines

https://www.academia.edu/13069408/Report_on_Edgar_Anderson_s_Iris_Data_Analysis
Two of the three species were collected in theGasp´e Peninsula ”all from the same pasture, and picked on the same day and measured at the same time bythe same person with the same apparatus”.

Who was Ronald Fisher ?
https://www.famousscientists.org/ronald-fisher/
Although Ronald Fisher’s name is less well-known than some others, he was one of the twentieth century’s greatest scientists.

In addition to being probably the greatest statistician ever, he also invented experimental design and was one of the principal founders of population genetics. He unified the disconnected concepts of natural selection and Mendel’s rules of inheritance. The importance of his book Statistical Methods for Research Workers in quantitative biology has been likened to that of Isaac Newton’s Principia in physics.

According to geneticist and author Richard Dawkins, Fisher was the greatest biologist since Charles Darwin.

Fisher viewed himself as a scientist who was especially interested in biology. He did not, however, enjoy learning the names and details of biological structures. He decided to study mathematics, believing it was through mathematics he could make the greatest contributions to biology.

| sepal_length | sepal_width | petal_length | petal_width | species    | 
|--------------|-------------|--------------|-------------|------------| 
| 5.1          | 3.5         | 1.4          | 0.2         | setosa     | 
| 4.9          | 3.0         | 1.4          | 0.2         | setosa     | 
| 4.7          | 3.2         | 1.3          | 0.2         | setosa     | 
| 4.6          | 3.1         | 1.5          | 0.2         | setosa     | 
| 5.0          | 3.6         | 1.4          | 0.2         | setosa     | 
| 5.4          | 3.9         | 1.7          | 0.4         | setosa     | 
| 4.6          | 3.4         | 1.4          | 0.3         | setosa     | 
| 5.0          | 3.4         | 1.5          | 0.2         | setosa     | 
| 4.4          | 2.9         | 1.4          | 0.2         | setosa     | 
| 4.9          | 3.1         | 1.5          | 0.1         | setosa     | 
| 5.4          | 3.7         | 1.5          | 0.2         | setosa     | 
| 4.8          | 3.4         | 1.6          | 0.2         | setosa     | 
| 4.8          | 3.0         | 1.4          | 0.1         | setosa     | 
| 4.3          | 3.0         | 1.1          | 0.1         | setosa     | 
| 5.8          | 4.0         | 1.2          | 0.2         | setosa     | 
| 5.7          | 4.4         | 1.5          | 0.4         | setosa     | 
| 5.4          | 3.9         | 1.3          | 0.4         | setosa     | 
| 5.1          | 3.5         | 1.4          | 0.3         | setosa     | 
| 5.7          | 3.8         | 1.7          | 0.3         | setosa     | 
| 5.1          | 3.8         | 1.5          | 0.3         | setosa     | 
| 5.4          | 3.4         | 1.7          | 0.2         | setosa     | 
| 5.1          | 3.7         | 1.5          | 0.4         | setosa     | 
| 4.6          | 3.6         | 1.0          | 0.2         | setosa     | 
| 5.1          | 3.3         | 1.7          | 0.5         | setosa     | 
| 4.8          | 3.4         | 1.9          | 0.2         | setosa     | 
| 5.0          | 3.0         | 1.6          | 0.2         | setosa     | 
| 5.0          | 3.4         | 1.6          | 0.4         | setosa     | 
| 5.2          | 3.5         | 1.5          | 0.2         | setosa     | 
| 5.2          | 3.4         | 1.4          | 0.2         | setosa     | 
| 4.7          | 3.2         | 1.6          | 0.2         | setosa     | 
| 4.8          | 3.1         | 1.6          | 0.2         | setosa     | 
| 5.4          | 3.4         | 1.5          | 0.4         | setosa     | 
| 5.2          | 4.1         | 1.5          | 0.1         | setosa     | 
| 5.5          | 4.2         | 1.4          | 0.2         | setosa     | 
| 4.9          | 3.1         | 1.5          | 0.1         | setosa     | 
| 5.0          | 3.2         | 1.2          | 0.2         | setosa     | 
| 5.5          | 3.5         | 1.3          | 0.2         | setosa     | 
| 4.9          | 3.1         | 1.5          | 0.1         | setosa     | 
| 4.4          | 3.0         | 1.3          | 0.2         | setosa     | 
| 5.1          | 3.4         | 1.5          | 0.2         | setosa     | 
| 5.0          | 3.5         | 1.3          | 0.3         | setosa     | 
| 4.5          | 2.3         | 1.3          | 0.3         | setosa     | 
| 4.4          | 3.2         | 1.3          | 0.2         | setosa     | 
| 5.0          | 3.5         | 1.6          | 0.6         | setosa     | 
| 5.1          | 3.8         | 1.9          | 0.4         | setosa     | 
| 4.8          | 3.0         | 1.4          | 0.3         | setosa     | 
| 5.1          | 3.8         | 1.6          | 0.2         | setosa     | 
| 4.6          | 3.2         | 1.4          | 0.2         | setosa     | 
| 5.3          | 3.7         | 1.5          | 0.2         | setosa     | 
| 5.0          | 3.3         | 1.4          | 0.2         | setosa     | 
| 7.0          | 3.2         | 4.7          | 1.4         | versicolor | 
| 6.4          | 3.2         | 4.5          | 1.5         | versicolor | 
| 6.9          | 3.1         | 4.9          | 1.5         | versicolor | 
| 5.5          | 2.3         | 4.0          | 1.3         | versicolor | 
| 6.5          | 2.8         | 4.6          | 1.5         | versicolor | 
| 5.7          | 2.8         | 4.5          | 1.3         | versicolor | 
| 6.3          | 3.3         | 4.7          | 1.6         | versicolor | 
| 4.9          | 2.4         | 3.3          | 1.0         | versicolor | 
| 6.6          | 2.9         | 4.6          | 1.3         | versicolor | 
| 5.2          | 2.7         | 3.9          | 1.4         | versicolor | 
| 5.0          | 2.0         | 3.5          | 1.0         | versicolor | 
| 5.9          | 3.0         | 4.2          | 1.5         | versicolor | 
| 6.0          | 2.2         | 4.0          | 1.0         | versicolor | 
| 6.1          | 2.9         | 4.7          | 1.4         | versicolor | 
| 5.6          | 2.9         | 3.6          | 1.3         | versicolor | 
| 6.7          | 3.1         | 4.4          | 1.4         | versicolor | 
| 5.6          | 3.0         | 4.5          | 1.5         | versicolor | 
| 5.8          | 2.7         | 4.1          | 1.0         | versicolor | 
| 6.2          | 2.2         | 4.5          | 1.5         | versicolor | 
| 5.6          | 2.5         | 3.9          | 1.1         | versicolor | 
| 5.9          | 3.2         | 4.8          | 1.8         | versicolor | 
| 6.1          | 2.8         | 4.0          | 1.3         | versicolor | 
| 6.3          | 2.5         | 4.9          | 1.5         | versicolor | 
| 6.1          | 2.8         | 4.7          | 1.2         | versicolor | 
| 6.4          | 2.9         | 4.3          | 1.3         | versicolor | 
| 6.6          | 3.0         | 4.4          | 1.4         | versicolor | 
| 6.8          | 2.8         | 4.8          | 1.4         | versicolor | 
| 6.7          | 3.0         | 5.0          | 1.7         | versicolor | 
| 6.0          | 2.9         | 4.5          | 1.5         | versicolor | 
| 5.7          | 2.6         | 3.5          | 1.0         | versicolor | 
| 5.5          | 2.4         | 3.8          | 1.1         | versicolor | 
| 5.5          | 2.4         | 3.7          | 1.0         | versicolor | 
| 5.8          | 2.7         | 3.9          | 1.2         | versicolor | 
| 6.0          | 2.7         | 5.1          | 1.6         | versicolor | 
| 5.4          | 3.0         | 4.5          | 1.5         | versicolor | 
| 6.0          | 3.4         | 4.5          | 1.6         | versicolor | 
| 6.7          | 3.1         | 4.7          | 1.5         | versicolor | 
| 6.3          | 2.3         | 4.4          | 1.3         | versicolor | 
| 5.6          | 3.0         | 4.1          | 1.3         | versicolor | 
| 5.5          | 2.5         | 4.0          | 1.3         | versicolor | 
| 5.5          | 2.6         | 4.4          | 1.2         | versicolor | 
| 6.1          | 3.0         | 4.6          | 1.4         | versicolor | 
| 5.8          | 2.6         | 4.0          | 1.2         | versicolor | 
| 5.0          | 2.3         | 3.3          | 1.0         | versicolor | 
| 5.6          | 2.7         | 4.2          | 1.3         | versicolor | 
| 5.7          | 3.0         | 4.2          | 1.2         | versicolor | 
| 5.7          | 2.9         | 4.2          | 1.3         | versicolor | 
| 6.2          | 2.9         | 4.3          | 1.3         | versicolor | 
| 5.1          | 2.5         | 3.0          | 1.1         | versicolor | 
| 5.7          | 2.8         | 4.1          | 1.3         | versicolor | 
| 6.3          | 3.3         | 6.0          | 2.5         | virginica  | 
| 5.8          | 2.7         | 5.1          | 1.9         | virginica  | 
| 7.1          | 3.0         | 5.9          | 2.1         | virginica  | 
| 6.3          | 2.9         | 5.6          | 1.8         | virginica  | 
| 6.5          | 3.0         | 5.8          | 2.2         | virginica  | 
| 7.6          | 3.0         | 6.6          | 2.1         | virginica  | 
| 4.9          | 2.5         | 4.5          | 1.7         | virginica  | 
| 7.3          | 2.9         | 6.3          | 1.8         | virginica  | 
| 6.7          | 2.5         | 5.8          | 1.8         | virginica  | 
| 7.2          | 3.6         | 6.1          | 2.5         | virginica  | 
| 6.5          | 3.2         | 5.1          | 2.0         | virginica  | 
| 6.4          | 2.7         | 5.3          | 1.9         | virginica  | 
| 6.8          | 3.0         | 5.5          | 2.1         | virginica  | 
| 5.7          | 2.5         | 5.0          | 2.0         | virginica  | 
| 5.8          | 2.8         | 5.1          | 2.4         | virginica  | 
| 6.4          | 3.2         | 5.3          | 2.3         | virginica  | 
| 6.5          | 3.0         | 5.5          | 1.8         | virginica  | 
| 7.7          | 3.8         | 6.7          | 2.2         | virginica  | 
| 7.7          | 2.6         | 6.9          | 2.3         | virginica  | 
| 6.0          | 2.2         | 5.0          | 1.5         | virginica  | 
| 6.9          | 3.2         | 5.7          | 2.3         | virginica  | 
| 5.6          | 2.8         | 4.9          | 2.0         | virginica  | 
| 7.7          | 2.8         | 6.7          | 2.0         | virginica  | 
| 6.3          | 2.7         | 4.9          | 1.8         | virginica  | 
| 6.7          | 3.3         | 5.7          | 2.1         | virginica  | 
| 7.2          | 3.2         | 6.0          | 1.8         | virginica  | 
| 6.2          | 2.8         | 4.8          | 1.8         | virginica  | 
| 6.1          | 3.0         | 4.9          | 1.8         | virginica  | 
| 6.4          | 2.8         | 5.6          | 2.1         | virginica  | 
| 7.2          | 3.0         | 5.8          | 1.6         | virginica  | 
| 7.4          | 2.8         | 6.1          | 1.9         | virginica  | 
| 7.9          | 3.8         | 6.4          | 2.0         | virginica  | 
| 6.4          | 2.8         | 5.6          | 2.2         | virginica  | 
| 6.3          | 2.8         | 5.1          | 1.5         | virginica  | 
| 6.1          | 2.6         | 5.6          | 1.4         | virginica  | 
| 7.7          | 3.0         | 6.1          | 2.3         | virginica  | 
| 6.3          | 3.4         | 5.6          | 2.4         | virginica  | 
| 6.4          | 3.1         | 5.5          | 1.8         | virginica  | 
| 6.0          | 3.0         | 4.8          | 1.8         | virginica  | 
| 6.9          | 3.1         | 5.4          | 2.1         | virginica  | 
| 6.7          | 3.1         | 5.6          | 2.4         | virginica  | 
| 6.9          | 3.1         | 5.1          | 2.3         | virginica  | 
| 5.8          | 2.7         | 5.1          | 1.9         | virginica  | 
| 6.8          | 3.2         | 5.9          | 2.3         | virginica  | 
| 6.7          | 3.3         | 5.7          | 2.5         | virginica  | 
| 6.7          | 3.0         | 5.2          | 2.3         | virginica  | 
| 6.3          | 2.5         | 5.0          | 1.9         | virginica  | 
| 6.5          | 3.0         | 5.2          | 2.0         | virginica  | 
| 6.2          | 3.4         | 5.4          | 2.3         | virginica  | 
| 5.9          | 3.0         | 5.1          | 1.8         | virginica  | 

