

# Design Documentation for the 2kN Heat Sink Engine #

In an attempt to wrangle some design requirements into a single location, this document is to serve as a first-location reference for design variables and documentation.

## Basic Parameters ##

* Thrust: 500lbf (2.2kN)
* Chamber Pressure: 350psia (2.41 MPa)
* Exit Pressure: 14.7 psia (0.101 MPa)
* Oxidizer: Liquid Oxygen
* Fuel: Isopropyl alcohol, 70% by volume

## Injector Parameters ##

### Flowrates:
* Fuel: 0.87 lb/sec (0.394 kg/sec)
* Oxidizer: 1.13 lb/sec (0.513 kg/sec)
* Total: 2.0 lb/sec (0.907 kg/sec)

*(Note: these values are from the PSAS LFE python notebook scripts. May vary slightly if using RPA to calculate flowrates.)*
	
### Pressure Loss ###

* Pressure loss target = 70 psi (483 kPa) for Pintle and Annulus

Pressure target for the injector is 20% of the chamber pressure. This is not a precise target and sourcing is pretty sketchy, so this is a somewhat squishy number, however with a 350psi chamber pressure, we are shooting for 70 psi (483 kPa) pressure loss through the injector. There is more discussion in Jacob Tiller's pintle documentation, however the general idea is there needs to be enough pressure drop to accelerate the fluids and cushion upstream from combustion instability, but there is a clear upper limit created by the cavitating venturis upstream of the injector.


### Fluid Velocities ###

* The fluid velocity target range is ~30-100 ft/s (~10-30 m/s). 

This is a range from recollection. This value can be found by calculated from flowrates & total orifice areas. This value is necessary to calculate the momentum ratio, which helps define the combination fan angle of the fluids. 

Bonus points if you can find the sourcing for this information. Marc has lost it... if you do, please add reference here. Probably can be found in Huzel & Huang. 

### Momentum Ratio ###

* The target momentum ratio for the injector is 1:1

Fluid momentum is mdot*V, as explained in Jacob Tiller's pintle documentation. The momentum ratio of the fluids dictates the combined angle of the flow from the axial fuel and radial oxidizer flows. The target angle is 45 degrees, corresponding to a 1:1 momentum ratio.


## Strategy ##

CAD design strategy here...
