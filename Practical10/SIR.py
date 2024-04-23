#Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
N=10000
beta=0.3
gamma=0.05
S=N-1             #Initial number of susceptible persons
I=1               #Initial number of infected
R=0               #Number of initial recoveries
susceptible=[S]
infected=[I]
recovered=[R]
for i in range (1,1001):
    prob_infection = beta * I / N
    infections=np.random.choice([0, 1], size=S, p=[1 - prob_infection, prob_infection])
    new_infections = np.sum(infections)                                                   #Count the actual number of infections
    S-=new_infections
    I+=new_infections
    prob_recovery = gamma
    recoveries=np.random.choice([0, 1], size=I, p=[1 - prob_recovery, prob_recovery])
    new_recoveries = np.sum(recoveries)                                                   #Count the actual number of recoveries
    I-=new_recoveries
    R+=new_recoveries
    susceptible.append(S)
    infected.append(I)
    recovered.append(R)
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(susceptible,label='Susceptible')
plt.plot(infected,label='Infected')
plt.plot(recovered,label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of individuals')
plt.title('SIR model')
plt.legend()
plt.savefig("C:/Users/17231/Desktop/work_place/IBI1_2023-24/IBI1_2023-24/Practical10/SIR_model")
plt.show()