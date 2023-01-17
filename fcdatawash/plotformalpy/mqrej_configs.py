import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

fig,ax = plt.subplots(figsize=(12,9))


datac = np.array(pd.read_csv('../plotCSV/constraint.csv'))
datacx = np.array(pd.read_csv('../plotCSV/constraint2.csv'))
datac[:,0] = 1e-9*datac[:,0]
# input('halt')

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



a2 = np.load('../plotCSV/sbdotscepcz2.npy')
# b2 = np.load('../plotCSV/sb2dots1.npy')
# b2 = np.load('../plotCSV/sbdotsdel2.npy')
b2 = np.load('../plotCSV/sbdots_newcut.npy')

c2 = np.load('../plotCSV/sbdotscepcw2.npy')
d2 = np.vstack((a2,b2[-5:]))


for i in range(b2.shape[0]):
    print(i,b2[i])
# input('halt')
# print(a2.shape)
# print(b2.shape)
print(a2)
print(b2)

a_add = np.array([45.6,100])
c_add = np.array([80,100])
# ax1.fill_between(datac3[:,0],datac3[:,1],y2=10,color='black',alpha=0.6)

a2,c2 = np.vstack((a2,a_add)),np.vstack((c2,c_add))
print(b2[12])
l22, = ax.plot(a2[:,0],a2[:,1],linewidth=3,linestyle='solid',c='red')
l21, = ax.plot(b2[:,0],b2[:,1],linewidth=3,linestyle='solid',c='black')
l23, = ax.plot(c2[:,0],c2[:,1],linewidth=3,linestyle=':',c='blue')

l24, = ax.plot(d2[:,0],d2[:,1],linewidth=5,linestyle='dashed',c='green',alpha=0.5)


lc2, = ax.plot(datac[:,0],datac[:,1],linewidth=0,linestyle='solid',color='gray')
# lc22 = ax.plot(datac2[:,0],datac2[:,1],linewidth=0,color = 'red')
lc22, = ax.plot(datacx2[:,0],datacx2[:,1],linewidth=0,color = 'orange')


datace613 = np.array(pd.read_csv('/home/xyh/Downloads/e613c.csv'))
ax.fill_between(datace613[:,0],datace613[:,1],y2=10,color='purple',alpha=0.3)
lc33, = ax.plot(datace613[:,0],datace613[:,1],linewidth=0,color='violet')
ax.text(1.7,0.007,r'E613',fontsize=20,color='violet')


ax.set_xscale('log')
ax.set_yscale('log')

ax.set_xlim((0.1,100))
ax.set_ylim((5e-3,1))

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
ax.text(2,0.3,'Colliders',fontsize=20, color='grey')
ax.text(0.12,0.5,'MiniBooNE',fontsize=20,color='orange')

ax.text(0.23,0.1,'BESIII',fontsize=20,color='Green')

ax.text(3,0.06,r'$WW$ mode',fontsize=20,color='blue',rotation=15)
ax.text(2,0.04,'Higgs Factory mode',fontsize=20,color='black',rotation=15)
ax.text(3,0.018,r'$Z$-pole mode',fontsize=20,color='red',rotation=12.5)
ax.text(36,0.1,r'Combined',fontsize=20,color='green',rotation=55)

ax.spines['top'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
ax.xaxis.set_tick_params(width=1.5, which='minor')
ax.xaxis.set_tick_params(width=1.5)
ax.yaxis.set_tick_params(width=1.5, which='minor')
ax.yaxis.set_tick_params(width=1.5)
ax.set_xticklabels([1,0.1,1,10,100], fontdict=None, minor=False)

# ax.legend((l21,l22,l23,l24),
#            ('Higgs Fatory','Z-pole','W+W-','Combined Best'),loc='lower right',fontsize=14,framealpha=0)

plt.savefig('../figformal/mqrej_configs_2.pdf',format='pdf')
plt.show()