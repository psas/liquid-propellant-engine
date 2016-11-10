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
rth = 0.394 #throat radius, should converge
r0 = rth * 10 #chamber diameter defined however

#init. arrays
n = 0 
it = 1000 #number of sampled points
T = [T_chamber] #temperature
p = np.linspace(p_chamber_ns, p_exit, it) #pressure
V = [R*T[n]/p[n]] #specific vol
Mach = [0.06] #Mach number
v = [Mach[n]*sqrt(2*k*R*T[0])] #velocity
x = [0] #length
r = [r0] #radius
A = [pi*r[0]**2] #cross-sectional area
#Also add Pr, Re, Nu, h, etc, etc...

#start loop for flow properties
n = 1
while n < it:
	V.append(V[0]*(p[0]/p[n])**(1/k))
	T.append(T[0]*(p[n]/p[0])**((k-1)/k))
	v.append(sqrt(2*k*R*T[0]/(k-1)*(1-(p[n]/p[0])**((k-1)/k))))
	Mach.append(v[n]/(sqrt(k*R*T[n])))
	A.append(mdot*V[n]/v[n])
	r.append(sqrt(A[n]/pi))
   #Also add Pr, Re, Nu, h, etc, etc...
	if Mach[n] <= 1:
		x.append(0.5*(r[0]-r[n])) #placeholder linear function
		nn = n #throat index
	else:
		x.append((r[n]-r[nn])/3 + x[nn]) #placeholder linear function
	n += 1

#these numbers should match w/ old outputs when the actual geometry is input
print("Mach number at exit = %f" % Mach[-1])
print("Pressure at throat = %f [psi]" % p[nn])
print("Temperature at exit = %f [units?]" % T[-1])
print("Velocity at exit = %f [ft/s]" % v[-1])
rth_simd = "%.4f" % r[nn]
print("Radius at throat = {} (c.f {}) [units?]".format(rth_simd, rth))
print("Expansion ratio = {} (c.f {})".format(A[-1]/A[nn], '3-ish?'))
print("Contraction ratio = {} (c.f {})".format(A[0]/A[nn], '10-ish?'))

#plots
f, (ax1, ax2, ax3, ax4) = plt.subplots(4, sharex=True)
plt.xlim(0, 1.8)
ax1.plot(x, r)
ax1.set_ylabel("r")
ax1.set_title('yada yada vs. thingamajig')
ax2.plot(x, T)
ax2.set_ylabel("T")
ax3.plot(x, p)
ax3.set_ylabel("p")
ax4.plot(x, Mach)
ax4.set_ylabel("Mach")
ax4.set_xlabel("x")
plt.show()


