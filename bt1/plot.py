import numpy as np
from math import sin, cos, exp, tan, sqrt, pi
import matplotlib
import matplotlib.pyplot as plt

def wave(n,z,a,V0,coeff):
    z0 = a*sqrt(coeff*V0)
    l = z/a
    k = sqrt(z0**2 - z**2)/a
    
    samples = 300
    
    if n % 2 == 1:
        B = sqrt(k/(1 + k*a)) * cos(l*a) * exp(k*a)
        F = B
        D = sqrt(k/(1 + k*a))

        x1 = np.linspace(-2*a, -a, samples)
        y1 = B * np.exp(k * x1)
        
        x2 = np.linspace(-a, a, samples)
        y2 = D * np.cos(l * x2)

        x3 = np.linspace(a, 2*a, samples)
        y3 = F * np.exp(-k * x3)
    else:
        B = -sqrt(k/(1 + k*a)) * sin(l*a) * exp(k*a)
        F = -B
        C = sqrt(k/(1 + k*a))
        
        x1 = np.linspace(-2*a, -a, samples)
        y1 = B * np.exp(k * x1)
        
        x2 = np.linspace(-a, a, samples)
        y2 = C * np.sin(l * x2)
        
        x3 = np.linspace(a, 2*a, samples)
        y3 = F * np.exp(-k * x3)
        
    x = np.concatenate([x1, x2, x3])
    y = np.concatenate([y1, y2, y3])
    return x, y

def plot_wave(n,z,a,V0,coeff,scale,e_flag):
    E = -V0 + (z**2)/(coeff * (a**2))
    if e_flag == 1:
        plt.axhline(y=E, color="red",
                    linestyle="--",
                    label=f"E{n} = {E:.2f} MeV")
        
    x, y = wave(n,z,a,V0,coeff)
    y = scale * y + E
    plt.plot(x,y,color="blue")

def plot_all_waves(solutions,a,V0,coeff,scale,e_flag):
    for i in range(1,len(solutions)):
        plot_wave(i,solutions[i],a,V0,coeff,scale,e_flag)

def plot_well(a,V0):
    x = [-2*a, -a, -a,  a,  a, 2*a]
    y = [ 0,   0, -V0, -V0,   0, 0]
    plt.plot(x,y,color="black")
