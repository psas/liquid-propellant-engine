#Heat transfer pseudocode --first try
#--Erin Schmidt

#Objective is to plot flow parameters along nozzle length

#Note** use python 3, otherwise fix division, print etc.

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from math import sqrt

#jupyter magic words
#%config InlineBackend.figure_formats=['svg']
#%matplotlib inline

#constants
T_chamber = 3500 #or whatever, chamber temp
k = 1.4 #or whatever, ratio of specific heats
mdot = 1 #choked mass flow rate (e.g. mdot at throat)
R =  1 #specific gas constant (from CEA)
p_exit = 14.4 #exit pressure (assuming optimal expansion)
p_chamber_ns = 375 # or whatever, total chamber pressure

#init. arrays
n = 0 
it = 10 #number of sampled points
T = [T_chamber] #temperature
p = np.linspace(p_chamber_ns, p_exit, it) #pressure
V = [R*T[n]/p[n]] #specific vol
v = [0] #velocity
Mach = [0] #Mach number
A = [] #cross-sectional area
x = [] #length
#Also add Pr, Re, Nu, h, etc, etc...

#start loop for flow properties
n = 1
while n < it:
	V.append(V[n-1]*(p[n-1]/p[n])**(1/k))
	T.append(T[n-1]*(p[n]/p[n-1])**((k-1)/k))
	v.append(sqrt(2*k*R*T[n-1]/(k-1)*(1-(p[n]/p[n-1])**((k-1)/k))))
	Mach.append(v[n]/(sqrt(k*R*T[n])))
	A.append(mdot*V[n]/v[n])
	#Also add Pr, Re, Nu, h, etc, etc...
#	if Mach[n] < 1:
#		x.append("some defined function of A")
#	else:
#		x.append("some other defined function of A")	
	n += 1

plt.plot(A, T) #really you want to plot vs. x
plt.title("yada yada vs. thingamajig")
plt.ylabel("whichever variable")
plt.xlabel("x [in or m or whatever]")
plt.show()


