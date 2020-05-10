#coding: UTF-8
import math
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

def eq_S(S,I):
    return -beta*S*I

def eq_I(S,I):
    return beta*S*I-gamma*I

def eq_R(I):
    return gamma*I

def calc_k1(p,func,h):
    return h*func(p)

def calc_k2(p,q,func,h):
    return h*func(p,q)

def RungeKutta1(p,func,h):
        k_1 = calc_k1(p,func,h)
        k_2 = calc_k1(p+0.5*h*k_1,func,h)
        k_3 = calc_k1(p+0.5*h*k_2,func,h)
        k_4 = calc_k1(p+h*k_3,func,h)
        k=(k_1+2*k_2+2*k_3+k_4)/6
        return h*k

def RungeKutta2(p,q,func,h):
        k_1 = calc_k2(p,q,func,h)
        k_2 = calc_k2(p+0.5*h*k_1,q+0.5*h*k_1,func,h)
        k_3 = calc_k2(p+0.5*h*k_2,q+0.5*h*k_2,func,h)
        k_4 = calc_k2(p+h*k_3,q+h*k_3,func,h)
        k=(k_1+2*k_2+2*k_3+k_4)/6
        return h*k

#initial settings50
total_population = 10000000
beta = 2e-14
gamma= beta/5

total_time = 1000000
h = 0.1
time_cycle = int(total_time/h)

S = np.zeros(time_cycle+1)
I = np.zeros(time_cycle+1)
R = np.zeros(time_cycle+1)
RR = np.zeros(time_cycle+1)
S[0] = 0.999999*total_population
I[0] = 0.000001*total_population
R[0] = total_population-S[0]-I[0]

for t in range(time_cycle):
    S[t+1] = S[t]+RungeKutta2(S[t],I[t],eq_S,h)
    I[t+1] = I[t]+RungeKutta2(S[t],I[t],eq_I,h)
    R[t+1] = total_population-S[t+1]-I[t+1]

#figure 
time = np.arange(time_cycle+1)


#plt.plot(time,S)
plt.plot(time,I)
plt.plot(time,R)
plt.legend(['I','R'])

plt.savefig('tokyo')

