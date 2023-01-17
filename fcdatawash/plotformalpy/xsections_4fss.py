import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# zvvx = np.array(
#     [7.212, 7.23, 7.253, 7.278, 7.261, 7.29, 7.309, 7.311, 7.355, 7.35, 7.375, 7.372, 7.353, 7.254, 7.03, 6.339, 4.194, 0.05])
# wvvx = np.array(
#     [24.33,24.54,24.42,24.48,24.60,24.57,24.62,24.63,24.49,
#      24.48,24.35,24.04,23.52,22.61,21.25,19.09,15.81,11.09,4.97,0.01])
# vvsection = np.array([58.12,58.37,58.55,58.57,58.64,58.83,59.21,59.39,59.4,59.88,59.62,59.88,60.18,60.2,60.54,60.41,60.52,60.24,58.88,54.67,41.44])
hvvx = np.array(pd.read_table('../plotCSV/4fssxsectiondotsh.csv',header=None))
zvvx = np.array(pd.read_table('../plotCSV/4fssxsectiondotsz.csv',header=None))
wvvx = np.array(pd.read_table('../plotCSV/4fssxsectiondotsw.csv',header=None))
print(wvvx[:,0])
hmasses = np.linspace(1,100,100,endpoint=True)
zmasses = np.linspace(1,45,45,endpoint=True)
wmasses = np.linspace(1,79,79,endpoint=True)
print(wmasses)
print(hvvx.shape)
print(hmasses.shape)
# input('halt')
# zxsection = np.load('/store/disposed/milliq/cepcz/zxsection.npy')
# wxsection = np.load('/store/disposed/milliq/cepcw/wxsection.npy')

mass = 10**np.linspace(0,2,21)

# a = np.zeros(shape=(18,))
# a[:17] = mass[:17]
# a[17] = 45.5
# print(a.shape)

fig,ax = plt.subplots(figsize=(9,6.75))

lnh, = ax.plot(hmasses,hvvx[:,0],linewidth=3, linestyle = 'solid',color='black')
lnw, = ax.plot(wmasses,wvvx[:,0],linewidth=3, linestyle = '-.',color='red')
lnz, = ax.plot(zmasses,zvvx[:,0],linewidth=3, linestyle = ':',color='blue')

ax.set_xscale('log')
ax.set_yscale('log')
# ax.set_ylim()

for label in ax.xaxis.get_majorticklabels():
    label.set_fontsize(20)
    label.set_fontname('verdana')
for label in ax.xaxis.get_minorticklabels():
    label.set_fontsize(20)
    label.set_fontname('verdana')
for label in ax.yaxis.get_majorticklabels():
    label.set_fontsize(20)
    label.set_fontname('verdana')
for label in ax.yaxis.get_minorticklabels():
    label.set_fontsize(20)
    label.set_fontname('verdana')

ax.tick_params(which = 'major', length=17,direction='in',top=True,right=True)
ax.tick_params(which = 'minor', length=9,direction='in',top=True,right=True)


# ax.legend((lnh,lnw,lnz,),('Higgs Factory','W+W-','Z-pole'),loc='lower left',fontsize=24,framealpha=0)

ax.text(3,5,r'Z-pole,$\sqrt{s}$=91.2 GeV',fontsize=20,color='blue')
ax.text(3,17,r'$W^+W^-$,$\sqrt{s}$=160 GeV',fontsize=20,color='red')
ax.text(3,45,r'Higgs Factory,$\sqrt{s}$=240 GeV',fontsize=20,color='black')
# ax.text(2,12,r'Vector 4-fermion interaction',fontsize=20)
ax.text(2.3,2.5,r'$L$=$\frac{1}{\Lambda^2}$$\bar{\chi}\chi\bar{e}e$',fontsize=20)
ax.text(2.3,1.7,r'$\Lambda = 200$GeV',fontsize=20)


ax.spines['top'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
ax.xaxis.set_tick_params(width=1.5, which='minor')
ax.xaxis.set_tick_params(width=1.5)
ax.yaxis.set_tick_params(width=1.5, which='minor')
ax.yaxis.set_tick_params(width=1.5)
ax.set_xticklabels([1,1,10,100], fontdict=None, minor=False)


ax.set_ylim(1, 100)
ax.set_xlim(1,100)
ax.set_xlabel(r'$m_\chi$ (GeV)',fontsize=24)
ax.set_ylabel(r'$\sigma$ (pb)',fontsize=24)

plt.savefig('/home/xyh/texworkbench/cepc/paperdraft/figs/xsection_4fss_1.pdf',format='pdf')

plt.show()