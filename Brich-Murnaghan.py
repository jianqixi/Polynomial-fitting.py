#!/usr/bin/env python

'''Example of fitting the Birch-Murnaghan EOS to data'''
import numpy as np
import sys, os, math
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

#read raw data from txt files
fitting=open("ratio-energy-second.txt",'r')

#define the ratio of c to a as c_a and the corresponding energy
lattice=[]
ratio=[]
energy=[]
volume=[]
#read data and store to the list of c_a[] and energy[]
while 1:
 data=fitting.readlines()
 if not data:
   break
 else:
   for i in range(0,15):
#      lattice.append(float(data[i].split()[0]))
      volume.append(float(data[i].split()[0]))
      energy.append(float(data[i].split()[2]))

#convert the list of c_a[] and energy[] to arrays for further fitting using polyfit function
Vols=np.asarray(volume)
#ratio_value=np.asarray(ratio)
Energies=np.asarray(energy)

#Vols=math.sqrt(3.0)*1.5*lat**3*ratio_value
#print Vols

#define the Brich-Murnaghan function based on Computational Materials Science 47 (2010) 1040-1048
def BM(parameters, V):
   E0=parameters[0]
   B0=parameters[1]
   BP=parameters[2]
   V0=parameters[3]

   a=E0+(9*B0*V0*(6-BP))/16
   b=(-9*B0*V0**(5.0/3.0)*(16-3*BP))/16
   c=(9*B0*V0**(7.0/3.0)*(14-3*BP))/16
   d=(-9*B0*V0**3*(4-BP))/16
   E=a+b*V**(-2.0/3.0)+c*V**(-4.0/3.0)+d*V**(-6.0/3.0)
   return E

#minimize above function
def objective(pars, y, x):
   err=y-BM(pars,x)
   return err

#initial guess of parameters
x0=[-194,1.0,5,323]         #For B0 the unit is eV/A^3, should *160.21773 GPa

plsq = leastsq(objective,x0,args=(Energies, Vols))
print 'Fitted parameters = {0}'.format(plsq[0])
#plt.plot(Vols,Energies,'ro')
#make a vector to evaluate fits on with a lot of points so it looks smooth
x = np.linspace(min(Vols),max(Vols),100)
y = BM(plsq[0],x)
#plt.plot(x,y,'k-')
#plt.xlabel('volume')
#plt.ylabel('energy')
#plt.savefig('BM curve.png')
