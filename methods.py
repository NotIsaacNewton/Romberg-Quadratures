#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 14:21:29 2021

@author: ariandovald
"""

import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate


# CREATING CLASS
class math:

    def __init__(self, equation):
        self.equation = equation

    def f(self, x):
        """calculates y given x"""
        y = self.equation(x)
        return y

    # TRAPEZOIDAL ORDINAL SUM
    def trapezoidal_ordsum(self, steps, a, b, a_new, b_new, delta_x, f) -> float:
        """calculates a trapezoidal ordinate sum for a given function f and
        endpoints a and b"""
        ordsum = np.float64(0)
        x = a_new  # SET STARTING POINT FOR X

        if a == a_new and b == b_new:  # CHECK IF THIS IS THE FIRST ITERATION OR NOT
            ordsum += 0.5 * f(x)  # ADD HALF OF THE STARTING ENDPOINT
            for n in range(1, steps - 1):
                # REPEAT LOOP FROM AFTER STARTING ENDPOINT TO BEFORE ENDING ENDPOINT
                x = a + (n * delta_x)  # UPDATE X BY ADDING N * DELTA_X
                ordsum += f(x)  # ADD TO ORDINATE SUM
            ordsum += 0.5 * f(x + delta_x)  # ADD HALF OF THE ENDING ENDPOINT
        else:
            for n in range(0, steps):
                # REPEAT LOOP FROM AFTER STARTING ENDPOINT TO BEFORE ENDING ENDPOINT
                if (x + (delta_x / 2)) <= b:
                    x = a_new + (n * delta_x)  # UPDATE X BY ADDING N * DELTA_X
                    ordsum += f(x)  # ADD TO ORDINATE SUM

        return ordsum

    def integrate(self, start, end, steps):
        # CALCULATION OF delta_x
        delta_x = (end - start) * (steps ** (-1))

        # ARRAYS
        I = [[0]]
        ordsum = [0]

        # ROMBERG QUADRATURE METHOD WITH TRAPEZOIDAL SUMS
        ordsum.append(self.trapezoidal_ordsum(steps, start, end, start, end, delta_x, self.f))  # CALCULATE FIRST ORDINATE SUM
        I[0].extend([ordsum[-1] * delta_x])  # CALCULATE FIRST INTEGRAL

        DELTA_I = 10  # SET DIFFERENCE TO START LOOP
        N = 1
        while DELTA_I > 0.0001:
            STEPS_NEW = steps * (2 ** (N - 1))  # DOUBLE THE NUMBER OF STEPS
            DELTA_X_NEW = delta_x * (0.5 ** (N - 1))  # CALCULATE NEW DELTA-X
            a_new = start + (delta_x * (0.5 ** N))  # CALCULATE NEW STARTING POINT
            b_new = end - (delta_x * (0.5 ** N))  # CALCULATE NEW ENDING POINT
            ordsum.append(ordsum[-1] +
                          self.trapezoidal_ordsum(STEPS_NEW, start, end, a_new,
                                                 b_new, DELTA_X_NEW, self.f))  # UPDATE ORDINATE SUM
            I[0].extend([ordsum[-1] * (delta_x * (0.5 ** N))])  # UPDATE INTEGRAL ARRAY

            k = 1
            while (k - 1) < N:
                if k == N:
                    I.append([((4 ** k * I[k - 1][-1]) -
                               I[k - 1][-2]) / ((4 ** k) - 1)])
                    # APPLY ROMBERG QUADRATURE METHOD AND UPDATE THE TABLE
                else:
                    I[k].extend([((4 ** k * I[k - 1][-1]) -
                                  I[k - 1][-2]) / ((4 ** k) - 1)])
                    # APPLY ROMBERG QUADRATURE METHOD AND UPDATE THE TABLE
                k += 1  # MOVE TO NEXT ITERATION

            DELTA_I = abs(I[-1][-1] - I[-2][-1])  # CALCULATE NEW DIFFERENCE BETWEEN INTEGRALS
            N += 1  # MOVE FORWARDS TO NEXT ITERATION

        I[0].remove(0)
        self.romberg = tabulate(I, tablefmt='fancy_grid', numalign="right",
                       missingval="~", floatfmt=".3f")  # SAVE ROMBERG QUADRATURES
        return (I[-1][-1])  # PRINT FINAL RESULT

    def graph(self, start, end):
        t = np.linspace(start + start * (5 ** (-1)), end + end * (5 ** (-1)), int(round((end - start) * 100)))
        plt.plot(t, self.f(t), color="black")
        plt.show()

    def graphintegral(self, start, end):
        t = np.linspace(start + start * (5 ** (-1)), end + end * (5 ** (-1)), int(round((end - start) * 100)))
        plt.plot(t, self.f(t), color="black")
        plt.fill_between(np.linspace(start, end, int(round((end - start) * 100))),
                         self.f(np.linspace(start, end, int(round((end - start) * 100)))))
        plt.show()