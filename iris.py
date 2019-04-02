# Created by Adrian Donohoe 01/04/2019

import pandas as pd
import matplotlib.pyplot as plot

# Read in the CSV as dataframe
df = pd.read_csv('iris.csv')

# Adapted from https://stackoverflow.com/a/17071908
# Separate species into different dataframes
setosa = df.loc[df['species'] == 'setosa']
virginica = df.loc[df['species'] == 'virginica']
versicolor = df.loc[df['species'] == 'versicolor']

# Adapted from https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html#pandas.DataFrame.set_index
s = pd.Series(range(0,50)) # makes a pandas Series used to reindex the virginica and versicolor indexes
vi = virginica.set_index(s)
ve = versicolor.set_index(s)

plot.plot(setosa['sepal_length'],'b.',vi['sepal_length'],'r.',ve['sepal_length'],'g.')
plot.ylabel('Sepal Length in cm')
plot.title('Measurements of Sepal lengths by species')
labels = ['Setosa','Virginica','Versicolor']
plot.legend(labels) # Adapted from https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html
plot.show()

plot.plot(setosa['sepal_width'],'b.',vi['sepal_width'],'r.',ve['sepal_width'],'g.')
plot.ylabel('Sepal Width in cm')
plot.title('Measurements of Sepal widths by species')
labels = ['Setosa','Virginica','Versicolor']
plot.legend(labels) # Adapted from https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html
plot.show()

plot.plot(setosa['petal_length'],'b.',vi['petal_length'],'r.',ve['petal_length'],'g.')
plot.ylabel('Petal Length in cm')
plot.title('Measurements of Petal lengths by species')
labels = ['Setosa','Virginica','Versicolor']
plot.legend(labels) # Adapted from https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html
plot.show()

plot.plot(setosa['petal_width'],'b.',vi['petal_width'],'r.',ve['petal_width'],'g.')
plot.ylabel('Petal Width in cm')
plot.title('Measurements of Petal widths by species')
labels = ['Setosa','Virginica','Versicolor']
plot.legend(labels) # Adapted from https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html
plot.show()



# adapted https://www.kaggle.com/jchen2186/machine-learning-with-iris-dataset
plot.plot(setosa['sepal_length'].values,setosa['sepal_width'].values,'b+',vi['sepal_length'].values,vi['sepal_width'].values,'r+',ve['sepal_length'].values,ve['sepal_width'].values,'g+')
plot.legend(labels)
plot.show()
plot.plot(setosa['sepal_length'].values,setosa['petal_length'].values,'b+',vi['sepal_length'].values,vi['petal_length'].values,'r+',ve['sepal_length'].values,ve['petal_length'].values,'g+')
plot.legend(labels)
plot.show()
plot.plot(setosa['sepal_length'].values,setosa['petal_width'].values,'b+',vi['sepal_length'].values,vi['petal_width'].values,'r+',ve['sepal_length'].values,ve['petal_width'].values,'g+')
plot.legend(labels)
plot.show()

# Adapted from https://matplotlib.org/examples/statistics/histogram_demo_multihist.html
x_multi = [setosa['sepal_length'],vi['sepal_length'],ve['sepal_length']]
colours = ['blue','red','green']
plot.hist(x_multi,bins=10,stacked=True,color=colours)
plot.legend(labels)
plot.show()


#print('Setosa min sepal length is ', setosa['sepal_length'].min())
#print('Setosa max sepal length is ', setosa['sepal_length'].max())
#print('Setosa mean sepal length is ', setosa['sepal_length'].mean())
#print('Setosa min sepal length is ', setosa['sepal_length'].min())
#print('Setosa STD sepal length is ', setosa['sepal_length'].std())

