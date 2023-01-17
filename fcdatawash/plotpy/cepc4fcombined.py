import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

a = np.load('../plotCSV/sbdotscepc4fav.npy')
b = np.load('../plotCSV/sbdotscepc4fss.npy')
c = np.load('../plotCSV/sbdotscepc4fst.npy')
d = np.load('../plotCSV/sbdotscepc4fvv.npy')



az = np.load('../plotformalCSV/cepcz4f/sbdotscepcz4fav.npy')
bz = np.load('../plotformalCSV/cepcz4f/sbdotscepcz4fss.npy')
cz = np.load('../plotformalCSV/cepcz4f/sbdotscepcz4fst.npy')
dz = np.load('../plotformalCSV/cepcz4f/sbdotscepcz4fvv.npy')
# print(a.shape)
# print(b.shape)

aw = np.load('../plotformalCSV/cepcw4f/sbdotscepcw4fav.npy')[:-1]
# print(aw.shape)
bw = np.load('../plotformalCSV/cepcw4f/sbdotscepcw4fss.npy')[:-1]
# print(bw.shape)
cw = np.load('../plotformalCSV/cepcw4f/sbdotscepcw4fst.npy')[:-1]
dw = np.load('../plotformalCSV/cepcw4f/sbdotscepcw4fvv.npy')[:-1]
# a_mass = np.linspace(1,201,51)[:50]


# input('halt')
fig = plt.figure()
ax1,ax2,ax = plt.subplot(1,3,1),plt.subplot(1,3,2),plt.subplot(1,3,3)


l1, = ax1.plot(az[:,0],az[:,1],linewidth=5,linestyle='dashed',c='green')
l2, = ax1.plot(bz[:,0],bz[:,1],linewidth=5,linestyle='dashed',c='red')
l3, = ax1.plot(cz[:,0],cz[:,1],linewidth=5,linestyle='dashed',c='purple')
l4, = ax1.plot(dz[:,0],dz[:,1],linewidth=5,linestyle='dashed',c='blue')
ax1.set_xscale('log')
# ax.set_yscale('log')

ax1.set_xlabel(r'$m_\chi$ (GeV)',fontsize=25)
ax1.set_ylabel(r'$\Lambda (GeV)$',fontsize=25)

ax1.text(1,1800,r'CEPC Higgs Factory Model constraint on 4-fermion interactions',fontsize=30)
# datac = np.array(pd.read_csv('../plotCSV/constraint.csv'))
# datac[:,0] = 1e-9*datac[:,0]
#
# datac2 = np.column_stack((np.linspace(0,140,2),1/3*np.ones(shape=(2,))))
# for i in range(2,8):
#     datac[i,0] = 1
# for i in range(12,17):
#     datac[i,0] = 45
# datac[12,1] = 2.434105e-1
# datac[-2] = [100,0.70396]
# datac[-1,0] = 100

# l1c, = ax.plot(datac[:,0],datac[:,1],linewidth=0,linestyle='solid',color='gray')
# l1c2 = ax.plot(datac2[:,0],datac2[:,1],linewidth=0,color = 'red')

# ax.fill_between(datac[:,0],datac[:,1],y2=10,color='blue',alpha=0.3)
# ax.fill_between(datac2[:,0],datac2[:,1],y2=10,color='red',alpha=0.3)
# ax.legend((l1,l2),('FormCalc Monte Carlo','FeynCalc Analytic'),fontsize=24)

# ax.text(0.3,2,s='ILC constraint on millicharged model',fontsize=36)
# ax.text(0.3,1,s=r'$\sqrt{S}=500GeV,10^\circ<\theta_\gamma<170^\circ,p_T^\gamma>10 GeV$',fontsize=36)
#
ax1.set_ylim((500,1500))
ax1.tick_params(which = 'major', length=8,direction='in')
ax1.tick_params(which = 'minor', length=6,direction='in')

ax1.text(3,1200,'Z-pole',fontsize=19)

ax1.legend((l1,l2,l3,l4),('Chiral Vector','Scalar','Cross Scalar','Vector'),fontsize=17,loc='lower left')
for label in ax1.xaxis.get_minorticklabels():
    label.set_fontsize(24)
    label.set_fontname('verdana')
for label in ax1.xaxis.get_majorticklabels():
    label.set_fontsize(24)
    label.set_fontname('verdana')

for label in ax1.yaxis.get_minorticklabels():
    label.set_fontsize(24)
    label.set_fontname('verdana')
for label in ax1.yaxis.get_majorticklabels():
    label.set_fontsize(24)
    label.set_fontname('verdana')



l21, = ax2.plot(aw[:,0],aw[:,1],linewidth=5,linestyle='dashed',c='green')
l22, = ax2.plot(bw[:,0],bw[:,1],linewidth=5,linestyle='dashed',c='red')
l23, = ax2.plot(cw[:,0],cw[:,1],linewidth=5,linestyle='dashed',c='purple')
l24, = ax2.plot(dw[:,0],dw[:,1],linewidth=5,linestyle='dashed',c='blue')
ax2.set_xscale('log')
# ax.set_yscale('log')

ax2.set_xlabel(r'$m_\chi$ (GeV)',fontsize=25)
# ax2.set_ylabel(r'$\Lambda (GeV)$',fontsize=25)
ax2.text(3,1200,'W+W-',fontsize=19)
ax2.text(1,1800,r'CEPC Higgs Factory Model constraint on 4-fermion interactions',fontsize=30)
# datac = np.array(pd.read_csv('../plotCSV/constraint.csv'))
# datac[:,0] = 1e-9*datac[:,0]
#
# datac2 = np.column_stack((np.linspace(0,140,2),1/3*np.ones(shape=(2,))))
# for i in range(2,8):
#     datac[i,0] = 1
# for i in range(12,17):
#     datac[i,0] = 45
# datac[12,1] = 2.434105e-1
# datac[-2] = [100,0.70396]
# datac[-1,0] = 100

# l1c, = ax.plot(datac[:,0],datac[:,1],linewidth=0,linestyle='solid',color='gray')
# l1c2 = ax.plot(datac2[:,0],datac2[:,1],linewidth=0,color = 'red')

# ax.fill_between(datac[:,0],datac[:,1],y2=10,color='blue',alpha=0.3)
# ax.fill_between(datac2[:,0],datac2[:,1],y2=10,color='red',alpha=0.3)
# ax.legend((l1,l2),('FormCalc Monte Carlo','FeynCalc Analytic'),fontsize=24)

# ax.text(0.3,2,s='ILC constraint on millicharged model',fontsize=36)
# ax.text(0.3,1,s=r'$\sqrt{S}=500GeV,10^\circ<\theta_\gamma<170^\circ,p_T^\gamma>10 GeV$',fontsize=36)
#
ax2.set_ylim((300,1300))
ax2.tick_params(which = 'major', length=8,direction='in')
ax2.tick_params(which = 'minor', length=6,direction='in')


ax2.legend((l1,l2,l3,l4),('Chiral Vector','Scalar','Cross Scalar','Vector'),fontsize=17,loc='lower left')
for label in ax2.xaxis.get_minorticklabels():
    label.set_fontsize(24)
    label.set_fontname('verdana')
for label in ax2.xaxis.get_majorticklabels():
    label.set_fontsize(24)
    label.set_fontname('verdana')

for label in ax2.yaxis.get_minorticklabels():
    label.set_fontsize(24)
    label.set_fontname('verdana')
for label in ax2.yaxis.get_majorticklabels():
    label.set_fontsize(24)
    label.set_fontname('verdana')


l1, = ax.plot(a[:,0],a[:,1],linewidth=5,linestyle='dashed',c='green')
l2, = ax.plot(b[:,0],b[:,1],linewidth=5,linestyle='dashed',c='red')
l3, = ax.plot(c[:,0],c[:,1],linewidth=5,linestyle='dashed',c='purple')
l4, = ax.plot(d[:,0],d[:,1],linewidth=5,linestyle='dashed',c='blue')
ax.set_xscale('log')
# ax.set_yscale('log')
ax.text(3,1800,'Higgs Factory',fontsize=19)
ax.set_xlabel(r'$m_\chi$ (GeV)',fontsize=25)
# ax.set_ylabel(r'$\Lambda (GeV)$',fontsize=25)

# ax.text(1,1800,r'CEPC Higgs Factory Model constraint on 4-fermion interactions',fontsize=30)
# datac = np.array(pd.read_csv('../plotCSV/constraint.csv'))
# datac[:,0] = 1e-9*datac[:,0]
#
# datac2 = np.column_stack((np.linspace(0,140,2),1/3*np.ones(shape=(2,))))
# for i in range(2,8):
#     datac[i,0] = 1
# for i in range(12,17):
#     datac[i,0] = 45
# datac[12,1] = 2.434105e-1
# datac[-2] = [100,0.70396]
# datac[-1,0] = 100

# l1c, = ax.plot(datac[:,0],datac[:,1],linewidth=0,linestyle='solid',color='gray')
# l1c2 = ax.plot(datac2[:,0],datac2[:,1],linewidth=0,color = 'red')

# ax.fill_between(datac[:,0],datac[:,1],y2=10,color='blue',alpha=0.3)
# ax.fill_between(datac2[:,0],datac2[:,1],y2=10,color='red',alpha=0.3)
# ax.legend((l1,l2),('FormCalc Monte Carlo','FeynCalc Analytic'),fontsize=24)

# ax.text(0.3,2,s='ILC constraint on millicharged model',fontsize=36)
# ax.text(0.3,1,s=r'$\sqrt{S}=500GeV,10^\circ<\theta_\gamma<170^\circ,p_T^\gamma>10 GeV$',fontsize=36)
#
ax.set_ylim((1000,2500))
ax.tick_params(which = 'major', length=8,direction='in')
ax.tick_params(which = 'minor', length=6,direction='in')


ax.legend((l1,l2,l3,l4),('Chiral Vector','Scalar','Cross Scalar','Vector'),fontsize=17,loc='lower left')
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