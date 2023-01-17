import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Initialising figure & axis.

fig,ax = plt.subplots(figsize=(12,9))

## Loading & drawing existing constraints.

constraint_mini = np.load('../../plotCSV/constraint/miniboone.npy')
constraint_besiii = np.load('../../plotCSV/constraint/besiii.npy')
constraint_collders = np.load('../../plotCSV/constraint/colliders.npy')
constraint_e613 = np.array(pd.read_csv('../../plotCSV/constraint/e613c.csv'))

ax.fill_between(constraint_mini[:,0],constraint_mini[:,1],y2=10,color='orange',alpha=0.3)
ax.fill_between(constraint_besiii[:,0],constraint_besiii[:,1],y2=10,color='green',alpha=0.3)
ax.fill_between(constraint_collders[:,0],constraint_collders[:,1],y2=10,color='grey',alpha=0.3)
ax.fill_between(constraint_e613[:,0],constraint_e613[:,1],y2=10,color='purple',alpha=0.3)

ax.text(2,0.3,'Colliders',fontsize=20, color='grey',fontfamily='serif')
ax.text(0.18,0.5,'MiniBooNE',fontsize=20,color='orange',rotation=270,fontfamily='serif')
ax.text(0.23,0.001,'BESIII',fontsize=20,color='Green',fontfamily='serif')
ax.text(0.17,0.003,r'E613',fontsize=20,color='purple',fontfamily='serif')

## Loading data to draw

mqexclusion_h = np.load('../../plotCSV/constraint/mqh_formal_0.1-100.npy')
mqexclusion_z = np.load('../../plotCSV/constraint/mqz_formal_0.1-38.npy')
mqexclusion_w = np.load('../../plotCSV/constraint/mqw_formal_0.1-67.npy')

mqexclusion_h = np.vstack((mqexclusion_h,[104,1e8]))
mqexclusion_z = np.vstack((mqexclusion_z,[40,1e8]))
mqexclusion_w = np.vstack((mqexclusion_w,[69,1e8]))


l21, = ax.plot(mqexclusion_h[:,0],mqexclusion_h[:,1],linewidth=3,linestyle='solid',c='black')
l22, = ax.plot(mqexclusion_z[:,0],mqexclusion_z[:,1],linewidth=3,linestyle='solid',c='red')
l23, = ax.plot(mqexclusion_w[:,0],mqexclusion_w[:,1],linewidth=3,linestyle=':',c='blue')


ax.set_xscale('log')
ax.set_yscale('log')

ax.set_xlim((0.1,120))
ax.set_ylim((5e-4,5))

for label in ax.xaxis.get_majorticklabels():
    label.set_fontsize(16)
    label.set_fontname('serif')
for label in ax.xaxis.get_minorticklabels():
    label.set_fontsize(16)
    label.set_fontname('serif')
for label in ax.yaxis.get_majorticklabels():
    label.set_fontsize(16)
    label.set_fontname('serif')
for label in ax.yaxis.get_minorticklabels():
    label.set_fontsize(16)
    label.set_fontname('serif')

ax.tick_params(which = 'major', length=17,direction='in',top=True,right=True)
ax.tick_params(which = 'minor', length=9,direction='in',top=True,right=True)



ax.set_xlabel(r'$m_\chi$ (GeV)',fontsize=24,fontfamily='serif')
ax.set_ylabel(r'$\epsilon$',fontsize=24,fontfamily='serif')



# ax.text(3,0.06,r'$WW$ mode',fontsize=20,color='blue',rotation=15)
# ax.text(2,0.04,'Higgs Factory mode',fontsize=20,color='black',rotation=15)
# ax.text(3,0.018,r'$Z$-pole mode',fontsize=20,color='red',rotation=12.5)
# ax.text(36,0.1,r'Combined',fontsize=20,color='green',rotation=55)

ax.spines['top'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
ax.xaxis.set_tick_params(width=1.5, which='minor')
ax.xaxis.set_tick_params(width=1.5)
ax.yaxis.set_tick_params(width=1.5, which='minor')
ax.yaxis.set_tick_params(width=1.5)
ax.set_xticklabels([1,0.1,1,10,100], fontdict={'family':'serif'}, minor=False)

ax.legend((l21,l22,l23),
           ('H-mode','Z-mode','WW-mode'),loc='lower right',prop={'family':'serif','size':24},framealpha=0)

plt.savefig('/home/xyh/texworkbench/cepc/paperdraft/figs/mqrej_configs_2.pdf',format='pdf')
# plt.savefig('/Users/yohengxu/Desktop/newfig/mqrej_configs_2.pdf',format='pdf')
plt.show()