import numpy as np
import pandas as pd
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
# import scipy as s

a = np.linspace(-1,1,31)
b = np.zeros(shape=(30,2))



data = np.array(pd.read_csv("plotCSV/peek.csv"))
for i in range(data.shape[0]):
    for j in range(30):
        if data[i][1] >= a[j] and data[i][1] < a[j+1]:
            b[j][0] += 1
            if data[i][0] >= b[j][1]:
                b[j][1] = data[i][0]

np.save("plotCSV/MCresult",b)
# def f(x):
#     return np.cos(np.arcsin(((4-x)/x)*0.31225))-angle
a,b =np.load("plotCSV/MCresult.npy")[:,1], np.array(pd.read_csv("plotCSV/theoretical.csv"))
print(a.shape,b.shape)
c = np.linspace(-1,1,31)[1:]
d = np.zeros(shape=(30,))
d[0] = 4
for i in range(1,30):
    if b[i-1 ]<= b[i]:
        d[i] = b[i]
    else:
        d[i] = b[i-1]


a1,b1 = np.column_stack((c,a)),np.column_stack((c,b))
fig, ax1 = plt.subplots()
ax1.scatter(c[1:-1],a[1:-1],s=7,c='red')
ax1.scatter(c[1:-1],d[1:-1],s=7,c='blue')
ax1.set_ylabel(r'$E_\gamma$ (GeV)')
ax1.set_xlabel(r'$\cos_\gamma$')

ax2 = ax1.twinx()
ax2.bar(c[1:-1],height=(d[1:-1]-a[1:-1]),color='orange',width=0.05,alpha=0.3)
ax2.set_ylabel(r'Difference (GeV)')
# p3 = plt.bar(c[1:-1],height=(d[1:-1]-a[1:-1])*4,ecolor='b',width=0.05)
plt.title(r"Monte Carlo result vs analytical limit")
plt.show()