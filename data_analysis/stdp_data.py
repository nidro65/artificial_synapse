import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from io import StringIO

plt.rcParams['text.usetex'] = True


csvTimeString = """.step x=-0.007
.step x=-0.0065
.step x=-0.006
.step x=-0.0055
.step x=-0.005
.step x=-0.0045
.step x=-0.004
.step x=-0.0035
.step x=-0.003
.step x=-0.0025
.step x=-0.002
.step x=-0.0015
.step x=-0.001
.step x=-0.00075
.step x=-0.0005
.step x=-0.00025
.step x=-1e-005
.step x=1e-005
.step x=0.00025
.step x=0.0005
.step x=0.00075
.step x=0.001
.step x=0.0015
.step x=0.002
.step x=0.00225
.step x=0.0025
.step x=0.00275
.step x=0.003
.step x=0.0035
.step x=0.004
.step x=0.0045
.step x=0.005
.step x=0.0055
.step x=0.006
.step x=0.0065
.step x=0.007
"""

csvTimeStringIO = StringIO(csvTimeString)
df_time = pd.read_csv(csvTimeStringIO, skipinitialspace=True, sep="\t", names=["time"])
df_time["time"] = df_time["time"].str.removeprefix(".step x=").astype(float)
df_time["time"] = df_time["time"]*10**3 # s to ms

print(df_time)

csvString = """  step	v(wdrift)	at
     1	0.474676	0.06
     2	0.47198	0.06
     3	0.468973	0.06
     4	0.465933	0.06
     5	0.462476	0.06
     6	0.459146	0.06
     7	0.455421	0.06
     8	0.451879	0.06
     9	0.448033	0.06
    10	0.444414	0.06
    11	0.440984	0.06
    12	0.437493	0.06
    13	0.434145	0.06
    14	0.432714	0.06
    15	0.431429	0.06
    16	0.429728	0.06
    17	0.428477	0.06
    18	0.558188	0.06
    19	0.556259	0.06
    20	0.554559	0.06
    21	0.552749	0.06
    22	0.550919	0.06
    23	0.547095	0.06
    24	0.543075	0.06
    25	0.541171	0.06
    26	0.538801	0.06
    27	0.536853	0.06
    28	0.534773	0.06
    29	0.53051	0.06
    30	0.526682	0.06
    31	0.522579	0.06
    32	0.518887	0.06
    33	0.515236	0.06
    34	0.511988	0.06
    35	0.508807	0.06
    36	0.505653	0.06
"""

csvStringIO = StringIO(csvString)

df = pd.read_csv(csvStringIO, skipinitialspace=True, sep="\t")

print(df)

x0_drift = 0.5 # mV
# delta_t = np.array([-12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, -0.01, 0, +0.01, 1, 2 , 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) # in ms
# # weight_drift_overlap = [] # in %
# weight_drift_seperate = np.array([477.02858, 474.04248, 470.504834, 466.38814, 461.53432, 455.94934, 449.65556, 442.624, 435.12201, 427.33446, 419.70128, 412.71642, 407.11918, 499.57117, 591.18307, 587.7037, 574.67371, 565.18269, 555.62311, 546.56392, 538.37818, 531.13079, 524.89769, 519.52827, 515.10584, 511.4643, 508.24237])

# Implementation 2
# delta_t = np.array([-6, -5, -4, -3, -2, -1, -0.01, 0, +0.01, 1, 2 , 3, 4, 5, 6]) # in ms
# weight_drift = np.array([0.5, 0.5, 0.5, 0.498046, 0.488016, 0.478451, 0.469902, 0.5, 0.523134, 0.512685, 0.50274, 0.5, 0.5, 0.5, 0.5])

delta_t = np.array([0, 0.00025, 0.0005, 0.00075, 0.001, 0.00125, 0.0015, 0.00175, 0.002, 0.00225, 0.0025, 0.00275, 0.003, 0.00325, 0.0035, 0.00375, 0.004]) # in s

# weight_drift = np.array([0.523302, 0.52082, 0.51811, 0.515031, 0.512685, 0.510197, 0.508005, 0.505302, 0.50274, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5])

weight_drift = np.array([0.940572, 0.938994, 0.93669, 0.934673, 0.932327, 0.930087, 0.927536, 0.925109, 0.922313, 0.919734, 0.917069, 0.914222, 0.911354, 0.908653, 0.905277, 0.902834, 0.9])


weight_drift_change = 100*(df["v(wdrift)"] - x0_drift)/x0_drift

# plt.figure
# plt.grid(True)
# plt.plot(delta_t, weight_drift_seperate)
# plt.xlabel("Delta T = ")



fig, ax = plt.subplots(figsize=(9, 6), tight_layout=True)
ax.plot(df_time["time"], weight_drift_change)
ax.scatter(df_time["time"], weight_drift_change, marker='o', edgecolors="#1f77b4", facecolor='none')
ax.grid(True)
ax.set_xlabel(r"$\Delta T\mathrm{~in~ms}$", fontsize=20)
ax.set_ylabel(r"$\Delta w \mathrm{~in~} \%$", fontsize=20)
# ax.set_title(r'\TeX\ is Number $\displaystyle\sum_{n=1}^\infty'
#              r'\frac{-e^{i\pi}}{2^n}$!', fontsize=16, color='r')


plt.show()