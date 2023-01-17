import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

def binhist(ax,ratio,flagc=False):
    im = ax.imshow(ratio)
    ax.set_xticks(np.linspace(0,30,5))
    ax.set_xticklabels(np.linspace(-1,1,5))
    ax.set_yticks(np.linspace(0,30,5))
    ax.set_yticklabels(np.linspace(30,120,5))

    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    cbar = ax.figure.colorbar(im, cax=cax)
    if flagc:
        cbar.ax.set_ylabel(r'-log($d\sigma_s/d\sigma_b)$', rotation=-90, va="bottom",fontsize=24,fontfamily='serif')


if __name__ == '__main__':
    fig,ax1 = plt.subplots(figsize=(9,6.75))

    # Change this to 10,100 for another 2 subfigures.

    ratio = np.load('/home/xyh/PycharmProjects/cepc/plotCSV/optimisation/binration_1.npy')
    binhist(ax1, ratio, True)
    ax1.set_xlabel(r'cos$\theta_\gamma$', fontsize=24, fontfamily='serif')
    ax1.set_ylabel(r'$E_\gamma$ (GeV)', fontsize=24, fontfamily='serif')

    for label in ax1.xaxis.get_majorticklabels():
        label.set_fontsize(16)
        label.set_fontname('serif')
    for label in ax1.xaxis.get_minorticklabels():
        label.set_fontsize(16)
        label.set_fontname('serif')
    for label in ax1.yaxis.get_majorticklabels():
        label.set_fontsize(16)
        label.set_fontname('serif')
    for label in ax1.yaxis.get_minorticklabels():
        label.set_fontsize(16)
        label.set_fontname('serif')

    plt.savefig('/home/xyh/texworkbench/cepc/paperdraft/figs/binratio1.pdf', format='pdf')

    plt.show()