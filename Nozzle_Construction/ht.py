#Heat transfer pseudocode --first try
#--Erin Schmidt

#Objective is to plot flow parameters along nozzle length

#Note** use python 3, otherwise fix division, print etc.

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from math import sqrt, pi

#jupyter magic words
#%config InlineBackend.figure_formats=['svg']
#%matplotlib inline

#constants
T_chamber = 5485 #or whatever, chamber temp
k = 1.4 #or whatever, ratio of specific heats
mdot = 1.03 #choked mass flow rate (e.g. mdot at throat)
R =  1544/24.029 #specific gas constant (from CEA)
p_exit = 14.4 #exit pressure (assuming optimal expansion)
p_chamber_ns = 350 # or whatever, total chamber pressure
rth = 0.394
r0 = rth * 10

#init. arrays
n = 0 
it = 1000 #number of sampled points
T = [T_chamber] #temperature
p = np.linspace(p_chamber_ns, p_exit, it) #pressure
V = [R*T[n]/p[n]] #specific vol
Mach = [0.06] #Mach number
v = [Mach[n]*sqrt(2*k*R*T[0])] #velocity
A = [mdot*V[n]/v[n]] #cross-sectional area
x = [0] #length
#Also add Pr, Re, Nu, h, etc, etc...

#start loop for flow properties
n = 1
while n < it:
	V.append(V[0]*(p[0]/p[n])**(1/k))
	T.append(T[0]*(p[n]/p[0])**((k-1)/k))
	v.append(sqrt(2*k*R*T[0]/(k-1)*(1-(p[n]/p[0])**((k-1)/k))))
	Mach.append(v[n]/(sqrt(k*R*T[n])))

	if Mach[n] <= 1:
		A.append(mdot*V[n]/v[n])
		x.append(-sqrt(A[n]/pi) + r0)
		nn = n
		At = A[nn]
		rt = sqrt(At/pi)
	else:
		A.append(mdot*V[n]/v[n])
		x.append((sqrt(A[n]/pi) - rt)/2 + x[nn])
	n += 1

#print(nn)

#check if these number match, otherwise debug
print("Mach at exit = %f" % Mach[-1])
print("Pressure at exit = %f" % p[-1])
print("Temperature at exit = %f" % T[-1])
print("Velocity at exit = %f" % v[-1])
print("Radius at throat c.f {} = {}".format(rth, rt))

plt.plot(x, p) #really should be a plot vs x
plt.title("yada yada vs. thingamajig")
plt.ylabel("whichever variable")
plt.xlabel("x [in or m or whatever]")
plt.show()


