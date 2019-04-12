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



#g=sns.relplot(x=dfs.index,y="sepal_length",hue="species",style="species",data=dfs)
#g.set(xlabel='Index')
#plot.show()



f , axes = plot.subplots(1,2)
sns.relplot(x=dfs.index,y='petal_length',data=dfs,ax=axes[0],hue='species')
sns.relplot(x=dfs.index,y='sepal_length',data=dfs,ax=axes[1],hue='species')
plot.show()