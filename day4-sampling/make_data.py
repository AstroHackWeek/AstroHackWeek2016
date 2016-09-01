#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

import numpy as np
import matplotlib.pyplot as pl
np.random.seed(42)

true_params = [0.5, -0.1, -0.3]

x = np.sort(np.random.uniform(0, 10, 50))
y = true_params[0] * x + true_params[1]
yerr = np.random.uniform(0.05, 0.1, len(x))
y += np.sqrt(yerr**2 + np.exp(true_params[2])) * np.random.randn(len(y))

A = np.vander(x, 2)
ATA = np.dot(A.T, A / (yerr**2)[:, None])
w = np.linalg.solve(ATA, np.dot(A.T, y / yerr**2))

np.savetxt("data.txt", np.vstack((x, y, yerr)).T)

pl.errorbar(x, y, yerr=yerr, fmt=".k", capsize=0)
pl.plot(x, np.dot(A, w), "g")
pl.savefig("data.png")
