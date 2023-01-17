import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


hvvx = np.array(pd.read_table('../../plotCSV/xsectionplot/4fvvxsectiondots.csv',header=None))
zvvx = np.array(pd.read_table('../../plotCSV/xsectionplot/4fvvxsectiondotsz.csv',header=None))
wvvx = np.array(pd.read_table('../../plotCSV/xsectionplot/4fvvxsectiondotsw.csv',header=None))

hvvx = np.concatenate((hvvx,np.array([[0]])))
zvvx = np.concatenate((zvvx,np.array([[0]])))
wvvx = np.concatenate((wvvx,np.array([[0]])))


hmasses = np.linspace(1,120,120,endpoint=True)
zmasses = np.linspace(1,46,46,endpoint=True)
wmasses = np.linspace(1,80,80,endpoint=True)

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
    label.set_fontname('serif')
for label in ax.xaxis.get_minorticklabels():
    label.set_fontsize(20)
    label.set_fontname('serif')
for label in ax.yaxis.get_majorticklabels():
    label.set_fontsize(20)
    label.set_fontname('serif')
for label in ax.yaxis.get_minorticklabels():
    label.set_fontsize(20)
    label.set_fontname('serif')

ax.tick_params(which = 'major', length=17,direction='in',top=True,right=True)
ax.tick_params(which = 'minor', length=9,direction='in',top=True,right=True)


# ax.legend((lnh,lnw,lnz,),('Higgs Factory','W+W-','Z-pole'),loc='lower left',fontsize=24,framealpha=0)

ax.text(3,4,r'Z-mode $\sqrt{s}$=91.2 GeV',fontsize=20,
        color='blue',fontfamily='serif')
ax.text(3,17,r'WW-mode $\sqrt{s}$=160 GeV',fontsize=20,
        color='red',fontfamily='serif')
ax.text(3,42,r'H-mode $\sqrt{s}$=240 GeV',fontsize=20,
        color='black',fontfamily='serif')
# ax.text(2,12,r'Vector 4-fermion interaction',fontsize=20)
ax.text(2.2,80,r'$\Lambda_V = 200$GeV $L$=$\frac{1}{\Lambda^2_V}$$\bar{\chi}\gamma_\mu\chi\bar{e}\gamma^\mu e$',
        fontsize=26,fontfamily='serif')
# ax.text(2.3,3.5,r'$\Lambda = 200$GeV',fontsize=20)


ax.spines['top'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
ax.xaxis.set_tick_params(width=1.5, which='minor')
ax.xaxis.set_tick_params(width=1.5)
ax.yaxis.set_tick_params(width=1.5, which='minor')
ax.yaxis.set_tick_params(width=1.5)


ax.set_xticklabels([1,1,10,100], fontdict=None, minor=False)
ax.set_yticklabels([1,1,10,100], fontdict=None, minor=False)


ax.set_ylim(2, 200)
ax.set_xlim(1,200)
ax.set_xlabel(r'$m_\chi$ (GeV)',fontsize=24,fontfamily='serif')
ax.set_ylabel(r'$\sigma$ (pb)',fontsize=24,fontfamily='serif')

# plt.savefig('/Users/yohengxu/Desktop/newfig/xsection_4fvv_4.pdf',format='pdf')
plt.savefig('/home/xyh/texworkbench/cepc/paperdraft/figs/xsection_4fvv_4.pdf',format='pdf')

plt.show()