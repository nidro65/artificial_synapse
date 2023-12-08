import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True


x0_drift = 500 # mV
delta_t = np.array([-12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, -0.01, 0, +0.01, 1, 2 , 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) # in ms
# weight_drift_overlap = [] # in %
weight_drift_seperate = np.array([477.02858, 474.04248, 470.504834, 466.38814, 461.53432, 455.94934, 449.65556, 442.624, 435.12201, 427.33446, 419.70128, 412.71642, 407.11918, 499.57117, 591.18307, 587.7037, 574.67371, 565.18269, 555.62311, 546.56392, 538.37818, 531.13079, 524.89769, 519.52827, 515.10584, 511.4643, 508.24237])

weight_drift_change = (weight_drift_seperate - x0_drift) / x0_drift

# plt.figure
# plt.grid(True)
# plt.plot(delta_t, weight_drift_seperate)
# plt.xlabel("Delta T = ")



fig, ax = plt.subplots(figsize=(9, 6), tight_layout=True)
ax.plot(delta_t, weight_drift_change)
ax.scatter(delta_t, weight_drift_change, marker='o', edgecolors="#1f77b4", facecolor='none')
ax.grid(True)
ax.set_xlabel(r"$\Delta T$ in $\mathrm{ms}$", fontsize=16)
ax.set_ylabel(r"$\Delta w$ in $\%$", fontsize=16)
# ax.set_title(r'\TeX\ is Number $\displaystyle\sum_{n=1}^\infty'
#              r'\frac{-e^{i\pi}}{2^n}$!', fontsize=16, color='r')


plt.show()