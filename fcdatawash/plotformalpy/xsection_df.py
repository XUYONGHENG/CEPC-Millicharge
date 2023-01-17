import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

mass = 10**np.linspace(0,2,21)

hvvx = np.array(pd.read_table('../plotCSV/zppolth.csv',header=None))
zvvx = np.array(pd.read_table('../plotCSV/zppoltz.csv',header=None))
wvvx = np.array(pd.read_table('../plotCSV/zppoltw.csv',header=None))
hmasses = np.linspace(1,100,100,endpoint=True)
zmasses = np.linspace(1,45,45,endpoint=True)
wmasses = np.linspace(1,80,80,endpoint=True)

wvvx = np.vstack((wvvx,np.array([[0]])))
print(hvvx.shape,zvvx.shape,wvvx.shape)
# zxsection = np.column_stack((mass[:17],zxsection))
# zxsection = np.vstack((zxsection,np.array([45.5,0.0545])))

# print(zxsection)
# input('halt')
# np.save('/store/disposed/milliq/cepcz/zxsection.npy',zxsection)

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

ax.text(6,12e-3,r'$Z^\prime$ portal model',fontsize=20)
ax.text(4.5,7e-3,r'$g^A = 0, g^V_\chi = 1,g^V_f = 0.01$',fontsize=20)


ax.text(2,2.5e-3,r'Z-pole,$\sqrt{s}$=91.2 GeV',fontsize=20,color='blue',rotation=0)
ax.text(2,5e-1,r'$W^+W^-$,$\sqrt{s}$=160 GeV',fontsize=20,color='red',rotation=0)
ax.text(1.6,7e-2,r'Higgs Factory,$\sqrt{s}$=240 GeV',fontsize=20,color='black',rotation=0)

ax.set_ylim(1e-3, 5)
ax.set_xlim(1,100)

ax.set_xlabel(r'$m_\chi$ (GeV)',fontsize=24)
ax.set_ylabel(r'$\sigma$ (pb)',fontsize=24)

ax.set_xticklabels([1,1,10,100], fontdict=None, minor=False)

plt.savefig('/home/xyh/texworkbench/cepc/paperdraft/figs/xsection_df_1.pdf',format='pdf')

# plt.savefig('../figformal/xsection_mq_2.pdf',format='pdf')
plt.show()
