import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

eedata = np.array(pd.read_csv("plotCSV/eecepc1.csv"))
vvdata = np.array(pd.read_csv("plotCSV/cepcvvbg.csv"))

print(eedata.shape)

eew = np.array(pd.read_csv("plotCSV/eececp1w.csv"))
vvw = np.array(pd.read_csv("plotCSV/cepcvvbgw.csv"))
eew.flatten()
print(eew.shape)

# eehist, xedges, yedges= np.histogram2d(eedata[:,0],eedata[:,1],weights=eew[:,0],bins=(30,30))
# print(eehist)
plt.hist2d(eedata[:,0],eedata[:,1],weights=eew[:,0],bins=(30,30))
plt.show()