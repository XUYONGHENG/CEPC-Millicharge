import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

fig,ax = plt.subplots(figsize=(10,7.5))


datac = np.array(pd.read_csv('../plotCSV/constraint.csv'))
datacx = np.array(pd.read_csv('../plotCSV/constraint2.csv'))
datac[:,0] = 1e-9*datac[:,0]

# datac2 = np.column_stack((np.linspace(0,140,2),1/3*np.ones(shape=(2,))))
# datac3 = np.column_stack((np.linspace(0,1,2),1e-3*np.ones(shape=(2,))))

for i in range(2,8):
    datac[i,0] = 1
for i in range(12,17):
    datac[i,0] = 45
datac[12,1] = 2.434105e-1
datac[-2] = [100,0.70396]
datac[-1,0] = 100
# print(datac)
datac = np.vstack((datacx,datac[10:]))
print(datac)
mass = 10**np.linspace(0,2,21)

datacx2 = np.array(pd.read_csv('../plotCSV/cmini.csv'))



dataaug = np.array([[0.0001,1e-6],[1,1e-3]])


ax.fill_between(datac[:,0],datac[:,1],y2=10,color='grey',alpha=0.3)
ax.fill_between(datacx2[:,0],datacx2[:,1],y2=10,color='orange',alpha=0.3)
ax.fill_between(dataaug[:,0],dataaug[:,1],y2=10,color='green',alpha=0.3)


a = np.load('../plotCSV/sb3dots313.npy')
b = np.load('../plotCSV/sbdotsdel2.npy')
c = np.load('../plotCSV/sb3dots10degree.npy')

a2,c2 = np.load('../plotCSV/sbdotsdel2_eta313.npy'),np.load('../plotCSV/sbdotsdel2_eta244.npy')

a,c = np.vstack((a2,a)),np.vstack((c2,c))
# print(c.shape)

l1, = ax.plot(a[:,0],a[:,1],linewidth=2.4,linestyle='--',c='red')
l2, = ax.plot(b[:,0],b[:,1],linewidth=2.4,c='black')
l3, = ax.plot(c[:,0],c[:,1],linewidth=2.4,linestyle='-.',c='blue')
ax.set_xscale('log')
ax.set_yscale('log')
# ax1.text(1,0.3,s=r'The effect of $\theta$ coverage on the exclusion line',fontsize=19)
# ax1.text(2,0.15,s=r'$\sqrt{S}=240GeV, E_\gamma > 0.1 GeV$',fontsize=19)
# ax1.text(2,0.085,s=r'$\int L dt = 5 ab^{-1}$',fontsize=19)


lc2, = ax.plot(datac[:,0],datac[:,1],linewidth=0,linestyle='solid',color='gray')
# lc22 = ax1.plot(datac2[:,0],datac2[:,1],linewidth=0,color = 'red')

# ax1.fill_between(datac[:,0],datac[:,1],y2=10,color='blue',alpha=0.6)
# ax1.fill_between(datac2[:,0],datac2[:,1],y2=10,color='red',alpha=0.6)



# ax.text(2,0.6,'CMS e/3 Exclusion',fontsize=20)
ax.text(2,0.3,'Colliders',fontsize=24, color='grey')
ax.text(0.12,0.5,'MiniBooNE',fontsize=24,color='orange')
ax.text(0.23,0.1,'BESIII',fontsize=24,color='Green')

# ax.text(0.4,0.2,r'Expected sensitivity at each $\theta^{bound}$',fontsize=24)
# ax.text(1.3,0.12,'Millicharge',fontsize=24)

ax.set_xlim((0.1,100))
ax.set_ylim((1e-2,1))


ax.legend((l1,l2,l3),(r'$\theta=5\degree$',r'$\theta=8.5\degree$',r'$\theta=10\degree$'),fontsize=20,loc='lower right',framealpha=0)
ax.set_xlabel(r'$m_\chi$ (GeV)',fontsize=24)
ax.set_ylabel(r'$\epsilon$',fontsize=24)
for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(17)
for tick in ax.xaxis.get_minor_ticks():
    tick.label.set_fontsize(17)
for tick in ax.yaxis.get_major_ticks():
    tick.label.set_fontsize(17)
for tick in ax.yaxis.get_minor_ticks():
    tick.label.set_fontsize(17)

ax.tick_params(which = 'major', length=17,direction='in',top=True,right=True)
ax.tick_params(which = 'minor', length=9,direction='in',top=True,right=True)


ax.spines['top'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
ax.xaxis.set_tick_params(width=1.5, which='minor')
ax.xaxis.set_tick_params(width=1.5)
ax.yaxis.set_tick_params(width=1.5, which='minor')
ax.yaxis.set_tick_params(width=1.5)
ax.set_xticklabels([1,0.1,1,10,100], fontdict=None, minor=False)

datace613 = np.array(pd.read_csv('/home/xyh/Downloads/e613c.csv'))
ax.fill_between(datace613[:,0],datace613[:,1],y2=10,color='purple',alpha=0.3)
lc33, = ax.plot(datace613[:,0],datace613[:,1],linewidth=0,color='violet')
ax.text(1.7,0.015,r'E613',fontsize=20,color='violet')
plt.savefig('../figformal/mqrej_theta.pdf',format='pdf')
plt.show()