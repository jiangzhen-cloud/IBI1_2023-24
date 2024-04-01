import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir('C:/Users/17231/Desktop/work_place/IBI1_2023-24/IBI1_2023-24/Practical7')
print(os.getcwd())
print(os.listdir())
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
print(dalys_data.head(5))
print(dalys_data.info())
print(dalys_data.describe())
print(dalys_data.iloc[0,3])
print(dalys_data.iloc[2,0:5])
print(dalys_data.iloc[0:2,:])
print(dalys_data.iloc[0:10:2,0:5])
my_columns = [True, True, False, True]
print(dalys_data.iloc[0:3,my_columns])
print(dalys_data.loc[2:4,"Year"])
print(dalys_data.iloc[:,0])
a=dalys_data["Entity"]=="Afghanistan"
print(dalys_data[a].iloc[:,3])
print(dalys_data[a].iloc[:,3]==dalys_data.loc[0:29,"DALYs"])
china_data=dalys_data["Entity"]=="China"
print(dalys_data[china_data])
import numpy as np
b=np.array([dalys_data[china_data].iloc[:,3]])
print(np.mean(b))                                                                  # Calculate the average.
c=dalys_data[china_data].iloc[29,3] 
print(np.mean(b)>c)                                                                # The DALYs in China in 2019 was less than the mean.
plt.plot(dalys_data[china_data].Year, dalys_data[china_data].DALYs, 'b+')
plt.xticks(dalys_data[china_data].Year,rotation=-90)
plt.show()                                                                         # The DALYs data in China were plotted.
d=dalys_data["Entity"]=="England"
print(dalys_data[d].iloc[:,3])
plt.plot(dalys_data[d].Year,dalys_data[d].DALYs, "b+")
plt.xticks(dalys_data[d].Year,rotation=-90)
plt.show()                                                                         # The DALYs data in England were plotted.
