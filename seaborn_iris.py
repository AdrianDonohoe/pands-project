# Adapted from https://seaborn.pydata.org/examples/scatterplot_matrix.html
# In week 12 videos we saw how some Iris plots were done in seaborn. It is much simpler code and only took a few minutes to put together. In my view the seaborn plots are visually better.
import seaborn as sns
import matplotlib.pyplot as plot
import pandas as pd

#sns.set_style("ticks")  # Set the plot style
sns.set()  # Sets default styling
dfs = sns.load_dataset("iris") # Load the iris dataset built into seaborn
g=sns.pairplot(dfs, hue="species",markers=["o","s","D"]) # Make a pairplot of all columns in the dataset. The hue will be determined by species.The plot markers will be dots, squares and diamonds.
g.fig.suptitle("Sepal/Petal width/length pair plots") # Adapted from https://stackoverflow.com/a/49594152 . Add a super-title to the figure
plot.subplots_adjust(top=0.9) # Adapted from from https://stackoverflow.com/a/29814281 Adjusts the top of the plot to make room for the super-title.

plot.show() #Show the plot

# Adapted from https://stackoverflow.com/a/17071908
# Separate species into different dataframes
setosa = dfs.loc[dfs['species'] == 'setosa']   # Access a Dataframe by label species=setosa and assign to setosa variable
virginica = dfs.loc[dfs['species'] == 'virginica']
versicolor = dfs.loc[dfs['species'] == 'versicolor']

s = pd.Series(range(0,50)) # makes a pandas Series used to reindex the virginica and versicolor indexes
vi = virginica.set_index(s)
ve = versicolor.set_index(s)  # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html#pandas.DataFrame.set_index

g1 , axes = plot.subplots(nrows=2,ncols=2)  # Adpated from https://matplotlib.org/gallery/subplots_axes_and_figures/subplots_demo.html . Make a figure and axes object for subplot with 2 rows and 2 columns
sns.scatterplot(x=setosa.index,y='petal_length',data=setosa,ax=axes[0,0],marker="o",legend="full") # Apdapted from https://seaborn.pydata.org/generated/seaborn.scatterplot.html . Makes a scatter plot with x-axis (index), y-axis (petal length), hued by species in axes postion 0,0. Style/markers by species.
sns.scatterplot(x=vi.index,y='petal_length',data=vi,ax=axes[0,0],marker="s")
sns.scatterplot(x=ve.index,y='petal_length',data=ve,ax=axes[0,0],marker="D")

sns.scatterplot(x=setosa.index,y='sepal_length',data=setosa,ax=axes[0,1],marker="o") # Apdapted from https://seaborn.pydata.org/generated/seaborn.scatterplot.html . Makes a scatter plot with x-axis (index), y-axis (petal length), hued by species in axes postion 0,0. Style/markers by species.
sns.scatterplot(x=vi.index,y='sepal_length',data=vi,ax=axes[0,1],marker="s")
sns.scatterplot(x=ve.index,y='sepal_length',data=ve,ax=axes[0,1],marker="D")


sns.scatterplot(x=setosa.index,y='petal_width',data=setosa,ax=axes[1,0],marker="o") # Apdapted from https://seaborn.pydata.org/generated/seaborn.scatterplot.html . Makes a scatter plot with x-axis (index), y-axis (petal length), hued by species in axes postion 0,0. Style/markers by species.
sns.scatterplot(x=vi.index,y='petal_width',data=vi,ax=axes[1,0],marker="s")
sns.scatterplot(x=ve.index,y='petal_width',data=ve,ax=axes[1,0],marker="D")

sns.scatterplot(x=setosa.index,y='sepal_width',data=setosa,ax=axes[1,1],marker="o") # Apdapted from https://seaborn.pydata.org/generated/seaborn.scatterplot.html . Makes a scatter plot with x-axis (index), y-axis (petal length), hued by species in axes postion 0,0. Style/markers by species.
sns.scatterplot(x=vi.index,y='sepal_width',data=vi,ax=axes[1,1],marker="s")
sns.scatterplot(x=ve.index,y='sepal_width',data=ve,ax=axes[1,1],marker="D")
g1.suptitle("Measurements of Petal/Sepal widths/lengths by species") # Adds a super-title to the figure
plot.legend(("setosa","virginica","versicolor"),bbox_to_anchor=(1.01, 0, 0.3, 1), loc="lower left", mode="expand", ncol=1)
plot.subplots_adjust(right=0.8) # Adapted from from https://stackoverflow.com/a/29814281 Adjusts the top of the plot to make room for the super-title.
plot.show()


#f , axes = plot.subplots(nrows=2,ncols=2)  # Adpated from https://matplotlib.org/gallery/subplots_axes_and_figures/subplots_demo.html . Make a figure and axes object for subplot with 2 rows and 2 columns
#sns.scatterplot(x=dfs.index,y='petal_length',data=dfs,hue='species',ax=axes[0,0],style='species') # Apdapted from https://seaborn.pydata.org/generated/seaborn.scatterplot.html . Makes a scatter plot with x-axis (index), y-axis (petal length), hued by species in axes postion 0,0. Style/markers by species.
#sns.scatterplot(x=dfs.index,y='sepal_length',data=dfs,hue='species',ax=axes[0,1],style='species')
#sns.scatterplot(x=dfs.index,y='petal_width',data=dfs,hue='species',ax=axes[1,0],style='species')
#sns.scatterplot(x=dfs.index,y='sepal_width',data=dfs,hue='species',ax=axes[1,1],style='species')
#f.suptitle("Measurements of Petal/Sepal widths/lengths by species") # Adds a super-title to the figure
#plot.show()

sns.violinplot(data=dfs,x='species',y='petal_length')
plot.show()

sns.violinplot(data=dfs,x='species',y='petal_width')
plot.show()

sns.violinplot(data=dfs,x='species',y='sepal_length')
plot.show()

sns.violinplot(data=dfs,x='species',y='sepal_width')
plot.show()