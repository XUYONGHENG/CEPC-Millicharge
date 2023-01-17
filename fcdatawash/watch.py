import numpy as np
import matplotlib.pyplot as plt

sb0 = np.load('plotCSV/sbdots2.npy')
sb1 = np.load('plotCSV/sbdots4.npy')

print(sb0[:,1],sb1[:,1])

for i in range(sb0.shape[0]):
    print(sb0[i,1]-sb1[i,1])
    print(sb0[i,0])

