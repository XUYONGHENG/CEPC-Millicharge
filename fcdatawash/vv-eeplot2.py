import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


a = np.load('/home/xyh/feynarts/workspace2/eevvA-SM2.fortran/sigma.npy')
b = np.load('/home/xyh/feynarts/workspace2/eeeeA-SM3.fortran/sigma.npy')
# print(a,b)

c = np.load('/home/xyh/feynarts/workspace2/eevvA-SM2.fortran/sigma2.npy')
d = np.load('/home/xyh/feynarts/workspace2/eeeeA-SM3.fortran/sigma2.npy')

e = np.array(pd.read_csv('datasnapped.csv'))

f = np.load('/home/xyh/feynarts/workspace2/eevvA-SM2.fortran/sigma3.npy')
g = np.load('/home/xyh/feynarts/workspace2/eeeeA-SM3.fortran/sigma3.npy')
h = np.load('/home/xyh/feynarts/workspace2/eevmvmA-SM3.fortran/sigma3.npy')
# print(h[:50,1])
# print(f[0][1])

f[0,1] = f[0,1]/100
for i in range(1,38):
    f[i,1] = f[i,1]/10
# print(c[9])
# print(c[47])
# for i in range(/h.shape[0]):
#     if h[i][1]>0.9 and h[i+1][1]<0.2:
#         print(i)

for i in range(13):
    h[i,1] = h[i,1]/100

for i in range(13,41):
    h[i,1] = h[i,1]/10

# print(h[:50,1])
#
# input("x")

# for i in range(10):
#     c[i,1] = c[i,1]/100
# for i in range(10,47):
#     c[i,1] = c[i,1]/10
a = f[:]
b = g[:]
for i in range(a.shape[0]):
    a[i,1] = a[i,1]+2*h[i,1]
# print(b.shape[0])

fig, ax = plt.subplots()
# ax.scatter(a[:,0],np.log10(a[:,1]),s=7,c='red')
ax.plot(a[:-2,0],np.log10(a[:-2,1]),color = 'red',linestyle = '-')
# ax.scatter(b[:,0],np.log10(b[:,1]),s=7,c='blue')
ax.plot(b[:,0],np.log10(b[:,1]),color = 'blue',linestyle = '-')
# ax.scatter(e[:,0],np.log10(e[:,1]),s=7,c='black')
ax.plot(e[:,0],np.log10(e[:,1]),c='black',linestyle = '--',label = 'Mann et al. 1987')
ax.set_xlabel(r'$\sqrt{S}$ (GeV)',fontdict={'fontsize':24})
ax.set_ylabel(r'$\sigma$ (pb)',fontdict={'fontsize':24})
ax.set_yticklabels([str(0.001),str(0.01),str(0.1),str(1),str(10),str(100),str(1000),str(100)],fontdict={'fontsize':16})
ax.set_xticklabels(labels = [str(0),str(20),str(40),str(60),str(80),str(100),str(120),str(140)],fontdict={'fontsize':16})
plt.text(90,1,r'Mana et al, 1987', fontsize=24)
plt.text(40,0,r'$ee\rightarrow\nu\bar{\nu}\gamma$',color='red', fontsize=24)
plt.text(20,2.5,r'$ee\rightarrow ee\gamma$',color='blue',rotation=0, fontsize=24)
plt.title(r"$e^+e^-$ final states vs $\bar{\nu}\nu$ final states",fontdict={'fontsize':24})
plt.show()