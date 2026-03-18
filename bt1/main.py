import numpy as np
from math import sin, cos, tan, sqrt, ceil, pi
import methods

import matplotlib
import matplotlib.pyplot as plt
import plot

coeff = 0.0483

def get_z0(a,V0):
    return a*sqrt(coeff*V0)

def f_e(z0,z):
    return tan(z) - sqrt((z0/z)**2 - 1)

def df_e(z0,z):
    return 1/(cos(z)**2) + (z0**2)/((z**3)*sqrt((z0/z)**2 - 1))

def g_e(z0,z):
    return z - f_e(z0,z)/df_e(z0,z)

def f_o(z0,z):
    return -1/tan(z) - sqrt((z0/z)**2 - 1)

def df_o(z0,z):
    return 1/(sin(z)**2) + (z0**2)/((z**3)*sqrt((z0/z)**2 - 1))

def g_o(z0,z):
    return z - f_e(z0,z)/df_o(z0,z)

def get_results(n,method,a,V0,coeff,N,eps):
    z0 = a*sqrt(coeff * V0)
    nroot = ceil(2*z0/pi)

    bL = (n - 1) * pi/2 + eps
    bR = min(n * pi/2 - eps, z0 - eps)

    if n % 2 == 1:
        match method:
            case "bi":
                results = methods.bi(f_e,z0,bL,bR,N,eps)
            case "nr":
                results = methods.nr(g_e,z0,(bL+bR)/2,N,eps)
            case "sc":
                results = methods.sc(f_e,z0,bL,bL+eps,N,eps)
    else:
        match method:
            case "bi":
                results = methods.bi(f_o,z0,bL,bR,N,eps)
            case "nr":
                results = methods.nr(g_o,z0,(bL+bR)/2,N,eps)
            case "sc":
                results = methods.sc(f_o,z0,bL,bL+eps,N,eps)
    return results

def output_results(n,a,V0,filename,N,eps):
    z_bi = get_results(n,"bi",a,V0,coeff,N,eps)
    z_nr = get_results(n,"nr",a,V0,coeff,N,eps)
    z_sc = get_results(n,"sc",a,V0,coeff,N,eps)
    
    with open(filename,"w") as f:
        width = 20
        f.write(f"| {'i':^4} | {'Bisection':^{width}} | {'Newton - Raphson':^{width}} | {'Secant':^{width}} |\n")
        f.write("-"*(width*3 + 17) + "\n")
        nrow = max(len(z_bi), len(z_nr), len(z_sc))
        i = 0
        while i < nrow:
            bi_val = f"{z_bi[i]:.15f}" if i < len(z_bi) else ""
            nr_val = f"{z_nr[i]:.15f}" if i < len(z_nr) else ""
            sc_val = f"{z_sc[i]:.15f}" if i < len(z_sc) else ""
            f.write(f"| {i+1:^4} | {bi_val:^{width}} | {nr_val:^{width}} | {sc_val:^{width}} |\n")
            i += 1

def get_solutions(method,a,V0,coeff,N,eps):
    solutions = []
    solutions.append(0)

    z0 = a*sqrt(coeff * V0)
    nroot = ceil(2*z0/pi)

    for i in range(1,nroot+1):
        bL = (i - 1) * pi/2 + eps
        bR = min(i * pi/2 - eps, z0 - eps)

        if i % 2 == 1:
            match method:
                case "bi":
                    results = methods.bi(f_e,z0,bL,bR,N,eps)
                case "nr":
                    results = methods.nr(g_e,z0,(bL+bR)/2,N,eps)
                case "sc":
                    results = methods.sc(f_e,z0,bL,bL+eps,N,eps)
            z = results[-1]
            print("z_e =", z)
            solutions.append(z)

        else:
            match method:
                case "bi":
                    results = methods.bi(f_o,z0,bL,bR,N,eps)
                case "nr":
                    results = methods.nr(g_o,z0,(bL+bR)/2,N,eps)
                case "sc":
                    results = methods.sc(f_o,z0,bL,bL+eps,N,eps)
            z = results[-1]
            print("z_o =", z)
            solutions.append(z)

    return solutions

def plot_single(n,solutions,a,V0,filename,scale,e_flag,w,h):
    fig, ax = plt.subplots()
    plt.xlim(-w/2,w/2)
    plt.ylim(-h*1.1, h*0.2)

    plot.plot_wave(n,solutions[n],a,V0,coeff,scale,e_flag)
    plot.plot_well(a,V0)
	    
    plt.xlabel("x (fm)")
    plt.ylabel("Năng lượng (MeV)")
    ax.legend_ = None
    plt.savefig(filename, dpi=300)

def plot_full(solutions,a,V0,coeff,filename,scale,e_flag,w,h):
    fig, ax = plt.subplots()
    plt.xlim(-w/2,w/2)
    plt.ylim(-h*1.1, h*0.2)
    
    plot.plot_all_waves(solutions,a,V0,coeff,scale,e_flag)
    plot.plot_well(a,V0)
    
    plt.xlabel("x (fm)")
    plt.ylabel("Năng lượng (MeV)")
    ax.legend_ = None
    plt.savefig(filename, dpi=300)

N = 1000
eps = 1e-10

V0, a = 83, 2
output_results(3,a,V0,"data/results-table.txt",N,eps)
solutions = get_solutions("bi",a,V0,coeff,N,eps)
plot_single(3,solutions,a,V0,"images/plot-83-2-single.png",10,1,4*a,V0)
plot_full(solutions,a,V0,coeff,"images/plot-83-2.png",10,1,4*a,V0)

for i in range(1,3+1):
    E = -V0 + (solutions[i]**2)/(coeff * (a**2))
    x, y = plot.wave(i,solutions[i],a,V0,coeff)
    y = 10*y + E

    with open("data/energy-"+str(i)+".txt","w") as f:
        f.write(f"{x[0]} {E}\n")
        f.write(f"{x[-1]} {E}\n")

    with open("data/wave-"+str(i)+".txt","w") as f:
        for j in range(0,len(x)):
            f.write(f"{x[j]} {y[j]}\n")
            
    with open("data/potential.txt","w") as f:
        f.write(f"{x[0]} 0\n")
        f.write(f"{-a} 0\n")
        f.write(f"{-a} {-V0}\n")
        f.write(f"{a} {-V0}\n")
        f.write(f"{a} 0\n")
        f.write(f"{x[-1]} 0\n")

V0, a = 1, 1
solutions = get_solutions("bi",a,V0,coeff,N,eps)
plot_full(solutions,a,V0,coeff,"images/plot-1-1.png",1,1,4*a,2*V0)

V0, a = 0.5, 0.5
solutions = get_solutions("bi",a,V0,coeff,N,eps)
plot_full(solutions,a,V0,coeff,"images/plot-05-05.png",1,1,4*a,2*V0)

V0, a = 200, 20
solutions = get_solutions("bi",a,V0,coeff,N,eps)
plot_full(solutions,a,V0,coeff,"images/plot-200-20.png",1,0,4*a,V0)

V0, a = 500, 50
solutions = get_solutions("bi",a,V0,coeff,N,eps)
plot_full(solutions,a,V0,coeff,"images/plot-500-50.png",1,0,4*a,V0)
