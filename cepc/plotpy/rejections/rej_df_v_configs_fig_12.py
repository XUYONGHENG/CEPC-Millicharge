import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# print(np.load('../../plotCSV/df_h_formal_1-100.npy'))

eftexclusion_h_small = np.load('/home/xyh/PycharmProjects/cepc/plotCSV/zp_v_h_formal_1-50.npy')
eftexclusion_h_large = np.load('/home/xyh/PycharmProjects/cepc/plotCSV/zp_v_h_formal_50-100.npy')
eftexclusion_h = np.vstack((eftexclusion_h_small,eftexclusion_h_large[:-1]))
eftexclusion_w = np.load('/home/xyh/PycharmProjects/cepc/plotCSV/zp_v_w_formal_1-70.npy')
eftexclusion_z = np.load('/home/xyh/PycharmProjects/cepc/plotCSV/zp_v_z_formal_1-40.npy')

eftexclusion_h = np.vstack((eftexclusion_h[:109],[75,1e-5],eftexclusion_h[109:]))
eftexclusion_h = np.vstack((eftexclusion_h,[104,1e8]))
eftexclusion_w = np.vstack((eftexclusion_w[:-1],[70,1e8]))
eftexclusion_z = np.vstack((eftexclusion_z[:-1],[40,1e8]))



constraint_visible = np.array(pd.read_csv('../../plotCSV/constraint/visible_axial.csv',header=None))

constraint_direct_detection = np.load('../../plotCSV/constraint/xenon1t.npy')
constraint_direct_detection = np.vstack(([constraint_direct_detection[0,0],1e8],constraint_direct_detection))

fig, ax = plt.subplots(figsize=(12,9))

print(constraint_direct_detection)
print(eftexclusion_w.shape)
# input('halt')

lh, = ax.plot(eftexclusion_h[:,0],eftexclusion_h[:,1],linewidth=3,linestyle='solid',c='black')
lw, = ax.plot(eftexclusion_w[:,0],eftexclusion_w[:,1],linewidth=3,linestyle='dashed',c='red')
lz, = ax.plot(eftexclusion_z[:,0],eftexclusion_z[:,1],linewidth=3,linestyle=':',c='blue')
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

ax.text(1.2,0.04,'Visible Channel',fontsize=24,rotation=-0,color='grey',fontfamily='serif')
ax.text(12,2e-5,'XENON1T',fontsize=24,color='green',fontfamily='serif')
ax.text(1.2,1e-4,s=r"$m_{Z'}=150$GeV $g_\chi^V=1$",fontsize=24,fontfamily='serif')

ax.set_xlim((1,120))
ax.set_ylim((1e-6,5e-1))

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

ax.set_xticklabels([1,1,10,100], fontdict={'family':'serif'}, minor=False)

ax.legend((lh,lw,lz),('H-mode','WW-mode','Z-mode'),loc='lower left',fontsize=24,framealpha=0)


plt.savefig('/home/xyh/texworkbench/cepc/paperdraft/figs/dfrej_3.pdf',format='pdf')
# plt.savefig('/Users/yohengxu/Desktop/dfrej_3.pdf',format='pdf')
plt.show()