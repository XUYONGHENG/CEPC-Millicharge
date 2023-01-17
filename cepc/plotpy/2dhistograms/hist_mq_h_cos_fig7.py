import obwatch_general as obw
import numpy as np
import matplotlib.pyplot as plt



if __name__ == '__main__':
    fig,ax = plt.subplots(figsize=(10,7.5))

    data1 = np.load('/home/xyh/PycharmProjects/cepc/plotCSV/2dhistogram/mq_h_cos_m1_hist.npy')
    data50 = np.load('/home/xyh/PycharmProjects/cepc/plotCSV/2dhistogram/mq_h_cos_m50_hist.npy')
    data100 = np.load('/home/xyh/PycharmProjects/cepc/plotCSV/2dhistogram/mq_h_cos_m100_hist.npy')
    databg = np.load('/home/xyh/PycharmProjects/cepc/plotCSV/2dhistogram/mq_h_cos_smbg_hist.npy')

    line1, = ax.plot(data1[:,0],data1[:,1],color='purple',linewidth=3,linestyle='solid')
    line2, = ax.plot(data50[:,0],data50[:,1],color='blue',linewidth=3,linestyle='-.')
    line3, = ax.plot(data100[:,0],data100[:,1],color='red',linewidth=3,linestyle=':')
    linebg, = ax.plot(databg[:,0],databg[:,1],color='black',linewidth=3,linestyle='--')

    obw.decorate(ax, xlabel=r'$\cos\theta_\gamma$',\
                 ylabel=r'$\frac{1}{\sigma}\frac{d\sigma}{d\cos\theta_\gamma}$', xlog=False, ylog=True)

    ax.legend((line1,line2,line3,linebg),(r'$m_\chi = 1$ GeV',r'$m_\chi = 50$ GeV',r'$m_\chi = 100$ GeV','Irreducible BG'),
              prop={'family': 'serif', 'size': 19},loc='upper center',framealpha=0)

    ax.text(-0.25,0.5,r'$\sqrt{s}=240$ GeV',fontsize=24,fontfamily='serif')
    ax.text(-0.19,0.3,r'Millicharge',fontsize=24,fontfamily='serif')

    ax.spines['top'].set_linewidth(1.5)
    ax.spines['bottom'].set_linewidth(1.5)
    ax.spines['left'].set_linewidth(1.5)
    ax.spines['right'].set_linewidth(1.5)
    ax.xaxis.set_tick_params(width=1.5, which='minor')
    ax.xaxis.set_tick_params(width=1.5)
    ax.yaxis.set_tick_params(width=1.5, which='minor')
    ax.yaxis.set_tick_params(width=1.5)

    plt.savefig('/home/xyh/texworkbench/cepc/paperdraft/figs/mqhist_e_2.pdf',format='pdf')
    plt.show()
