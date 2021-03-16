"""
ecam Mar21

Example of use of pendulum.py
"""

import matplotlib.pyplot as plt
import numpy as np
from pendulum import f,Df,euler
from scipy.integrate import solve_ivp


#Solve the equation using the Euler method with default values
r_euler = euler()

#Plot the solution
plt.figure() #New figure
plt.plot(r_euler["t"],r_euler["y"][0,:])


#Solve the equation using Radau's method
r_radau = solve_ivp(f,[0,100],[0,1],"Radau",t_eval=np.linspace(0,100,1000),jac=Df)

#Plot the phase plane
plt.figure() #New figure
plt.plot(r_radau["y"][0,:],r_radau["y"][1,:])

#Solve using lsoda
r_lsoda = solve_ivp(f,[0,100],[0,1],"Radau",t_eval=np.linspace(0,100,1000),jac=Df)

#Plot energy
plt.figure()
plt.plot(r_lsoda["y"][0,:],r_lsoda["y"][1,:])
