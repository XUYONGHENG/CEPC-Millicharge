import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

mass = 10**np.linspace(0,2,21)


## Load & prepare the data.
hvvx = np.array(pd.read_table('../../plotCSV/xsectionplot/zpplot.csv',header=None))
hvvx = np.concatenate((hvvx,np.array([[0]])))

zvvx = np.array(pd.read_table('../../plotCSV/xsectionplot/zpplotz.csv',header=None))
wvvx = np.array(pd.read_table('../../plotCSV/xsectionplot/zpplotw.csv',header=None))



hmasses = np.linspace(1,120,120,endpoint=True)
zmasses = np.linspace(1,45,45,endpoint=True)
wmasses = np.linspace(1,80,80,endpoint=True)

wvvx = np.vstack((wvvx,np.array([[0]])))
print(hvvx.shape,zvvx.shape,wvvx.shape)

hmasses2 = np.linspace(74.99,75.01,101,endpoint=True)
hmasses2 = (hmasses2-75)*1000
hvvx2 = np.array(pd.read_table('../../plotCSV/xsectionplot/zpplotzoom.csv',header=None))



### Draw!

fig,ax = plt.subplots(figsize=(9,6.75))

lnh, = ax.plot(hmasses,hvvx[:,0],linewidth=3, linestyle = 'solid',color='black')
lnw, = ax.plot(wmasses,wvvx[:,0],linewidth=3, linestyle = '-.',color='red')
lnz, = ax.plot(zmasses,zvvx[:,0],linewidth=3, linestyle = ':',color='blue')

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


# Write stuff
ax.text(1.5,18e-1,r'$Z^\prime$ portal model $g^V_\chi = 1$ $g^V_f = 0.01$',fontsize=20,fontfamily='serif')
ax.text(2,2.5e-3,r'Z-mode $\sqrt{s}$=91.2 GeV',fontsize=20,color='blue',rotation=0,fontfamily='serif')
ax.text(2,5e-1,r'WW-mode $\sqrt{s}$=160 GeV',fontsize=20,color='red',rotation=0,fontfamily='serif')
ax.text(2,3e-2,r'H-mode $\sqrt{s}$=240 GeV',fontsize=20,color='black',rotation=0,fontfamily='serif')


# Tune
ax.set_ylim(1e-3, 5)
ax.set_xlim(1,120)

ax.set_xlabel(r'$m_\chi$ (GeV)',fontsize=24,fontfamily='serif')
ax.set_ylabel(r'$\sigma$ (pb)',fontsize=24,fontfamily='serif')

# ax.set_yticklabels([0.001,1,10,100])
ax.set_xticklabels([1,1,10,100], fontdict=None, minor=False,fontfamily='serif')

ax2 = fig.add_axes([0.68,0.58,.12,.12])
lzoominh, = ax2.plot(hmasses2,hvvx2[:,0],color='black')

ax2.set_xlabel(r'$m_\chi-M_{Z^\prime}/2$ (MeV)',fontsize=12,fontfamily='serif')
ax2.set_ylabel(r'$\sigma$ (pb)',fontsize=12,fontfamily='serif')

ax2.spines['top'].set_linewidth(1.5)
ax2.spines['bottom'].set_linewidth(1.5)
ax2.spines['left'].set_linewidth(1.5)
ax2.spines['right'].set_linewidth(1.5)
ax2.xaxis.set_tick_params(width=1.5, which='minor')
ax2.xaxis.set_tick_params(width=1.5)
ax2.yaxis.set_tick_params(width=1.5, which='minor')
ax2.yaxis.set_tick_params(width=1.5)

ax2.tick_params(which = 'major', direction='in',top=True,right=True)
ax2.tick_params(which = 'minor',direction='in',top=True,right=True)



plt.savefig('/home/xyh/texworkbench/cepc/paperdraft/figs/xsection_df_2.pdf',format='pdf')
# plt.savefig('/Users/yohengxu/Desktop/newfig/xsection_df_2.pdf',format='pdf')


plt.show()
