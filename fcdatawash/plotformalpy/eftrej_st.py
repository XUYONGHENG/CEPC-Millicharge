import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

mass = 10**np.linspace(0,2,21)

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

############################################################################################
aw = np.load('../plotformalCSV/cepcw4f/sbdotscepcw4fav.npy')[:-1]
# print(aw.shape)
bw = np.load('../plotformalCSV/cepcw4f/sbdotscepcw4fss.npy')[:-1]
# print(bw.shape)
cw = np.load('../plotformalCSV/cepcw4f/sbdotscepcw4fst.npy')[:-1]
dw = np.load('../plotformalCSV/cepcw4f/sbdotscepcw4fvv.npy')[:-1]
# a_mass = np.linspace(1,201,51)[:50]

######
wadd = np.array([80,1])
zadd = np.array([45.6,1])

aw,bw,cw,dw = np.vstack((aw,wadd)),np.vstack((bw,wadd)),np.vstack((cw,wadd)),np.vstack((dw,wadd))
az,bz,cz,dz = np.vstack((az[:-1],zadd)),np.vstack((bz[:-1],zadd)),np.vstack((cz[:-1],zadd)),np.vstack((dz,zadd))

############

# input('halt')
fig,ax = plt.subplots(figsize=(9,6.75))

l1a, = ax.plot(c[:,0],c[:,1],linewidth=3,linestyle='solid',color='black')
l1b, = ax.plot(cw[:,0],cw[:,1],linewidth=3,linestyle='dashed',color='red')
l1d, = ax.plot(cz[:,0],cz[:,1],linewidth=3,linestyle=':',color='blue')


ax.set_xscale('log')
# ax.set_yscale('log')


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
ax.set_ylabel(r'$\Lambda$ (GeV)',fontsize=24)

ax.text(2,1000,r'Higgs Factory $\sqrt{s}$=240 GeV',fontsize=20,color='black')
ax.text(2,620,r'$W^+W^-$ $\sqrt{s}$=160 GeV',fontsize=20,color='red')
ax.text(1.5,770,r'$Z$-pole $\sqrt{s}$=91.2 GeV',fontsize=20,color='blue')
ax.text(3,400,'Scalar(t)',fontsize=24)

ax.set_xlim(1,100)
ax.set_ylim(200,1200)

ax.spines['top'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
ax.xaxis.set_tick_params(width=1.5, which='minor')
ax.xaxis.set_tick_params(width=1.5)
ax.yaxis.set_tick_params(width=1.5, which='minor')
ax.yaxis.set_tick_params(width=1.5)

ax.set_xticklabels([1,1,10,100], fontdict=None, minor=False)

plt.savefig('../figformal/eftrej_st_2.pdf',format='pdf')

plt.show()