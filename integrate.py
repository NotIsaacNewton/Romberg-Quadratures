#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 14:21:25 2021

@author: ariandovald
"""

import numpy as np
import methods as met


# USER-DEFINED CONSTANTS AND VARIABLES
START = 0
END = 2
STEPS = 1


# DEFINE EQUATION
def equation(x):
    y = np.sin(x*np.pi/2) * ((np.pi)**x)
    return y


eq = met.math(equation)
eq.graphintegral(START, END)
print(eq.integrate(START, END, STEPS))
