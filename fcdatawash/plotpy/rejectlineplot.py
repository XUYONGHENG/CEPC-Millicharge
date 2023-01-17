import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib import cm
import pandas as pd
from mpl_toolkits import mplot3d

# filtered939,filtered984 = np.load("/store/eevva/pveve2939withob.npy"),np.load("/store/eeeea/filtered984.npy")
# egamma939,cosgamma939 = filtered939[:,8],filtered939[:,17]
# egamma984,cosgamma984 = filtered984[:,8],filtered984[:,17]
# el2939,el2984 = filtered939[:,4],filtered984[:,4]
# el1939,el1984 = filtered939[:,0],filtered984[:,0]
# cosl1939,cosl1984 = filtered939[:,15],filtered984[:,15]
# cosl2939,cosl2984 = filtered939[:,16],filtered984[:,16]
# ptl1939,ptl2939,ptgamma939 = filtered939[:,18],filtered939[:,19],filtered939[:,20]
# ptl1984,ptl2984,ptgamma984 = filtered984[:,18],filtered984[:,19],filtered984[:,20]
# phil1939,phil2939,phigamma939 = filtered939[:,-3],filtered939[:,-2],filtered939[:,-1]
# phil1984,phil2984,phigamma984 = filtered984[:,-3],filtered984[:,-2],filtered984[:,-1]
# mlepton939 = ((filtered939[:,0]+filtered939[:,4])**2-(filtered939[:,1]+filtered939[:,5])**2-(filtered939[:,2]+filtered939[:,6])**2-(filtered939[:,3]+filtered939[:,7])**2)**(1/2)
# threeDdata1 = np.column_stack((egamma939,cosgamma939))


# print(threeDdata1.shape)
# np.savetxt("plotCSV/pveve2939.csv",threeDdata1,delimiter=', ')
# np.savetxt("egamma939.csv",egamma939,delimiter=', ')
# np.savetxt("cosgamma939.csv",cosgamma939,delimiter=', ')

# distribution, xedges, yedges =    np.histogram2d(egamma939,cosgamma939,bins=50,normed=True,range=[[0,125],[-1,1]])
#
# xpos, ypos = np.meshgrid(xedges[:-1],yedges[:-1])
# xpos=xpos.flatten('F')
# ypos=ypos.flatten('F')
# zpos=np.zeros_like(xpos)
#
# dx = 0.5 * np.ones_like(zpos)
# dy = dx
# dz = distribution.flatten()
# print(dz.shape)
# fig = plt.figure()
# ax =fig.add_subplot(111,projection='3d')
# ax.bar3d(xpos,ypos,zpos,dx,dy,dz)
# plt.show()
#############
#Basic 3D framework
#############
# plt.figure()
# ax = plt.axes(projection='3d')
# zline = np.linspace(0, 15, 1000)
# xline = np.sin(zline)
# yline = np.cos(zline)
# ax.plot3D(xline,yline,zline)
# plt.show()

###############
###############
#E vs Cos\theta_\gamma
###############
# fig, ax = plt.subplots()
# h = ax.hist2d(cosgamma984,egamma984,bins=30,norm=LogNorm())
# plt.colorbar(h[3],ax=ax)
# ax.set_title(r'$|Cos\theta_l|>0.984$, 35139 Events')
# plt.xlabel(r'$Cos\theta_\gamma$')
# plt.ylabel(r'$E_\gamma$')
# plt.savefig("984EvCos.png")
###############
# #
# plt.figure(figsize=(10,8))
# plt.subplot(2,1,1)
# plt.title(r'$Cos\theta$ and Energy Distribution of leptons at angular cut of 0.984')
# plt.hist(el1939,bins=200,color='blue',alpha=0.5,label='electron')
# plt.hist(el2939,bins=200,color='r',alpha=0.5,label='positron')
# plt.legend(loc='upper center')
# plt.xlabel(r'$E\ (GeV)$')
# plt.ylabel(r'$Count$')
# plt.subplot(2,1,2)
# plt.hist(cosl1939,bins=200,color='blue',alpha=0.5,label='electron')
# plt.hist(cosl2939,bins=200,color='red',alpha=0.5,label='postiron')
# plt.legend(loc='upper center')
# plt.xlabel(r'$Cos\theta$')
# plt.ylabel(r'$Count$')
# plt.savefig('939leptonhist.png')

#
##########################
#
# plt.figure(figsize=(10,5))
# plt.hist(ptl2939,bins=200,color='red',alpha=0.5,label='positron')
# plt.hist(ptl1939,bins=200,color='blue',alpha=0.5,label='electron')
# plt.hist(ptgamma939,bins=200,color='yellow',alpha=0.5,label='photon')
# plt.xlabel(r'$p_T$')
# plt.ylabel(r'Count')
# plt.legend(loc='upper left')
# plt.title(r'$p_T    $ Distribution of final state leptons w/ cos$\theta$ cut of 0.939')
# plt.savefig('939pthist.png')

datac = np.array(pd.read_csv('../plotCSV/constraint.csv'))
datac[:,0] = 1e-9*datac[:,0]

datac2 = np.column_stack((np.linspace(0,140,2),1/3*np.ones(shape=(2,))))
for i in range(2,8):
    datac[i,0] = 1
for i in range(12,17):
    datac[i,0] = 45
datac[12,1] = 2.434105e-1
datac[-2] = [100,0.70396]
datac[-1,0] = 100
print(datac)
data1 = np.load('../plotCSV/sb2dots1.npy')
data1a = np.load('../plotCSV/sb2dots1_10fb-1.npy')
data1b = np.load('../plotCSV/sb2dots1_10fb-2.npy')
data1c = np.load('../plotCSV/sb2dots1_10fb-3.npy')

print(data1a)
dataup = np.column_stack((np.linspace(1,100,datac.shape[0]),10*np.ones(shape=(datac.shape[0]))))
print(dataup.shape)

fig = plt.figure()
ax1,ax2 = plt.subplot(1,2,1),plt.subplot(1,2,2)
# l1, = ax.plot(data[:,0],data[:,1],linewidth=2.25,linestyle='dashed',color='r')
l1, = ax1.plot(data1[:,0],data1[:,1],linewidth=3,linestyle='solid',color='black')
l1c, = ax1.plot(datac[:,0],datac[:,1],linewidth=0,linestyle='solid',color='gray')
l1c2 = ax1.plot(datac2[:,0],datac2[:,1],linewidth=0,color = 'red')
l1a, = ax1.plot(data1a[:,0],data1a[:,1],linewidth=3,linestyle='dashed',color='blue')
l1b, = ax1.plot(data1b[:,0],data1b[:,1],linewidth=3,linestyle='dashed',color='red')
l1d, = ax1.plot(data1c[:,0],data1c[:,1],linewidth=3,linestyle='dashed',color='grey')

# l1u, = ax1.plot(dataup[:,0],dataup[:,1],10)
ax1.fill_between(datac[:,0],datac[:,1],y2=10,color='blue',alpha=0.6)
ax1.fill_between(datac2[:,0],datac2[:,1],y2=10,color='red',alpha=0.6)

ax1.set_xscale('log')
ax1.set_ylim(0.02,1)
ax1.set_yscale('log')
ax1.set_xlabel(r'$m_\chi$(GeV)',fontdict={'fontsize':25})
ax1.set_ylabel(r'$\epsilon$',fontdict={'fontsize':25})
ax1.legend((l1d,l1,l1a,l1b,),(r'2.5 $ab^{-1}$',r'5 $ab^{-1}$',r'10 $ab^{-1}$',r'20 $ab^{-1}$',),loc='lower right',fontsize=15)

ax1.tick_params(which = 'major', length=15,direction='in')
ax1.tick_params(which = 'minor', length=7,direction='in')


data2 = np.load('../plotCSV/4fsbdots4.npy')
data2a = np.load('../plotCSV/4fsbdots5.npy')
data2b = np.load('../plotCSV/4fsbdots6.npy')
data2c = np.load('../plotCSV/4fsbdots7.npy')


l2, = ax2.plot(data2[:,0],data2[:,1],linewidth=3,linestyle='dashed',color='grey')
l2a, = ax2.plot(data2a[:,0],data2a[:,1],linewidth=3,linestyle='solid',color='black')
l2b, = ax2.plot(data2b[:,0],data2b[:,1],linewidth=3,linestyle='dashed',color='blue')
l2c, = ax2.plot(data2c[:,0],data2c[:,1],linewidth=3,linestyle='dashed',color='red')

ax2.set_ylim(1000,5000)
ax2.set_yscale('log')
ax2.set_xscale('log')
ax2.tick_params(which = 'major', length=15,direction='in')
ax2.tick_params(which = 'minor', length=7,direction='in')
ax2.legend((l2,),('four-fermion',),loc=2,fontsize=15)
ax2.set_xlabel(r'$m_\chi$(GeV)',fontdict={'fontsize':25})
ax2.set_ylabel(r'$\Lambda$',fontdict={'fontsize':16})
ax1.text(1,0.15,r'CEPC constraint on $\epsilon$',fontsize=25)
ax1.text(0.5,0.5,r'Existing experimental bound',fontsize=25)
ax2.text(3,1300,r'CEPC constraint on $\Lambda$',fontsize=25)
ax2.legend((l1d,l1,l1a,l1b,),(r'2.5 $ab^{-1}$',r'5 $ab^{-1}$',r'10 $ab^{-1}$',r'20 $ab^{-1}$',),loc='lower right',fontsize=15)


for label in ax1.xaxis.get_majorticklabels():
    label.set_fontsize(16)
    label.set_fontname('verdana')
for label in ax1.xaxis.get_minorticklabels():
    label.set_fontsize(16)
    label.set_fontname('verdana')
for label in ax1.yaxis.get_majorticklabels():
    label.set_fontsize(16)
    label.set_fontname('verdana')
for label in ax1.yaxis.get_minorticklabels():
    label.set_fontsize(16)
    label.set_fontname('verdana')
for label in ax2.xaxis.get_majorticklabels():
    label.set_fontsize(16)
    label.set_fontname('verdana')
for label in ax2.xaxis.get_minorticklabels():
    label.set_fontsize(16)
    label.set_fontname('verdana')
for label in ax2.yaxis.get_majorticklabels():
    label.set_fontsize(16)
    label.set_fontname('verdana')
for label in ax2.yaxis.get_minorticklabels():
    label.set_fontsize(16)
    label.set_fontname('verdana')

# ax.text(,0.)
# ax.legend((l1,l2),(r'Old cuts',r'New cuts'),loc='lower center',fontsize = 15)
for tick in ax1.xaxis.get_major_ticks():
    tick.label.set_fontsize(20)
for tick in ax1.xaxis.get_minor_ticks():
    tick.label.set_fontsize(16)
for tick in ax1.yaxis.get_major_ticks():
    tick.label.set_fontsize(20)
for tick in ax1.yaxis.get_minor_ticks():
    tick.label.set_fontsize(16)
# ax1.text(1,0.015,'CECP constraint on millicharge DM',fontsize=18)
# ax1.text(0,0.015,'Existing experimental bound',fontsize=18)
plt.show()
# print(data1)