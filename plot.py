import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

date = np.loadtxt('SIR.csv',dtype=str,delimiter=',',usecols=0)
n_infected = np.loadtxt('SIR.csv',delimiter=',',usecols=1)

print(date.dtype)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(date,n_infected)

xfmt = mdates.DateFormatter("%m%d")
xloc = mdates.DayLocator()


ax.xaxis.set_major_locator(xloc)
ax.xaxis.set_major_formatter(xfmt)
ax.set_xlim(datetime.datetime(2020,1,27), datetime.datetime(2020,5,6)) 
plt.savefig('seni')

