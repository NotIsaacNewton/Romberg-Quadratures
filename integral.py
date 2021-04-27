#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 14:21:25 2021

@author: ariandovald
"""

import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
import methods as met

#USER-DEFINED CONSTANTS AND VARIABLES
A = -4.5
B = 5.5
STEPS = 1

#FUNCTION TO BE INTEGRATED
def f(x):
    '''calculates y given x'''
    y = np.tanh(x)
    return y

#MAKE PLOT OF FUNCTION
t = np.linspace(A+A*(5**(-1)), B+B*(5**(-1)), int(round((B-A)*100)))
plt.plot(t, f(t), color="black")
plt.fill_between(np.linspace(A, B, int(round((B-A)*100))), f(np.linspace(A, B, int(round((B-A)*100)))))

#CALCULATION OF DELTA_X
DELTA_X = (B-A)*(STEPS**(-1))

#ARRAYS
I = [[0]]
ordsum = [0]

#ROMBERG QUADRATURE METHOD WITH TRAPEZOIDAL SUMS
ordsum.append(met.trapezoidal_ordsum(STEPS, A, B, A, B, DELTA_X, f)) #CALCULATE FIRST ORDINATE SUM
I[0].extend([ordsum[-1] * DELTA_X]) #CALCULATE FIRST INTEGRAL

DELTA_I = 10 #SET DIFFERENCE TO START LOOP
N = 1
while DELTA_I > 0.001:
    STEPS_NEW = STEPS * (2**(N-1)) #DOUBLE THE NUMBER OF STEPS
    DELTA_X_NEW = DELTA_X * (0.5**(N-1)) #CALCULATE NEW DELTA-X
    a_new = A + (DELTA_X * (0.5**N)) #CALCULATE NEW STARTING POINT
    b_new = B - (DELTA_X * (0.5**N)) #CALCULATE NEW ENDING POINT
    ordsum.append(ordsum[-1] +
                  met.trapezoidal_ordsum(STEPS_NEW, A, B, a_new,
                                         b_new, DELTA_X_NEW, f)) #UPDATE ORDINATE SUM
    I[0].extend([ordsum[-1] * (DELTA_X * (0.5**N))]) #UPDATE INTEGRAL ARRAY

    k = 1
    while (k-1) < N:
        if k == N:
            I.append([((4**k * I[k-1][-1]) -
                       I[k-1][-2])/((4**k)-1)])
                            #APPLY ROMBERG QUADRATURE METHOD AND UPDATE THE TABLE
        else:
            I[k].extend([((4**k * I[k-1][-1]) -
                          I[k-1][-2])/((4**k)-1)])
                            #APPLY ROMBERG QUADRATURE METHOD AND UPDATE THE TABLE
        k += 1 #MOVE TO NEXT ITERATION

    DELTA_I = abs(I[-1][-1] - I[-2][-1]) #CALCULATE NEW DIFFERENCE BETWEEN INTEGRALS
    N += 1 #MOVE FORWARDS TO NEXT ITERATION

I[0].remove(0)
print(tabulate(I, tablefmt='fancy_grid', numalign="right",
               missingval="~", floatfmt=".3f")) #PRINT ROMBERG QUADRATURES
print(I[-1][-1]) #PRINT FINAL RESULT
