import numpy as np
import MonteCarlo as mc
import time as time

a = np.zeros(shape=(10000000,4))
for i in range(a.shape[0]):
    a[i] = mc.phase_space_23_dot_gamma(240)
np.savetxt("/store/eexxa/ee19.csv",a,delimiter=', ')
