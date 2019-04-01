# Created by Adrian Donohoe 01/04/2019

import pandas as pd
import matplotlib.pyplot as plot

df = pd.read_csv('iris.csv')

# Adapted from https://stackoverflow.com/a/17071908

setosa = df.loc[df['species'] == 'setosa']
virginica = df.loc[df['species'] == 'virginica']
versicolor = df.loc[df['species'] == 'versicolor']

plot.plot(setosa['sepal_length'],'b-')
plot.show()