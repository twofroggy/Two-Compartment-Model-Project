#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 22:30:33 2021

@author: tiffwong
"""
import matplotlib.pyplot as plt
import numpy as np 

#%% regular data 

x1 = [0.623, 0.374, 0.249, 0.183, 0.145, 0.120, 0.103, 0.089, 0.078, 0.068, 0.060, 
      0.053 , 0.047 , 0.041 , 0.037] 

x2 = [0.000, 0.113, 0.151, 0.157, 0.150, 0.137, 0.124, 0.110, 0.098, 0.087, 0.077 , 
      0.068 , 0.060 , 0.053 , 0.047] 

t = [0.000, 7.143, 14.286, 21.429, 28.571, 35.714, 42.857, 50, 57.143, 64.286, 71.429, 78.571, 85.714, 92.857,100] 


plt.scatter(t, x1, label = "x1 data", marker='o') 
plt.scatter(t, x2, label = "x2 data", marker='o') 
plt.plot(t, x1, label = "est_x1", marker='o') 
plt.plot(t, x2, label = "est_x2", marker='o')

plt.xlabel('Time, t') 
plt.ylabel('Compartment Concentration Measurements, mg/mL')

plt.title("Observed vs. Predicted Compartment Concentration") 

plt.legend() 
plt.show()

#%% ln data 
x2 = [0.113, 0.151, 0.157, 0.150, 0.137, 0.124, 0.110, 0.098, 0.087, 0.077 , 
      0.068 , 0.060 , 0.053 , 0.047] 

lnx1 = np.log(x1) 
lnx2 = np.log(x2) 
lnx2 = np.append(lnx2,0)

plt.plot(t, lnx1, label = "ln(x1) data", marker='o') 
plt.plot(t, lnx2, label = "ln(x2) data", marker='o') 

plt.xlabel('Time, t') 
plt.ylabel('ln(Compartment Concentration Measurements), mg/mL')

plt.title("ln(Data) versus Model") 

plt.legend(loc = "upper right") 
plt.show()