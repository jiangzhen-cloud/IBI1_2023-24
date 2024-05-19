Sleep=8                                                                              #The requested activity that can be modified.
dic={"Sleeping":Sleep,"Classes":6,"Studying":3.5,"TV":2,"Music":1,"other":11.5-Sleep}           #Create a dictionary
import matplotlib.pyplot as plt
class_labels=["Sleeping","Classes","Studying","TV","Music","other"]                  #Set up the labels
time_week=[Sleep,6,3.5,2,1,11.5-Sleep]                                                          #Set the data
Studying_and_esle=[0,0,0.1,0,0,0]                                                    #Set the highlighted sections
plt.figure()
plt.pie(time_week,labels=class_labels,startangle=90,explode=Studying_and_esle)       #Draw the pie chart
plt.show()
plt.clf()
Sleeping_time=dic["Sleeping"]
print(Sleeping_time)                                                                 #Output the number of hours spent sleeping