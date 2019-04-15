# Verbatim from https://seaborn.pydata.org/examples/scatterplot_matrix.html
# In week 12 videos we saw how some Iris plots were done in seaborn. It is much simpler code and only took a few minutes to put together. In my view the seaborn plots are visually better but seeing as I spent hours putting the matplotlib ones together myslef, they can stay in the project.
import seaborn as sns
import matplotlib.pyplot as plot

sns.set(style="ticks")
dfs = sns.load_dataset("iris")
g=sns.pairplot(dfs, hue="species",markers=["o","s","D"])
g.fig.suptitle("Sepal/Petal width/length pair plots") # Adapted from https://stackoverflow.com/a/49594152
plot.subplots_adjust(top=0.9) # Adapted from from https://stackoverflow.com/a/29814281
plot.show()



f , axes = plot.subplots(nrows=2,ncols=2)  # Adpated from https://matplotlib.org/gallery/subplots_axes_and_figures/subplots_demo.html
sns.scatterplot(x=dfs.index,y='petal_length',data=dfs,hue='species',ax=axes[0,0]) # Apdapted from https://seaborn.pydata.org/generated/seaborn.scatterplot.html
sns.scatterplot(x=dfs.index,y='sepal_length',data=dfs,hue='species',ax=axes[0,1])
sns.scatterplot(x=dfs.index,y='petal_width',data=dfs,hue='species',ax=axes[1,0])
sns.scatterplot(x=dfs.index,y='sepal_width',data=dfs,hue='species',ax=axes[1,1])
f.suptitle("Measurements of Petal/Sepal widths/lengths by species")
plot.show()