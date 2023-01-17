import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

a = np.load('../plotCSV/sbdotsilc.npy')[:,1]
b = np.load('../plotCSV/sb2dots1.npy')
print(a.shape)
# print(b.shape)

a_mass = np.linspace(1,201,51)[:50]

fig, ax = plt.subplots()

l2, = ax.plot(b[:,0],b[:,1],linewidth=5,linestyle='dashed',c='red')
l1, = ax.plot(a_mass,a,linewidth=5,linestyle='dashed',c='black')

ax.set_xscale('log')
ax.set_yscale('log')

ax.set_xlabel(r'$m_\chi$ (GeV)',fontsize=25)
ax.set_ylabel(r'$\sigma\ (pb)$',fontsize=25)


datac = np.array(pd.read_csv('../plotCSV/constraint.csv'))
datac[:,0] = 1e-9*datac[:,0]

datac2 = np.column_stack((np.linspace(0,140,2),1/3*np.ones(shape=(2,))))
for i in range(2,8):
    datac[i,0] = 1
for i in range(12,17):
    datac[i,0] = 45
datac[12,1] = 2.434105e-1
datac[-2] = [100,0.70396]
datac[-1,0] = 100

l1c, = ax.plot(datac[:,0],datac[:,1],linewidth=0,linestyle='solid',color='gray')
l1c2 = ax.plot(datac2[:,0],datac2[:,1],linewidth=0,color = 'red')

ax.fill_between(datac[:,0],datac[:,1],y2=10,color='blue',alpha=0.3)
ax.fill_between(datac2[:,0],datac2[:,1],y2=10,color='red',alpha=0.3)
# ax.legend((l1,l2),('FormCalc Monte Carlo','FeynCalc Analytic'),fontsize=24)

ax.text(0.3,2,s='ILC constraint on millicharged model',fontsize=21)
ax.text(0.3,1,s=r'$\sqrt{S}=500GeV,10^\circ<\theta_\gamma<170^\circ,p_T^\gamma>10 GeV$',fontsize=21)

ax.set_ylim((0.01,10))
ax.tick_params(which = 'major', length=8,direction='in')
ax.tick_params(which = 'minor', length=6,direction='in')


ax.legend((l2,l1),('CEPC','ILC'),fontsize=18,loc='lower right')
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