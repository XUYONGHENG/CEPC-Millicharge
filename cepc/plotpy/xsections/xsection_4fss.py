import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

hvvx = np.array(pd.read_table('../../plotCSV/xsectionplot/4fssxsectiondotsh2.csv',header=None))
zvvx = np.array(pd.read_table('../../plotCSV/xsectionplot/4fssxsectiondotsz.csv',header=None))
wvvx = np.array(pd.read_table('../../plotCSV/xsectionplot/4fssxsectiondotsw.csv',header=None))

hvvx = np.concatenate((hvvx,np.array([[0]])))
zvvx = np.concatenate((zvvx,np.array([[0]])))
wvvx = np.concatenate((wvvx,np.array([[0]])))

hmasses = np.linspace(1,120,120,endpoint=True)
zmasses = np.linspace(1,46,46,endpoint=True)
wmasses = np.linspace(1,80,80,endpoint=True)

print(wmasses)
print(hvvx.shape)
print(hmasses.shape)

mass = 10**np.linspace(0,2,21)

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


ax.text(1.5,2.5,r'Z-mode $\sqrt{s}$=91.2 GeV',fontsize=20,color='blue',fontfamily='serif')
ax.text(1.5,11,r'WW-mode $\sqrt{s}$=160 GeV',fontsize=20,color='red',fontfamily='serif')
ax.text(1.5,36,r'H-mode $\sqrt{s}$=240 GeV',fontsize=20,color='black',fontfamily='serif')
ax.text(2.5,77,r'$\Lambda_s = 200$GeV $L$=$\frac{1}{\Lambda^2_s}$$\bar{\chi}\chi\bar{e}e$',fontsize=26,fontfamily='serif')


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


ax.set_ylim(1, 200)
ax.set_xlim(1,200)
ax.set_xlabel(r'$m_\chi$ (GeV)',fontsize=24,fontfamily='serif')
ax.set_ylabel(r'$\sigma$ (pb)',fontsize=24,fontfamily='serif')

# plt.savefig('/Users/yohengxu/Desktop/newfig/xsection_4fss_1.pdf',format='pdf')
plt.savefig('/home/xyh/texworkbench/cepc/paperdraft/figs/xsection_4fss_1.pdf',format='pdf')

plt.show()