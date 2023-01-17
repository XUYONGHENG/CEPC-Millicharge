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
totalsections = 10*np.array([3.557, 3.532, 3.52, 3.496, 3.469, 3.448, 3.412, 3.375, 3.327, 3.276, 3.224, 3.150, 3.096,
                          3.034, 3.053, 2.972, 2.879, 2.767, 2.592, 2.292, 1.632])
masses = 10**np.linspace(0,2,21,endpoint=True)

data= np.column_stack((masses[:],totalsections[:]))
data1 = np.load('../plotCSV/sbdots4.npy')
fig,ax = plt.subplots()
l1, = ax.plot(data[:,0],data[:,1],linewidth=2.25,linestyle='dashed',color='r')
l2, = ax.plot(data1[:,0],data1[:,1],linewidth=2.25,linestyle='dashed',color='blue')
ax.set_xscale('log')
ax.set_ylim(0.01,0.15)
ax.set_yscale('log')
ax.set_xlabel(r'$m_\chi\ (\rm GeV}$)',fontdict={'fontsize':25})
ax.set_ylabel(r'$\sigma{\rm\ (ab)}$',fontdict={'fontsize':25})
ax.tick_params(which = 'major', length=15,direction='in')
ax.tick_params(which = 'minor', length=7,direction='in')
# ax.legend((l1,l2),(r'Old cuts',r'New cuts'),loc='lower center',fontsize = 15)
for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(20)
for tick in ax.xaxis.get_minor_ticks():
    tick.label.set_fontsize(16)
for tick in ax.yaxis.get_major_ticks():
    tick.label.set_fontsize(20)
for tick in ax.yaxis.get_minor_ticks():
    tick.label.set_fontsize(16)
ax.text(1,0.1,'CEPC constraint on millicharge DM',fontsize=25)
plt.show()