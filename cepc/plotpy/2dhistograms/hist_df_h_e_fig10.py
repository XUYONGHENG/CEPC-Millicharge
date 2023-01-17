import obwatch_general as obw
import numpy as np
import matplotlib.pyplot as plt



if __name__ == '__main__':
    fig,ax = plt.subplots(figsize=(10,7.5))

    data1 = np.load('/home/xyh/PycharmProjects/cepc/plotCSV/2dhistogram/df_h_e_m1_hist.npy')
    data50 = np.load('/home/xyh/PycharmProjects/cepc/plotCSV/2dhistogram/df_h_e_m50_hist.npy')
    data100 = np.load('/home/xyh/PycharmProjects/cepc/plotCSV/2dhistogram/df_h_e_m100_hist.npy')
    databg = np.load('/home/xyh/PycharmProjects/cepc/plotCSV/2dhistogram/df_h_e_smbg_hist.npy')

    line1, = ax.plot(data1[:,0],data1[:,1],color='purple',linewidth=3,linestyle='solid')
    line2, = ax.plot(data50[:,0],data50[:,1],color='blue',linewidth=3,linestyle='-.')
    line3, = ax.plot(data100[:,0],data100[:,1],color='red',linewidth=3,linestyle=':')
    linebg, = ax.plot(databg[:,0],databg[:,1],color='black',linewidth=3,linestyle='--')

    ax.text(15, 4e-2, r'$Z^\prime$ portal model', fontdict={'fontsize': 20}, fontfamily='serif')
    ax.text(16, 2e-2, r'$\sqrt{s}=240$ GeV', fontsize=20, fontfamily='serif')
    # ax.text(40,8e-5,'Higgs factory',fontsize=24)
    obw.decorate(ax, xlabel=r'$E_\gamma$ (GeV)', ylabel=r'$\frac{1}{\sigma}\frac{d\sigma}{dE_\gamma}$ (GeV$^{-1})$',
                 xlog=False, ylog=True)
    # obw.decorate(ax, xlabel=r'$E_\gamma$ (GeV)', ylabel=r'$Probability$', xlog=False, ylog=True)

    ax.set_ylim(1e-5, 3e-1)
    ax.spines['top'].set_linewidth(1.5)
    ax.spines['bottom'].set_linewidth(1.5)
    ax.spines['left'].set_linewidth(1.5)
    ax.spines['right'].set_linewidth(1.5)
    ax.xaxis.set_tick_params(width=1.5, which='minor')
    ax.xaxis.set_tick_params(width=1.5)
    ax.yaxis.set_tick_params(width=1.5, which='minor')
    ax.yaxis.set_tick_params(width=1.5)

    ax.text(27, 5e-4, r'$m_\chi = 100$ GeV', color='red', fontsize=20, rotation=270, fontfamily='serif')
    ax.text(80, 1e-1, r'$m_\chi = 50$ GeV', color='blue', fontsize=20, rotation=0, fontfamily='serif')
    ax.text(95, 6e-4, r'$m_\chi = 1$ GeV', color='purple', fontsize=20, rotation=-60, fontfamily='serif')
    ax.text(40, 5e-4, 'Irreducible BG', color='black', fontsize=20, rotation=-12.50, fontfamily='serif')

    plt.savefig('/home/xyh/texworkbench/cepc/paperdraft/figs/dfhhist_e_2.pdf', format='pdf')
    plt.show()