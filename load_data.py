import pickle
import numpy as np
from class_reduced_measurement import ReducedMeasurement
import matplotlib.pyplot as plt
"""
Dataset of publication "Electrical impedance-based tissue classification for bladder tumor differentiation"

The impedance data is stored patient-wise in ReducedMeasurement objects which contain both frequency and impedance z.
"""


with open('dataset.pickle', 'rb') as h:
    data = pickle.load(h)

# Example: Plot healthy measurements of patient 1
p1_h = data['patient1']['healthy']
fig, ax = plt.subplots(2, 1, sharex=True)
ax[0].set_xscale('log')
ax[0].set_ylabel('$|Z|$')
ax[1].set_ylabel('$\\phi(Z)$')
for measurement in p1_h:
    ax[0].plot(measurement.frequency, np.abs(measurement.z))
    ax[1].plot(measurement.frequency, np.angle(measurement.z))
