import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

a = np.load('/home/xyh/feynarts/workspace2/eeXXA-QED.fortran/result.npy')
b = np.load('../plotCSV/analyeexxa.npy')
print(a.shape)
print(b.shape)

a_mass = 10**np.linspace(0,2,21)

fig, ax = plt.subplots()

l2, = ax.plot(b[:,0],b[:,1],linewidth=2.5,linestyle='solid')
l1, = ax.plot(a_mass,a,linewidth=2.5,linestyle='--')

ax.set_xscale('log')
ax.set_yscale('log')

ax.set_xlabel(r'$m_\chi$ (GeV)',fontsize=25)
ax.set_ylabel(r'$\sigma\ (pb)$',fontsize=25)

ax.legend((l1,l2),('FormCalc Monte Carlo','FeynCalc Analytic'),fontsize=24)

ax.text(1,0.25,s='eexxA: Monte Carlo vs Analytic',fontsize=36)
ax.text(1,0.2,s=r'$\sqrt{S}=240GeV,|\eta_\gamma|<2.6,E_\gamma>0.1GeV$',fontsize=36)


ax.tick_params(which = 'major', length=8,direction='in')
ax.tick_params(which = 'minor', length=6,direction='in')

for label in ax.yaxis.get_minorticklabels():
    label.set_fontsize(24)
    label.set_fontname('verdana')
for label in ax.xaxis.get_majorticklabels():
    label.set_fontsize(24)
    label.set_fontname('verdana')

plt.show()