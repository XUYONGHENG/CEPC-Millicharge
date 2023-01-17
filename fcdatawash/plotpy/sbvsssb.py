import numpy as np
import matplotlib.pyplot as plt

o = np.load('../plotCSV/ssbdots1.npy')[:,-1]
t = np.load('../plotCSV/sb2dots1.npy')[:,-1]

mass = 10**np.linspace(0,2,21)

fig, ax = plt.subplots()

tl, = ax.plot(mass,t,linewidth=3,linestyle='solid',color='black')
ol, = ax.plot(mass,o,linewidth=3,linestyle='dashed',color='red')

ax.set_xscale('log')
ax.set_yscale('log')

for label in ax.xaxis.get_majorticklabels():
    label.set_fontsize(16)
    label.set_fontname('verdana')
for label in ax.xaxis.get_minorticklabels():
    label.set_fontsize(16)
    label.set_fontname('verdana')
for label in ax.yaxis.get_majorticklabels():
    label.set_fontsize(16)
    label.set_fontname('verdana')
for label in ax.yaxis.get_minorticklabels():
    label.set_fontsize(16)
    label.set_fontname('verdana')

ax.text(1,0.1,r'Two different definitions of signal significance',fontsize=25)
ax.legend((tl,ol),(r'S/$\sqrt{B}$',r'S/$\sqrt{S+B}$'),loc='upper left',fontsize = 25)

ax.set_xlabel(r'$m_\chi$ (GeV)',fontsize=24)
ax.set_ylabel(r'$\epsilon$',fontsize=24)

plt.show()

