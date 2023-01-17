import numpy as np
import matplotlib.pyplot as plt

o = np.load('../plotCSV/sbdotsdel.npy')[:,-1]
t = np.load('../plotCSV/sb2dots1.npy')[:,-1]

o,t = t,o

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

ax.text(1,0.22,r'Impact of Delphes detector simulation',fontsize=25)
ax.text(1,0.1,s=r'$\sqrt{S}=240GeV, |\eta|<2.6, S/\sqrt{B}$ = 2',fontsize=25)
ax.legend((ol,tl),(r'FormCalc + our smearing code',r'MG5 + Pythia8 + Delphes'),loc='upper left',fontsize = 25)

ax.set_xlabel(r'$m_\chi$ (GeV)',fontsize=24)
ax.set_ylabel(r'$\epsilon$',fontsize=24)

plt.show()

