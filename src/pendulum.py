from scipy.integrate import ode #Object oriented solver API
import numpy as np #Numerical routines

def f(t,y,k=1.):
    """
    Right hand side of the pendulum equation.
    """
    return np.array([ y[1], -k*np.sin(y[0]) ])

def Df(t,y,k=1.):
    """
    Jacobian of the right hand side of the pendulum equation.
    """
    return np.array([ [ 0,1 ], [-np.cos(y[0]), 0 ] ])

def E(y,k=1.):
    """
    Pendulum energy.
    """
    yt = y.T
    return 0.5*yt[:,1]**2 + k*(1 - np.cos(yt[:,0]))


def solve_ode(y0=[0.,1.], k=1, tmax=10.,dt=1.e-1,solver="dop853"):
    """
    Example solver using the scipy.integrate.ode API
    """
    s = ode(f)
    s.set_f_params(k)
    s.set_initial_value(y0,0)
    s.set_integrator(solver)

    Y = [y0]
    T = [0.]
    while s.t < tmax:
        Y.append(s.integrate(s.t+dt))
        T.append(s.t)

    return {"t":np.array(T),"y":np.array(Y).T}

def euler(t=[0.,10.],y0=[0.,1.],nsteps=100,k=1):
    """
    Euler's method
    """
    T = np.linspace(t[0],t[1],nsteps)
    h = T[1]-T[0]

    Y = [ y0 ]

    for t in T[1:]:
        Y.append( Y[-1] + h*f(t,Y[-1],k) )

    return {"t":T, "y":np.array(Y).T}
