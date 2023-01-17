import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

a = np.load('../plotCSV/sbdotscepcz.npy')
b = np.load('../plotCSV/sb2dots1.npy')
c = np.load('../plotCSV/sbdotscepcw.npy')

print(a.shape)
print(b.shape)
print(c.shape)

d = np.vstack((a,b[-5:]))
# print(d.shape)

mass = 10**np.linspace(0,2,21)

fig, ax = plt.subplots()

l2, = ax.plot(a[:,0],a[:,1],linewidth=3,linestyle='solid',c='red')
l1, = ax.plot(mass,b[:,1],linewidth=3,linestyle='solid',c='violet')
l3, = ax.plot(c[:,0],c[:,1],linewidth=3,linestyle='solid',c='blue')

l4, = ax.plot(d[:,0],d[:,1],linewidth=5,linestyle='dashed',c='black',alpha=0.5)

ax.set_xscale('log')
ax.set_yscale('log')

ax.set_xlabel(r'$m_\chi$ (GeV)',fontsize=25)
ax.set_ylabel(r'$\epsilon $',fontsize=25)


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

ax.text(1,0.6,s='CEPC constraints on milliQ',fontsize=36)
# ax.text(1,0.,s=r'$\sqrt{S}=91.2GeV$,CEPC detector cuts & Advanced cuts',fontsize=36)
ax.set_xlim((0.6,120))
ax.set_ylim((1e-2,1))
ax.tick_params(which = 'major', length=8,direction='in')
ax.tick_params(which = 'minor', length=6,direction='in')


ax.legend((l1,l2,l3,l4),(r'Higgs Factory',r'Z pole',r'W+W-',r'Combined best'),fontsize=20,loc='lower right')
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