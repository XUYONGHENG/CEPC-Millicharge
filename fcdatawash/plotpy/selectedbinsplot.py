import numpy as np
import matplotlib.pyplot as plt

data1,data10 = np.load('../plotCSV/selectedbins1.npy'),np.load('../plotCSV/selectedbins10.npy')
print(data1)
fig1,fig10 = np.ones(shape=(30,30)),np.ones(shape=(30,30))

# data1,data10 = np.int(data1),np.int(data10)

for i in range(data1.shape[0]):
    fig1[int(data1[i,0]),int(data1[i,1])] = 0

for i in range(data10.shape[0]):
    fig10[int(data10[i,0]),int(data10[i,1])] = 0

# fig = plt.figure()
# ax1,ax2 = plt.subplot(1,2,1),plt.subplot(1,2,2)
# ax1.imshow(fig1,cmap='Greys')
# ax2.imshow(fig10,cmap='Greys')
# ax1.set_title(r'$m_\chi$ = 1 GeV',fontsize=24)
# ax1.set_xlabel(r'cos$\theta_\gamma$',fontsize=24)
# ax1.set_ylabel(r'$E_\gamma$',fontsize=24)
#
# ax2.set_title(r'$m_\chi$ = 10 GeV',fontsize=24)
# ax2.set_xlabel(r'cos$\theta_\gamma$',fontsize=24)
# ax2.set_ylabel(r'$E_\gamma$',fontsize=24)
# plt.show()
fig,ax = plt.subplots(figsize=(10,7.5))
ax.imshow(fig10,cmap='gist_gray')
ax.set_xticks(ax.get_xticks()[::1])
ax.set_xlim(0,30)


ax.spines['top'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
ax.xaxis.set_tick_params(width=1.5, which='minor')
ax.xaxis.set_tick_params(width=1.5)
ax.yaxis.set_tick_params(width=1.5, which='minor')
ax.yaxis.set_tick_params(width=1.5)

ax.set_xticklabels([-1,-1,'-2/3','-1/3',0,'1/3','2/3',1,1], fontdict={'fontsize':18}, minor=False)
ax.set_yticklabels([30,30,45,60,75,90,105,120,1], fontdict={'fontsize':18}, minor=False)

ax.set_xlabel(r'$\cos\theta$',fontsize=24)
ax.set_ylabel(r'$E_\gamma$ (GeV)',fontsize=24)

ax.text(6,10,'Suggested bins',fontsize=24)
ax.text(1,14,r'Millicharge $\epsilon=0.01$,$m_\chi=10$ GeV',fontsize=24)
ax.text(4,18,r'$\sqrt{s}=240$ GeV,$\int\cal{L}=5.6$ ab$^{-1}$',fontsize=24)
plt.savefig('../figformal/suggestbins.pdf',format='pdf')
plt.show()
