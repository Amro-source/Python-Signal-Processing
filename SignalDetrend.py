# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 21:12:53 2021

@author: Zikantika
"""

from scipy import signal
from numpy.random import default_rng
import numpy as np


rng = default_rng()
npoints = 1000
noise = rng.standard_normal(npoints)
x = 3 + 2*np.linspace(0, 1, npoints) + noise
(signal.detrend(x) - noise).max()

