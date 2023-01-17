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

data1 = np.load('../plotCSV/sbdotsdel2.npy')
data1a = np.load('../plotCSV/sbdotsdel2_2.5.npy')
data1b = np.load('../plotCSV/sbdotsdel2_10.npy')
data1c = np.load('../plotCSV/sbdotsdel2_20.npy')

# l1, = ax.plot(data[:,0],data[:,1],linewidth=2.25,linestyle='dashed',color='r')
l1, = ax.plot(data1[:,0],data1[:,1],linewidth=3,linestyle='solid',color='black')
l1c, = ax.plot(datac[:,0],datac[:,1],linewidth=0,linestyle='solid',color='gray')
# l1c2 = ax.plot(datac2[:,0],datac2[:,1],linewidth=0,color = 'red')
l1a, = ax.plot(data1a[:,0],data1a[:,1],linewidth=3,linestyle='dashed',color='blue')
l1b, = ax.plot(data1b[:,0],data1b[:,1],linewidth=3,linestyle='dashed',color='red')
l1d, = ax.plot(data1c[:,0],data1c[:,1],linewidth=3,linestyle='dashed',color='grey')


ax.set_xscale('log')
ax.set_yscale('log')

ax.set_xlim((0.1,100))
ax.set_ylim((1e-2,1))

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

ax.tick_params(which = 'major', length=17,direction='in',top=True,right=True)
ax.tick_params(which = 'minor', length=9,direction='in',top=True,right=True)

ax.set_xlabel(r'$m_\chi$ (GeV)',fontsize=24)
ax.set_ylabel(r'$\epsilon$',fontsize=24)

# ax.text(2,0.6,'CMS e/3 Exclusion',fontsize=20)
ax.text(2,0.3,'Colliders',fontsize=24, color='grey')
ax.text(0.12,0.5,'MiniBooNE',fontsize=24,color='orange')
ax.text(0.23,0.1,'BESIII',fontsize=24,color='Green')

ax.spines['top'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
ax.xaxis.set_tick_params(width=1.5, which='minor')
ax.xaxis.set_tick_params(width=1.5)
ax.yaxis.set_tick_params(width=1.5, which='minor')
ax.yaxis.set_tick_params(width=1.5)
ax.set_xticklabels([1,0.1,1,10,100], fontdict=None, minor=False)

ax.legend((l1d,l1,l1a,l1b,),(r'2.5 ab$^{-1}$',r'5.6 ab$^{-1}$',
                              r'10 ab$^{-1}$',r'20 ab$^{-1}$',),loc='lower right',fontsize=18,framealpha=0)

datace613 = np.array(pd.read_csv('/home/xyh/Downloads/e613c.csv'))
ax.fill_between(datace613[:,0],datace613[:,1],y2=10,color='purple',alpha=0.3)
lc33, = ax.plot(datace613[:,0],datace613[:,1],linewidth=0,color='violet')
ax.text(1.7,0.015,r'E613',fontsize=20,color='violet')
# ax.text(0.3,0.2,r'Expected sensitivity at each $\int\cal{L}dt$',fontsize=24)
# ax.text(1.2,0.12,'Millicharge',fontsize=24)

plt.savefig('../figformal/mqrej_lumis.pdf',format='pdf')
plt.show()