# Created by Adrian Donohoe 01/04/2019

import pandas as pd
import matplotlib.pyplot as plot


# Read in the CSV as dataframe
df = pd.read_csv('iris.csv')

# Adapted from https://stackoverflow.com/a/17071908
# Separate species into different dataframes
setosa = df.loc[df['species'] == 'setosa']   # Access a Dataframe by label species=setosa and assign to setosa variable
virginica = df.loc[df['species'] == 'virginica'] # Creating a virginica dataframe
versicolor = df.loc[df['species'] == 'versicolor'] # Creating a versicolor dataframe

# Adapted from https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html#pandas.DataFrame.set_index
s = pd.Series(range(0,50)) # makes a pandas Series used to reindex the virginica and versicolor indexes
vi = virginica.set_index(s) # set the index of the virginica dataframe
ve = versicolor.set_index(s)  # set the index of the versicolor dataframe , https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html#pandas.DataFrame.set_index


#https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplot.html?highlight=subplot#matplotlib.pyplot.subplot
plot.subplot(2,2,1) # make a subplot with 2 rows,2 columns at index 1
plot.plot(setosa['sepal_length'],'b.',vi['sepal_length'],'r.',ve['sepal_length'],'g.') # Plot the sepal lenghts of the 3 species in blue,red and green dots
plot.ylabel('Sepal Length in cm')  # Add a label to the y-axis
labels = ['Setosa','Virginica','Versicolor'] # will use this list to add a legend
plot.legend(labels) # Adapted from https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html. Adds a legend using the 'labels' list

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
plot.subplot(4,4,5) # make a subplot with 4 rows,4 columns at index 5
# The following takes the sepal length and width for each species. We apply the to_numpy() method to create a numpy array for plotting.
plot.plot(setosa['sepal_length'].to_numpy(),setosa['sepal_width'].to_numpy(),'b+',vi['sepal_length'].to_numpy(),vi['sepal_width'].to_numpy(),'r+',ve['sepal_length'].to_numpy(),ve['sepal_width'].to_numpy(),'g+')
plot.ylabel('Sepal width in cm')

plot.subplot(4,4,9) # Subplot for sepal length vs petal length
plot.plot(setosa['sepal_length'].to_numpy(),setosa['petal_length'].to_numpy(),'b+',vi['sepal_length'].to_numpy(),vi['petal_length'].to_numpy(),'r+',ve['sepal_length'].to_numpy(),ve['petal_length'].to_numpy(),'g+')
plot.ylabel('Petal length in cm')

plot.subplot(4,4,13) # Subplot for sepal length vs petal width
plot.plot(setosa['sepal_length'].to_numpy(),setosa['petal_width'].to_numpy(),'b+',vi['sepal_length'].to_numpy(),vi['petal_width'].to_numpy(),'r+',ve['sepal_length'].to_numpy(),ve['petal_width'].to_numpy(),'g+')
plot.ylabel('Petal width in cm')
plot.xlabel('Sepal length in cm')

# Adapted from https://matplotlib.org/examples/statistics/histogram_demo_multihist.html
plot.subplot(4,4,1) # Subplot for sepal length histogram
x_multi = [setosa['sepal_length'],vi['sepal_length'],ve['sepal_length']]
colours = ['blue','red','green'] # list to be used for histogram color parameter
plot.ylabel('Sepal length in cm')
plot.hist(x_multi,bins=10,stacked=True,color=colours) # plot a stacked histogram

plot.subplot(4,4,6)  # Subplot for sepal width histogram
x1_multi = [setosa['sepal_width'],vi['sepal_width'],ve['sepal_width']]
colours = ['blue','red','green']
plot.hist(x1_multi,bins=10,stacked=True,color=colours)

plot.subplot(4,4,11) # Subplot for petal length histogram
x2_multi = [setosa['petal_length'],vi['petal_length'],ve['petal_length']]
colours = ['blue','red','green']
plot.hist(x2_multi,bins=10,stacked=True,color=colours)

plot.subplot(4,4,16) # Subplot for petal width histogram
x3_multi = [setosa['petal_width'],vi['petal_width'],ve['petal_width']]
colours = ['blue','red','green']
plot.hist(x3_multi,bins=10,stacked=True,color=colours)
plot.xlabel('Petal width in cm')

plot.subplot(4,4,2) # Subplot for sepal width vs sepal length
plot.plot(setosa['sepal_width'].to_numpy(),setosa['sepal_length'].to_numpy(),'b+',vi['sepal_width'].to_numpy(),vi['sepal_length'].to_numpy(),'r+',ve['sepal_width'].to_numpy(),ve['sepal_length'].to_numpy(),'g+')

plot.subplot(4,4,10) # Subplot for sepal width vs petal length
plot.plot(setosa['sepal_width'].to_numpy(),setosa['petal_length'].to_numpy(),'b+',vi['sepal_width'].to_numpy(),vi['petal_length'].to_numpy(),'r+',ve['sepal_width'].to_numpy(),ve['petal_length'].to_numpy(),'g+')

plot.subplot(4,4,14) # Subplot for sepal width vs petal width
plot.plot(setosa['sepal_width'].to_numpy(),setosa['petal_width'].to_numpy(),'b+',vi['sepal_width'].to_numpy(),vi['petal_width'].to_numpy(),'r+',ve['sepal_width'].to_numpy(),ve['petal_width'].to_numpy(),'g+')
plot.xlabel('Sepal width in cm')


plot.subplot(4,4,3) # Subplot for petal length vs sepal length
plot.plot(setosa['petal_length'].to_numpy(),setosa['sepal_length'].to_numpy(),'b+',vi['petal_length'].to_numpy(),vi['sepal_length'].to_numpy(),'r+',ve['petal_length'].to_numpy(),ve['sepal_length'].to_numpy(),'g+')

plot.subplot(4,4,7) # Subplot for petal length vs sepal width
plot.plot(setosa['petal_length'].to_numpy(),setosa['sepal_width'].to_numpy(),'b+',vi['petal_length'].to_numpy(),vi['sepal_width'].to_numpy(),'r+',ve['petal_length'].to_numpy(),ve['sepal_width'].to_numpy(),'g+')

plot.subplot(4,4,15) # Subplot for petal length vs petal width
plot.plot(setosa['petal_length'].to_numpy(),setosa['petal_width'].to_numpy(),'b+',vi['petal_length'].to_numpy(),vi['petal_width'].to_numpy(),'r+',ve['petal_length'].to_numpy(),ve['petal_width'].to_numpy(),'g+')
plot.xlabel('Petal length in cm')


plot.subplot(4,4,4) # Subplot for petal width vs sepal length with labels
plot.plot(setosa['petal_width'].to_numpy(),setosa['sepal_length'].to_numpy(),'b+',label='setosa')
plot.plot(vi['petal_width'].to_numpy(),vi['sepal_length'].to_numpy(),'r+',label='virginica')
plot.plot(ve['petal_width'].to_numpy(),ve['sepal_length'].to_numpy(),'g+',label='versicolor')
# Adapted https://stackoverflow.com/a/43439132
plot.legend(bbox_to_anchor=(0., 1.02, 1.1, .2), loc="lower left", mode="expand", ncol=3) # 3 column label legend achored to box, using lower left as starting point

plot.subplot(4,4,8) # Subplot for petal width vs sepal width with labels
plot.plot(setosa['petal_width'].to_numpy(),setosa['sepal_width'].to_numpy(),'b+',vi['petal_width'].to_numpy(),vi['sepal_width'].to_numpy(),'r+',ve['petal_width'].to_numpy(),ve['sepal_width'].to_numpy(),'g+')

plot.subplot(4,4,12) # Subplot for petal width vs petal length with labels
plot.plot(setosa['petal_width'].to_numpy(),setosa['petal_length'].to_numpy(),'b+',vi['petal_width'].to_numpy(),vi['petal_length'].to_numpy(),'r+',ve['petal_width'].to_numpy(),ve['petal_length'].to_numpy(),'g+')

plot.suptitle('Sepal/Petal width/length pair plots') # Adds a super title to the 4x4 plot. Adapted from https://matplotlib.org/api/_as_gen/matplotlib.pyplot.suptitle.html
plot.show()

#print('Setosa min sepal length is ', setosa['sepal_length'].min())
#print('Setosa max sepal length is ', setosa['sepal_length'].max())
#print('Setosa mean sepal length is ', setosa['sepal_length'].mean())
#print('Setosa min sepal length is ', setosa['sepal_length'].min())
#print('Setosa STD sepal length is ', setosa['sepal_length'].std())


y=df.describe() # This makes a number of calculations in one go.
y.to_csv('description.csv') # Used this csv to generate a table for the README

sy=setosa.describe() # This makes a number of calculations in one go.
sy.to_csv('setosa_description.csv') # Used this csv to generate a table for the README
viy=vi.describe()# This makes a number of calculations in one go.
viy.to_csv('virginica_description.csv') # Used this csv to generate a table for the README
vey=ve.describe()# This makes a number of calculations in one go.
vey.to_csv('versicolor_description.csv') # Used this csv to generate a table for the README

