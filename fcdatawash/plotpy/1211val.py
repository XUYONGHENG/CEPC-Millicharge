import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

a = np.load('../plotCSV/sbdotsilc1211.npy')
b = np.load('../plotCSV/sbdotsilc1211mg5.npy')
print(a.shape)
# print(b.shape)

# a_mass = np.linspace(1,201,51)[:50]

fig, ax = plt.subplots()


l1, = ax.plot(a[:,0],a[:,1],linewidth=5,linestyle='dashed',c='blue')
l2, = ax.plot(b[:,0],b[:,1],linewidth=5,linestyle='dashed',c='red')

# ax.set_xscale('log')
# ax.set_yscale('log')

ax.set_xlabel(r'$m_\chi$ (GeV)',fontsize=25)
ax.set_ylabel(r'$\sigma\ (pb)$',fontsize=25)



# l1c, = ax.plot(datac[:,0],datac[:,1],linewidth=0,linestyle='solid',color='gray')
# l1c2 = ax.plot(datac2[:,0],datac2[:,1],linewidth=0,color = 'red')

# ax.fill_between(datac[:,0],datac[:,1],y2=10,color='blue',alpha=0.3)
# ax.fill_between(datac2[:,0],datac2[:,1],y2=10,color='red',alpha=0.3)
# ax.legend((l1,l2),('FormCalc Monte Carlo','FeynCalc Analytic'),fontsize=24)

ax.text(1,800,s='ILC constraint on vector 4-fermion interaction model',fontsize=36)
ax.text(1,900,s=r'$\sqrt{S}=250GeV,|\cos\theta_\gamma|<0.995,E_\gamma>8 GeV$ with Z peak removed',fontsize=36)
ax.text(1,700,s=r'$\int Ldt=250fb^{-1}$',fontsize=36)



ax.set_ylim((500,1200))
ax.tick_params(which = 'major', length=8,direction='in')
ax.tick_params(which = 'minor', length=6,direction='in')


ax.legend((l2,l1),('MG5','Formcalc'),fontsize=40,loc='lower right')
for label in ax.xaxis.get_minorticklabels():
    label.set_fontsize(24)
    label.set_fontname('verdana')
for label in ax.xaxis.get_majorticklabels():
    label.set_fontsize(24)
    label.set_fontname('verdana')

for label in ax.yaxis.get_minorticklabels():
    label.set_fontsize(24)
    label.set_fontname('verdana')
for label in ax.yaxis.get_majorticklabels():
    label.set_fontsize(24)
    label.set_fontname('verdana')



plt.show()