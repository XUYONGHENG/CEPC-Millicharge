import obwatch_general as obw
import numpy as np
import matplotlib.pyplot as plt



if __name__ == '__main__':
    fig,ax = plt.subplots(figsize=(10,7.5))

    data1 = np.load('/home/xyh/PycharmProjects/cepc/plotCSV/2dhistogram/mq_w_e_m1_hist.npy')
    data50 = np.load('/home/xyh/PycharmProjects/cepc/plotCSV/2dhistogram/mq_w_e_m50_hist.npy')
    data100 = np.load('/home/xyh/PycharmProjects/cepc/plotCSV/2dhistogram/mq_w_e_m100_hist.npy')
    databg = np.load('/home/xyh/PycharmProjects/cepc/plotCSV/2dhistogram/mq_w_e_smbg_hist.npy')

    line1, = ax.plot(data1[:,0],data1[:,1],color='purple',linewidth=3,linestyle='solid')
    line2, = ax.plot(data50[:,0],data50[:,1],color='blue',linewidth=3,linestyle='-.')
    line3, = ax.plot(data100[:,0],data100[:,1],color='red',linewidth=3,linestyle=':')
    linebg, = ax.plot(databg[:,0],databg[:,1],color='black',linewidth=3,linestyle='--')

    obw.decorate(ax, xlabel=r'$E_\gamma$ (GeV)', ylabel=r'$\frac{1}{\sigma}\frac{d\sigma}{dE_\gamma}$ (GeV$^{-1})$',
                 xlog=False, ylog=True)

    ax.text(15,0.035,r'$\sqrt{s}=160$ GeV',fontsize=20,fontfamily='serif')
    ax.text(15,0.07,'Millicharge',fontsize=20,fontfamily='serif')


    ax.text(67,0.045,r'$m_\chi = 1$ GeV',color='purple',fontsize=20,rotation=60,fontfamily='serif')
    ax.text(23,0.010,r'$m_\chi = 25$ GeV',color='blue',fontsize=20,rotation=-12,fontfamily='serif')
    ax.text(40,0.0015,r'$m_\chi = 50$ GeV',color='red',fontsize=20,rotation=-80,fontfamily='serif')
    ax.text(53,0.002,'Irreducible BG',color='black',fontsize=20,rotation=-70,fontfamily='serif')

    ax.set_ylim(1e-4,2e-1)

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
