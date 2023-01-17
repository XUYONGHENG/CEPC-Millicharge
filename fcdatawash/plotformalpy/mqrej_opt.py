import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

mass = 10**np.linspace(0,2,21)
fig,ax = plt.subplots(figsize=(12,9))

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
print(datacx2)


dataaug = np.array([[0.0001,1e-6],[1,1e-3]])


ax.fill_between(datac[:,0],datac[:,1],y2=10,color='grey',alpha=0.3)
ax.fill_between(datacx2[:,0],datacx2[:,1],y2=10,color='orange',alpha=0.3)
ax.fill_between(dataaug[:,0],dataaug[:,1],y2=10,color='green',alpha=0.3)



a2 = np.load('../plotformalCSV/optimised/sbdostcepcz.npy')
b2 = np.load('../plotformalCSV/optimised/sbdostcepch.npy')
c2 = np.load('../plotformalCSV/optimised/sbdostcepcw.npy')
# print(a2.shape,b2.shape)

# print(d2)
zadd = np.array([[0.1,0.0037],[0.5,0.0045]])
hadd = np.array([[0.1,0.0187],[0.5,0.022]])
wadd = np.array([[0.1,0.0138],[0.5,0.0164]])

z,h,w = np.column_stack((mass[:16],a2[:-1])),np.column_stack((mass,b2)),np.column_stack((mass[:19],c2[:-1]))
# input('halt')
z,h,w = np.vstack((zadd,z)),np.vstack((hadd,h)),np.vstack((wadd,w))

zadd2 = np.array([45.6,100])
wadd2 = np.array([80,100])
z,w = np.vstack((z,zadd2)),np.vstack((w,wadd2))

d2 = np.zeros(shape=(23,))
for i in range(23):
    if i<= 17:
        d2[i] = z[i,1]
    else:
        d2[i] = h[i,1]
# print(np.array([0.1,0.5]).shape)
mass1 = np.concatenate((np.array([0.1,0.5]),mass))

l22, = ax.plot(z[:,0],z[:,1],linewidth=3,linestyle='solid',c='red')
l21, = ax.plot(h[:,0],h[:,1],linewidth=3,linestyle='solid',c='black')
l23, = ax.plot(w[:,0],w[:,1],linewidth=3,linestyle=':',c='blue')

l24, = ax.plot(mass1,d2,linewidth=5,linestyle='dashed',c='green',alpha=0.5)

#

ax.set_xscale('log')
ax.set_yscale('log')

ax.set_xlim((0.1,100))
ax.set_ylim((2e-3,1))

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

ax.text(2,0.3,'Colliders',fontsize=20, color='grey')
ax.text(0.12,0.5,'MiniBooNE',fontsize=20,color='orange')

ax.text(0.23,0.1,'BESIII',fontsize=20,color='Green')

ax.text(3,0.02,r'$WW$ mode',fontsize=20,color='blue',rotation=15)
ax.text(2,0.07,'Higgs Factory mode',fontsize=20,color='black',rotation=15)
ax.text(3,0.009,r'$Z$-pole mode',fontsize=20,color='red',rotation=25)
ax.text(36,0.1,r'Combined',fontsize=20,color='green',rotation=55)

datace613 = np.array(pd.read_csv('/home/xyh/Downloads/e613c.csv'))
ax.fill_between(datace613[:,0],datace613[:,1],y2=10,color='purple',alpha=0.3)
lc33, = ax.plot(datace613[:,0],datace613[:,1],linewidth=0,color='violet')
ax.text(1.2,0.007,r'E613',fontsize=20,color='violet')

ax.legend((l21,l22,l23,l24),
           ('Higgs Fatory','Z-pole','$WW$','Combined'),loc='lower right',fontsize=14,framealpha=0)

plt.savefig('../figformal/mqrej_optcombined.pdf',format='pdf')
plt.show()