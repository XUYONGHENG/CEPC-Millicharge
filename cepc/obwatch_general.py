import numpy as np
import matplotlib.pyplot as plt


class Data(object):
    def __init__(self,data,energy,colour=0,style='solid',width=2,normalised=True):
        self.data = data
        if normalised:
            self.data[:,-1] = (1/np.sum(data[:,-1]))*data[:,-1]
        print(np.sum(self.data[:,-1]))
        self.colour=colour
        self.energy = energy
        self.style = style
        self.width = width


def obsubplot(ax,x,ob):
    if ob == 0 or ob == 1:
        dots = hollow_bar_hist(x.data[:, ob], w=x.data[:, -1], z=-2, r=(1,x.energy/2))
    elif ob == 2:
        dots = hollow_bar_hist(x.data[:, ob], w=x.data[:, -1], z=-2, r=(-1,1))
    elif ob == 3:
        dots = hollow_bar_hist(x.data[:, ob], w=x.data[:, -1], z=-2, r=(1,x.energy))

    # print(dots.shape)
    line, = ax.plot(dots[:,0],dots[:,1],linestyle = x.style,linewidth = x.width,color = x.colour)
    return line


def decorate(ax,xlabel,ylabel,xlog=True,ylog=True):
    if xlog:
        ax.set_xscale('log')
    if ylog:
        ax.set_yscale('log')

    ax.set_xlabel(xlabel,fontsize=24,fontfamily='serif')
    ax.set_ylabel(ylabel,fontsize=24,fontfamily='serif')

    ax.tick_params(which = 'major', length=17,direction='in',top=True,right=True)
    ax.tick_params(which = 'minor', length=9,direction='in',top=True,right=True)

    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(18)
        tick.label.set_fontname('serif')

    for tick in ax.xaxis.get_minor_ticks():
        tick.label.set_fontsize(18)
        tick.label.set_fontname('serif')

    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(18)
        tick.label.set_fontname('serif')

    for tick in ax.yaxis.get_minor_ticks():
        tick.label.set_fontsize(18)
        tick.label.set_fontname('serif')


##Low coupling, high integration

### Core function. This one yields the data to be illustrated.

def hollow_bar_hist(data,w,r = (1,120),binsize = 0,z = 0):
    if not binsize:
        binsize = (r[1] - r[0]) / 50
    if r :
        a,b = np.histogram(data,bins=50,weights=w,range=r)[1],(np.histogram(data,bins=50,weights=w,range=r)[0]/binsize)
    else:
        a, b = np.histogram(data, bins=50, weights=w)[1], (np.histogram(data, bins=50, weights=w)[0] / binsize)
    c = np.zeros(shape=(a.shape[0]*2,2))
    # print(np.sum(b)*binsize)
    c[0] = np.array([a[0],z])
    c[-1] = np.array([a[-1],z])
    for i in range(0,a.shape[0]-1):
       c[2*i+1] = np.array([a[i],b[i]])
       c[2*i+2] = np.array([a[i+1],b[i]])
    return c


#### Painting function. It paint a single line on all 4 axes once a time, so you'll have to call the function 4 times
#### If not, check your code.
####
#### The axes parameter must be a iteratable object containing 4 plt axes.
#### data is a (X,5) ndarray.
#### Energy is your CoM frame energy.

def paintdata(axes,data,energy,colour=False,width=3,style=1):
    ## Unlike before, input data now must have 5 rows; otherwise the function will REJECT your input.
    # print(style)
    # print(type(style))
    i = data
    c1, c2, c3, c4 = hollow_bar_hist(i[:,0], w=i[:,-1], z=-2,r=(1,energy)), hollow_bar_hist(i[:,1], w=i[:,-1], z=-2.5,r=(1,energy)), hollow_bar_hist(
        i[:,2], w=i[:,-1], r=(-1, 1)), hollow_bar_hist(i[:,3], w=i[:,-1], z=-2.5, r=(1, 2*energy))
    c = [c1,c2,c3,c4]
    if style == 1:
        s = 'solid'
    elif style == 2:
        s = 'dashed'
    ls = []
    if colour:
        for j in range(4):
            l, = axes[j].plot(c[j][:,0],c[j][:,1],linewidth=width,c=colour)
            ls.append(l)
    else:
        for j in range(4):
            # print(style == 'solid')
            l, = axes[j].plot(c[j][:,0],c[j][:,1],linewidth=width)
            ls.append(l)
    return ls



def general_painter(datas,energy=240):
    energy=energy/2
    fig = plt.figure()
    ax1, ax2, ax3, ax4 = plt.subplot(2, 2, 1), plt.subplot(2, 2, 2), plt.subplot(2, 2, 3), plt.subplot(2, 2, 4)
    axes = [ax1,ax2,ax3,ax4]
    lines = []
    for data in datas:
        # print(data.style)
        lines.append(paintdata(axes=axes,data=data.data,colour=data.colour,width=data.width,style='solid',energy=energy))
    ax1.set_xlabel(r'$E_\gamma$ (GeV)',fontdict={'fontsize':25})
    ax2.set_xlabel(r'$p^T_\gamma$ (GeV)',fontdict={'fontsize':25})
    ax3.set_xlabel(r'$\theta_\gamma$',fontdict={'fontsize':25})
    ax4.set_xlabel(r'$m_{missing} (GeV)$',fontdict={'fontsize':25})


    ax1.tick_params(which = 'major', length=15,direction='in')
    ax2.tick_params(which = 'major', length=15,direction='in')
    ax3.tick_params(which = 'major', length=15,direction='in')
    ax4.tick_params(which = 'major', length=15,direction='in')


    ax1.tick_params(which = 'minor', length=7,direction='in')
    ax2.tick_params(which = 'minor', length=7,direction='in')
    ax3.tick_params(which = 'minor', length=7,direction='in')
    ax4.tick_params(which = 'minor', length=7,direction='in')


    ax1.set_yscale('log')
    ax2.set_yscale('log')
    ax3.set_yscale('log')
    ax4.set_yscale('log')


    ax1.set_ylabel(r'$d\sigma/E_\gamma\cdot(fb/GeV)^{-1}$',fontdict={'fontsize':25})
    ax2.set_ylabel(r'$d\sigma/p^T_\gamma\cdot(fb/GeV)^{-1}$',fontdict={'fontsize':25})
    ax3.set_ylabel(r'$d\sigma/\cos\theta_\gamma\cdot(fb)^{-1}$',fontdict={'fontsize':25})
    ax4.set_ylabel(r'$d\sigma/m_{missing}\cdot(fb/GeV)^{-1}$',fontdict={'fontsize':25})

    lineexample = []
    for i in range(len(datas)):
        lineexample.append(lines[i][0])
    ax1.legend(tuple(lineexample),(r'$g^V_f = 10^{-2}$',r'$SM BG$',r'$g^V_f = 10^{-3}$',r'$m_\chi = 121 GeV$'
                                          ,r'$m_\chi = 161 GeV$','irreducible background'),loc='lower left',prop={'family':'serif','size':19},framealpha=0.5)

    for tick in ax1.xaxis.get_major_ticks():
        tick.label.set_fontsize(24)
    for tick in ax2.xaxis.get_major_ticks():
        tick.label.set_fontsize(24)
    for tick in ax3.xaxis.get_major_ticks():
        tick.label.set_fontsize(24)
    for tick in ax4.xaxis.get_major_ticks():
        tick.label.set_fontsize(24)
        # ax1.set_yticklabels([r'$10^{0}$',r'$10^{0.5}$',r'$10^{1}$',r'$10^{1.5}$',r'$10^{2}$',r'$10^{2.5}$'])
    for tick in ax1.yaxis.get_major_ticks():
        tick.label.set_fontsize(24)
    for tick in ax2.yaxis.get_major_ticks():
        tick.label.set_fontsize(24)
    for tick in ax3.yaxis.get_major_ticks():
        tick.label.set_fontsize(24)
    for tick in ax4.yaxis.get_major_ticks():
        tick.label.set_fontsize(24)


    for i in range(len(datas)):
        for j in range(4):
            lines[i][j].set_linestyle(datas[i].style)
    plt.show()



if __name__ == '__main__':
    # print(np.load('/store/disposed/muon2d.npy')[:20])
    # vmbg,vebg = np.load('/store/disposed/milliq/ilc/vmvmilcd.npy'),np.load('/store/disposed/milliq/ilc/veveilcd.npy')
    # vmbg[:,-1] = 0.02*vmbg[:,-1]
    # vebg[:,-1] = 0.01*vebg[:,-1]
    # bg = Data(data=np.vstack((vmbg,vebg)),colour='violet',style='dashed',width=3.5)
    # m1,m41,m81,m121,m161 = np.load('/store/disposed/milliq/ilc/mqilc132dot0d.npy'),np.load('/store/disposed/milliq/ilc/mqilc132dot10d.npy'),np.load(
    #     '/store/disposed/milliq/ilc/mqilc132dot20d.npy'),np.load('/store/disposed/milliq/ilc/mqilc132dot30d.npy'),np.load('/store/disposed/milliq/ilc/mqilc132dot40d.npy')
    # dm1,dm41,dm81,dm121,dm161 = Data(m1,colour='blue',style='solid',width=2),Data(m41,colour='red',style='solid',width=2),Data(m81,colour='Green',style='solid',width=2),Data(m121,width=2),Data(m161,width=2)
    #
    #
    # general_painter([dm1, dm41, dm81,dm121,dm161,bg],energy=250)
    # bg = Data(data=np.load('/store/disposed/dd.npy'),style='dashed',width=2.5,energy=240)
    # data2 = Data(data=np.load('/store/disposed/dfbg2d.npy'),style='solid',width=2.5,energy=240)
    data0 = Data(data=np.load('/store/disposed/muon2d.npy'),style='solid',width=2.5,energy=240)

    general_painter(datas=[data0],energy=240)