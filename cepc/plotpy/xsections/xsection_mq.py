import numpy as np
import matplotlib.pyplot as plt


hvvx = np.load('../../plotCSV/xsectionplot/mqploth.npy')
zvvx = np.load('../../plotCSV/xsectionplot/mqplotz.npy')
wvvx = np.load('../../plotCSV/xsectionplot/mqplotw.npy')

fig,ax = plt.subplots(figsize=(9,6.75))

lnh, = ax.plot(hvvx[:,0],hvvx[:,1],linewidth=3, linestyle = 'solid',color='black')
lnw, = ax.plot(wvvx[:,0],wvvx[:,1],linewidth=3, linestyle = '-.',color='red')
lnz, = ax.plot(zvvx[:,0],zvvx[:,1],linewidth=3, linestyle = ':',color='blue')

ax.set_xscale('log')
ax.set_yscale('log')


##########
ax.spines['top'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
ax.xaxis.set_tick_params(width=1.5, which='minor')
ax.xaxis.set_tick_params(width=1.5)
ax.yaxis.set_tick_params(width=1.5, which='minor')
ax.yaxis.set_tick_params(width=1.5)
##############


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

ax.text(5,2.5e-5,r'Millicharge $\epsilon=0.01$',fontsize=26,fontfamily='serif')
# ax.text(4.5,1.8e-2,r'$\epsilon=0.01$',fontsize=20)


ax.text(1.6,1.5e-5,r'Z-mode $\sqrt{s}$=91.2 GeV',fontsize=20,color='blue',rotation=-6,fontfamily='serif')
ax.text(1.6,5.3e-6,r'WW-mode $\sqrt{s}$=160 GeV',fontsize=20,color='red',rotation=-5,fontfamily='serif')
ax.text(1.6,2.5e-6,r'H-mode $\sqrt{s}$=240 GeV',fontsize=20,color='black',rotation=-3,fontfamily='serif')

ax.set_ylim(5e-7, 5e-5)
ax.set_xlim(1,200)

ax.set_xlabel(r'$m_\chi$ (GeV)',fontsize=24,fontfamily='serif')
ax.set_ylabel(r'$\sigma$ (pb)',fontsize=24,fontfamily='serif')

ax.set_xticklabels([1,1,10,100], fontdict=None, minor=False)

# plt.savefig('/Users/yohengxu/Desktop/newfig/xsection_mq_4.pdf',format='pdf')
plt.savefig('/home/xyh/texworkbench/cepc/paperdraft/figs/xsection_mq_4.pdf',format='pdf')

plt.show()
