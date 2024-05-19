import numpy as np
import matplotlib.pyplot as plt
uk_cities=np.array([0.04,0.56,0.62,9.7])                    #Set array
china_cities=np.array([0.58,8.4,22.2,29.9])                 #Set array
print(uk_cities)
print(china_cities)
x=["a","b","c","d"]                                         #Set the X-axis coordinates
plt.title("bar.graph")                                      #Set the title
plt.grid(ls="--",alpha=0.5)
plt.bar(x,uk_cities,ec="r",ls="--",lw=2)                    #Draw bar chart and trace it in red 
plt.show()
plt.clf()
plt.bar(x,china_cities,ec="y",ls="--",lw=2)                 #Draw bar chart and trace it in yellow
plt.show()
plt.clf()