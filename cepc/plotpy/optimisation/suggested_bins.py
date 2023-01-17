import numpy as np
import matplotlib.pyplot as plt

data1 = np.load('/home/xyh/PycharmProjects/cepc/plotCSV/optimisation/selectedbins1.npy')
data10 = np.load('/home/xyh/PycharmProjects/cepc/plotCSV/optimisation/selectedbins10.npy')
fig1,fig10 = np.ones(shape=(30,30)),np.ones(shape=(30,30))

# data1,data10 = np.int(data1),np.int(data10)
print(data10)
for i in range(data1.shape[0]):
    fig1[int(data1[i,0]),int(data1[i,1])] = 0

for i in range(data10.shape[0]):
    fig10[int(data10[29-i,0]),int(data10[29-i,1])] = 0

fig10 = fig10[::-1]

fig,ax = plt.subplots(figsize=(9,6.75))
ax.imshow(fig10,cmap='gist_gray')
# fig.rotate(180)
ax.set_xticks(ax.get_xticks()[::1])
ax.set_xlim(0,30)

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


ax.spines['top'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
ax.xaxis.set_tick_params(width=1.5, which='minor')
ax.xaxis.set_tick_params(width=1.5)
ax.yaxis.set_tick_params(width=1.5, which='minor')
ax.yaxis.set_tick_params(width=1.5)

ax.tick_params(which = 'major', length=17,direction='in',top=True,right=True)
ax.tick_params(which = 'minor', length=9,direction='in',top=True,right=True)

ax.set_xticklabels([-1,-1,'-2/3','-1/3',0,'1/3','2/3',1,1], fontdict={'fontsize':18}, minor=False)
ax.set_yticklabels(range(135,0,-15), fontdict={'fontsize':18}, minor=False)

ax.set_xlabel(r'$\cos\theta$',fontsize=20,fontfamily='serif')
ax.set_ylabel(r'$E_\gamma$ (GeV)',fontsize=20,fontfamily='serif')

ax.text(6,10,'Suggested bins',fontsize=20,fontfamily='serif')
ax.text(1,14,r'Millicharge $\epsilon=0.01$,$m_\chi=10$ GeV',fontsize=20,fontfamily='serif')
ax.text(4,18,r'$\sqrt{s}=240$ GeV,$\int\cal{L}=5.6$ ab$^{-1}$',fontsize=20,fontfamily='serif')
plt.savefig('/home/xyh/texworkbench/cepc/paperdraft/figs/suggestbins.pdf',format='pdf')
plt.show()
