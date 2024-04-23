#Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
N=10000
beta=0.3
gamma=0.05
vaccination_rates=[0,10,20,30,40,50,60,70,80,90,100]                                          #List of vaccination rates
data={f'Vaccination{rate}%':{"Infected":[]}for rate in vaccination_rates}
for vac_rate in vaccination_rates:
    S=N-int(N*vac_rate/100)
    I=1
    R=0
    infected=[]
    for i in range (1,1001):
        prob_infection = beta * I / N                                                         #Infection probability
        infections=np.random.choice([0, 1], size=S, p=[1 - prob_infection, prob_infection])
        new_infections = np.sum(infections)                                                   #Count the actual number of infections
        S-=new_infections
        I+=new_infections
        prob_recovery = gamma
        recoveries=np.random.choice([0, 1], size=I, p=[1 - prob_recovery, prob_recovery])
        new_recoveries = np.sum(recoveries)                                                   #Count the actual number of recoveries
        I-=new_recoveries
        R+=new_recoveries
        infected.append(I)
    data[f'Vaccination{vac_rate}%']['Infected']=infected                                      #Store data
#Plot result
plt.figure(figsize=(6, 4), dpi=150)
for key,value in data.items():
    plt.plot(value['Infected'],label=key+'-Infected')
plt.xlabel('Time')
plt.ylabel('Number of individuals')
plt.title('SIR model with different vaccination rates')
plt.legend()
plt.savefig("C:/Users/17231/Desktop/work_place/IBI1_2023-24/IBI1_2023-24/Practical10/SIR_model_with_different_vaccination_rates")
plt.show()