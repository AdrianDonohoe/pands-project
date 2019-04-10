# Verbatim from https://seaborn.pydata.org/examples/scatterplot_matrix.html
# In week 12 videos we saw how some Iris plots were done in seaborn. It is much simpler code and only took a few minutes to put together. In my view the seaborn plots are visually better but seeing as I spent hours putting the matplotlib ones together myslef, they can stay in the project.
import seaborn as sns
import matplotlib.pyplot as plot

sns.set(style="ticks")
dfs = sns.load_dataset("iris")
sns.pairplot(dfs, hue="species")
plot.show()