#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
#Pick the first infected person at random
population=np.zeros((100,100))
outbreak=np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]]=1
#Set parameters
beta=0.3
gamma=0.05
time_steps=100
#Draw initial situation
plt.figure(figsize=(6,4),dpi=150)
plt.imshow(population,cmap="viridis",interpolation="nearest")
plt.title("Initial State")
plt.show()
plt.close()
for t in range(time_steps):
# find infected points
    infectedIndex = np.where(population==1)
# loop through all infected points
    for i in range(len(infectedIndex[0])):
    # get x, y coordinates for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
    # infect each neighbour with probability beta
    # infect all 8 neighbours (this is a bit finicky, is there a better way?):
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
            # don't infect yourself! (Is this strictly necessary?)
                if (xNeighbour,yNeighbour) != (x,y):
                # make sure I don't fall off an edge
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                    # only infect neighbours that are not already infected!
                        if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
    recover=np.random.choice([0,1],len(infectedIndex[0]),p=[1-gamma,gamma])
    population[infectedIndex[0][recover==1],infectedIndex[1][recover==1]]=2
    #Every 15 time draw a result
    if t%15==0 or t==time_steps:
        plt.figure(figsize=(6,4),dpi=150)
        plt.imshow(population,cmap="viridis",interpolation="nearest",vmin=0,vmax=2)
        plt.title(f"step{t+1}")
        plt.savefig("C:/Users/17231/Desktop/work_place/IBI1_2023-24/IBI1_2023-24/Practical10/spatial_SIR_model")
        plt.show()
        plt.close()