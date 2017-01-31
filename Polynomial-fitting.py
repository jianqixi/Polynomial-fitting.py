#!/usr/bin/env python

###The first step for hexagonal structure lattice parameters
###Polynomial fitting to determine the minimum energy and corresponding c/a in different a range
import numpy as np
import sys, os, math
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
from sympy import *
from sympy.solvers import solve

#read raw data from txt files
fitting=open("sum",'r')

#define the ratio of c to a as c_a and the corresponding energy
ratio=[]
energy=[]

#read data and store to the list of c_a[] and energy[]
while 1:
 data=fitting.readlines()
 if not data:
   break
 else:
   for i in range(0,5):    #the loop for read these data
      ratio.append(float(data[i].split()[1]))
      energy.append(float(data[i].split()[2]))


#make a vector to evaluate fits on with a lot of points so it looks smooth
step=np.linspace(min(ratio),max(ratio),500)

#convert the list of c_a[] and energy[] to arrays for further fitting using polyfit function
r=np.asarray(ratio)
e=np.asarray(energy)
#print r 
#print e
#fitting the data using 3-order polynomial
#define the coefficients a, b, c, d
a,b,c,d=np.polyfit(r,e,3)

#plot the polynomial curve
#plt.plot(r,e,'ro')
#plt.plot(step,a*step**3+b*step**2+c*step+d,'--')
#plt.xlabel('c/a')
#plt.ylabel('Energy (eV)')
#plt.savefig('First',bbox_inches='tight',dpi=300)

#sample function
def g(x):
 return a*x**3+b*x**2+c*x+d

#derivative function
x=symbols('x')
der=diff(a*x**3+b*x**2+c*x+d)
#print der

#solve the derivative function and get the extremal point
ratio_value=solve(der)
print ratio_value

#convert the list of ratio_value[] into array for further function calculation
r_value=np.asarray(ratio_value)
energy_value=g(r_value)
print energy_value




