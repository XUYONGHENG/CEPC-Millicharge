import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


zp_axial_exclusion_h_small = np.load('/home/xyh/PycharmProjects/cepc/plotCSV/zp_a_h_formal_1-50.npy')
zp_axial_exclusion_h_large= np.load('/home/xyh/PycharmProjects/cepc/plotCSV/zp_a_h_formal_50-100.npy')
zp_axial_exclusion_h = np.vstack((zp_axial_exclusion_h_small,zp_axial_exclusion_h_large))
zp_axial_exclusion_w = np.load('/home/xyh/PycharmProjects/cepc/plotCSV/zp_a_w_formal_1-70.npy')
zp_axial_exclusion_z = np.load('/home/xyh/PycharmProjects/cepc/plotCSV/zp_a_z_formal_1-40.npy')

zp_axial_exclusion_h = np.vstack((zp_axial_exclusion_h[:-1],[104,1e8]))
zp_axial_exclusion_w = np.vstack((zp_axial_exclusion_w[:-1],[70,1e8]))
zp_axial_exclusion_z = np.vstack((zp_axial_exclusion_z[:-1],[40,1e8]))


# constraint_visible = np.load('../../plotCSV/constraint/df_visible.npy')
constraint_visible = np.array(pd.read_csv('../../plotCSV/constraint/visible_axial.csv',header=None))
constraint_direct_detection = np.load('../../plotCSV/constraint/xenon1tsd.npy')

constraint_direct_detection = np.vstack(([constraint_direct_detection[0,0],1e8],constraint_direct_detection))

fig, ax = plt.subplots(figsize=(12,9))


lh, = ax.plot(zp_axial_exclusion_h[:,0],zp_axial_exclusion_h[:,1],linewidth=3,linestyle='solid',c='black')
lw, = ax.plot(zp_axial_exclusion_w[:,0],zp_axial_exclusion_w[:,1],linewidth=3,linestyle='dashed',c='red')
lz, = ax.plot(zp_axial_exclusion_z[:,0],zp_axial_exclusion_z[:,1],linewidth=3,linestyle=':',c='blue')
lc_directdetection, = ax.plot(constraint_direct_detection[:,0],constraint_direct_detection[:,1],c='green',
                              linestyle='-.',linewidth=3)

lc_visible, = ax.plot(constraint_visible[:,0],constraint_visible[:,1],\
                color='grey',linestyle='-.',linewidth=3)

# ax.fill_between(constraint_direct_detection[:,0],constraint_direct_detection[:,1],y2=10,\
#                 color='green',alpha=0.3)
# ax.fill_between(constraint_visible[:,0],constraint_visible[:,1],y2=10,\
#                 color='grey',alpha=0.3)


ax.set_xscale('log')
ax.set_yscale('log')

ax.text(1.2,0.025,'Visible Channel',fontsize=24,rotation=-0,color='grey',fontfamily='serif')
ax.text(7,2e-1,'XENON1T',fontsize=24,color='green',fontfamily='serif')
ax.text(10,2e-4,s=r"$m_{Z'}=150$GeV $g^\chi_A=1$",fontsize=24,fontfamily='serif')

ax.set_xlim((1,120))
ax.set_ylim((5e-5,5e-1))

ax.set_xlabel(r'$m_\chi$ (GeV)',fontsize=25,fontfamily='serif')
ax.set_ylabel(r'$g_f^V$',fontsize=25,fontfamily='serif')


ax.tick_params(which = 'major', length=8,direction='in',top=True,right=True)
ax.tick_params(which = 'minor', length=6,direction='in',top=True,right=True)

for label in ax.xaxis.get_minorticklabels():
    label.set_fontsize(24)
    label.set_fontname('serif')
for label in ax.xaxis.get_majorticklabels():
    label.set_fontsize(24)
    label.set_fontname('serif')

for label in ax.yaxis.get_minorticklabels():
    label.set_fontsize(24)
    label.set_fontname('serif')
for label in ax.yaxis.get_majorticklabels():
    label.set_fontsize(24)
    label.set_fontname('serif')

ax.spines['top'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
ax.xaxis.set_tick_params(width=1.5, which='minor')
ax.xaxis.set_tick_params(width=1.5)
ax.yaxis.set_tick_params(width=1.5, which='minor')
ax.yaxis.set_tick_params(width=1.5)

# ax.set_xticklabels([1,1,10,100], fontdict={'family':'serif'}, minor=False)

ax.legend((lh,lw,lz),('H-mode','WW-mode','Z-mode'),loc='lower left',fontsize=24,framealpha=0)


plt.savefig('/home/xyh/texworkbench/cepc/paperdraft/figs/dfrejaxial_3.pdf',format='pdf')
# plt.savefig('/Users/yohengxu/Desktop/dfrej_3.pdf',format='pdf')
plt.show()