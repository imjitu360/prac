## 1)Import Require Libraries
import pandas as pd #library for read data
import matplotlib.pyplot as plt #library for visulize data
## 2)Import Dataset 
dataset=pd.read_csv('Iris.csv')
dataset.head()
dataset.tail()
## 3)Prepare Scatter-Plot
dataset.plot(kind="scatter",x="SepalLengthCm",y="SepalWidthCm",color="red")
plt.grid()
### ANOTHER WAY 
dataset.plot.scatter(x="SepalLengthCm",y="SepalWidthCm").grid()