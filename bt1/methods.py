# import numpy as np
# import matplotlib.pyplot as plt
# from math import tan, sqrt

# Bisection
def bi(f,z0,a,b,N,eps):
    results = []

    if f(z0,a) * f(z0,b) > 0:
        print(f"Interval [{a,b}] does not contain root because f(a) is of the same sign as f(b)")
        return results

    i = 1
    while i <= N:
        c = (a+b)/2
        results.append(c) 
        if abs(f(z0,c)) < eps: 
            break

        if f(z0,a)*f(z0,c) < 0: 
            b = c 
        else: 
            a = c

        i += 1

    return results

# Newton-Rapshon:
def nr(g,z0,p0,N,eps):
    results = []

    i = 1
    while i <= N:
        p = g(z0,p0)
        results.append(p)

        if abs(p-p0) < eps:
            break

        p0 = p
        i += 1

        if i > N:
            print("Newton - Raphson method failed after",N,"iterations")

    return results

# Secant
def sc(f,z0,p1,p2,N,eps):
    results = []

    fp1 = f(z0,p1)
    fp2 = f(z0,p2)

    i = 1    
    while i <= N:
        if abs(fp2 - fp1) < eps:
            print("Ham phan ky")
            break

        p = p2 - (fp2 * (p2 - p1)/(fp2 - fp1))
        results.append(p)

        if abs(p - p2) < eps:
            break
        
        p1 = p2
        fp1 = fp2
        p2 = p
        fp2 = f(z0,p)
        i += 1

        if i > N:
            print("Phuong phap Secant that bai sau",N,"lan lap")
        
    return results
