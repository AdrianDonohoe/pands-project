# Created by Adrian Donohoe 01/04/2019

import pandas as pd
import matplotlib.pyplot as plot


# Read in the CSV as dataframe
df = pd.read_csv('iris.csv')

# Adapted from https://stackoverflow.com/a/17071908
# Separate species into different dataframes
setosa = df.loc[df['species'] == 'setosa']   # Access a Dataframe by label species=setosa and assign to setosa variable
virginica = df.loc[df['species'] == 'virginica']
versicolor = df.loc[df['species'] == 'versicolor']

# Adapted from https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html#pandas.DataFrame.set_index
s = pd.Series(range(0,50)) # makes a pandas Series used to reindex the virginica and versicolor indexes
vi = virginica.set_index(s)
ve = versicolor.set_index(s)  # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html#pandas.DataFrame.set_index


#https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplot.html?highlight=subplot#matplotlib.pyplot.subplot
plot.subplot(2,2,1) # make a subplot with 2 rows,2 columns at index 1
plot.plot(setosa['sepal_length'],'b.',vi['sepal_length'],'r.',ve['sepal_length'],'g.') # Plot the sepal lenghts of the 3 species in blue,red and green dots
plot.ylabel('Sepal Length in cm')  # Add a label to the y-axis
labels = ['Setosa','Virginica','Versicolor'] # will use this list to add a legend
plot.legend(labels) # Adapted from https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html

plot.subplot(2,2,2) # make a subplot with 2 rows,2 columns at index 2
plot.plot(setosa['sepal_width'],'b.',vi['sepal_width'],'r.',ve['sepal_width'],'g.')
plot.legend(labels) # Adapted from https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html

plot.subplot(2,2,3) # make a subplot with 2 rows,2 columns at index 3
plot.plot(setosa['petal_length'],'b.',vi['petal_length'],'r.',ve['petal_length'],'g.')
plot.ylabel('Petal Length in cm')
plot.legend(labels) # Adapted from https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html

plot.subplot(2,2,4) # make a subplot with 2 rows,2 columns at index 4
plot.plot(setosa['petal_width'],'b.',vi['petal_width'],'r.',ve['petal_width'],'g.')
plot.legend(labels) # Adapted from https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html
plot.suptitle('Measurements of Petal/Sepal widths/lengths by species') # Adapted from https://stackoverflow.com/a/25243066

plot.show()  # Show the 2x2 Subplot (Plot saved as 2x2_measurements.png and displayed in the README)



# adapted https://www.kaggle.com/jchen2186/machine-learning-with-iris-dataset
# Using matplotlib instead of seaborn, I have recreated the 4x4 subplots from this kaggle project
plot.subplot(4,4,5)
plot.plot(setosa['sepal_length'].to_numpy(),setosa['sepal_width'].to_numpy(),'b+',vi['sepal_length'].to_numpy(),vi['sepal_width'].to_numpy(),'r+',ve['sepal_length'].to_numpy(),ve['sepal_width'].to_numpy(),'g+')
plot.ylabel('Sepal width in cm')

plot.subplot(4,4,9)
plot.plot(setosa['sepal_length'].to_numpy(),setosa['petal_length'].to_numpy(),'b+',vi['sepal_length'].to_numpy(),vi['petal_length'].to_numpy(),'r+',ve['sepal_length'].to_numpy(),ve['petal_length'].to_numpy(),'g+')
plot.ylabel('Petal length in cm')

plot.subplot(4,4,13)
plot.plot(setosa['sepal_length'].to_numpy(),setosa['petal_width'].to_numpy(),'b+',vi['sepal_length'].to_numpy(),vi['petal_width'].to_numpy(),'r+',ve['sepal_length'].to_numpy(),ve['petal_width'].to_numpy(),'g+')
plot.ylabel('Petal width in cm')
plot.xlabel('Sepal length in cm')

# Adapted from https://matplotlib.org/examples/statistics/histogram_demo_multihist.html
plot.subplot(4,4,1)
x_multi = [setosa['sepal_length'],vi['sepal_length'],ve['sepal_length']]
colours = ['blue','red','green']
plot.ylabel('Sepal length in cm')
plot.hist(x_multi,bins=10,stacked=True,color=colours)

plot.subplot(4,4,6)
x1_multi = [setosa['sepal_width'],vi['sepal_width'],ve['sepal_width']]
colours = ['blue','red','green']
plot.hist(x1_multi,bins=10,stacked=True,color=colours)

plot.subplot(4,4,11)
x2_multi = [setosa['petal_length'],vi['petal_length'],ve['petal_length']]
colours = ['blue','red','green']
plot.hist(x2_multi,bins=10,stacked=True,color=colours)

plot.subplot(4,4,16)
x3_multi = [setosa['petal_width'],vi['petal_width'],ve['petal_width']]
colours = ['blue','red','green']
plot.hist(x3_multi,bins=10,stacked=True,color=colours)
plot.xlabel('Petal width in cm')

plot.subplot(4,4,2)
plot.plot(setosa['sepal_width'].to_numpy(),setosa['sepal_length'].to_numpy(),'b+',vi['sepal_width'].to_numpy(),vi['sepal_length'].to_numpy(),'r+',ve['sepal_width'].to_numpy(),ve['sepal_length'].to_numpy(),'g+')

plot.subplot(4,4,10)
plot.plot(setosa['sepal_width'].to_numpy(),setosa['petal_length'].to_numpy(),'b+',vi['sepal_width'].to_numpy(),vi['petal_length'].to_numpy(),'r+',ve['sepal_width'].to_numpy(),ve['petal_length'].to_numpy(),'g+')

plot.subplot(4,4,14)
plot.plot(setosa['sepal_width'].to_numpy(),setosa['petal_width'].to_numpy(),'b+',vi['sepal_width'].to_numpy(),vi['petal_width'].to_numpy(),'r+',ve['sepal_width'].to_numpy(),ve['petal_width'].to_numpy(),'g+')
plot.xlabel('Sepal width in cm')


plot.subplot(4,4,3)
plot.plot(setosa['petal_length'].to_numpy(),setosa['sepal_length'].to_numpy(),'b+',vi['petal_length'].to_numpy(),vi['sepal_length'].to_numpy(),'r+',ve['petal_length'].to_numpy(),ve['sepal_length'].to_numpy(),'g+')

plot.subplot(4,4,7)
plot.plot(setosa['petal_length'].to_numpy(),setosa['sepal_width'].to_numpy(),'b+',vi['petal_length'].to_numpy(),vi['sepal_width'].to_numpy(),'r+',ve['petal_length'].to_numpy(),ve['sepal_width'].to_numpy(),'g+')

plot.subplot(4,4,15)
plot.plot(setosa['petal_length'].to_numpy(),setosa['petal_width'].to_numpy(),'b+',vi['petal_length'].to_numpy(),vi['petal_width'].to_numpy(),'r+',ve['petal_length'].to_numpy(),ve['petal_width'].to_numpy(),'g+')
plot.xlabel('Petal length in cm')


plot.subplot(4,4,4)
plot.plot(setosa['petal_width'].to_numpy(),setosa['sepal_length'].to_numpy(),'b+',label='setosa')
plot.plot(vi['petal_width'].to_numpy(),vi['sepal_length'].to_numpy(),'r+',label='virginica')
plot.plot(ve['petal_width'].to_numpy(),ve['sepal_length'].to_numpy(),'g+',label='versicolor')
# Adapted https://stackoverflow.com/a/43439132
plot.legend(bbox_to_anchor=(0., 1.02, 1.1, .2), loc="lower left", mode="expand", ncol=3)

plot.subplot(4,4,8)
plot.plot(setosa['petal_width'].to_numpy(),setosa['sepal_width'].to_numpy(),'b+',vi['petal_width'].to_numpy(),vi['sepal_width'].to_numpy(),'r+',ve['petal_width'].to_numpy(),ve['sepal_width'].to_numpy(),'g+')

plot.subplot(4,4,12)
plot.plot(setosa['petal_width'].to_numpy(),setosa['petal_length'].to_numpy(),'b+',vi['petal_width'].to_numpy(),vi['petal_length'].to_numpy(),'r+',ve['petal_width'].to_numpy(),ve['petal_length'].to_numpy(),'g+')

plot.suptitle('Sepal/Petal width/length pair plots')
plot.show()

#print('Setosa min sepal length is ', setosa['sepal_length'].min())
#print('Setosa max sepal length is ', setosa['sepal_length'].max())
#print('Setosa mean sepal length is ', setosa['sepal_length'].mean())
#print('Setosa min sepal length is ', setosa['sepal_length'].min())
#print('Setosa STD sepal length is ', setosa['sepal_length'].std())


y=df.describe()
y.to_csv('description.csv')

sy=setosa.describe()
sy.to_csv('setosa_description.csv')
viy=vi.describe()
viy.to_csv('virginica_description.csv')
vey=ve.describe()
vey.to_csv('versicolor_description.csv')

