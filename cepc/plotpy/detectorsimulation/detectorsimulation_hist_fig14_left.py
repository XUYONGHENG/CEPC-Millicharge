def selection_1():

    # Library import
    import numpy as np
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec
    from matplotlib.ticker import MultipleLocator, FormatStrFormatter

    # Library version
    # matplotlib_version = matplotlib.__version__
    # numpy_version      = numpy.__version__

    # Histo binning
    xBinning = np.linspace(60.0,85.0,101,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = np.array([60.125,60.375,60.625,60.875,61.125,61.375,61.625,61.875,62.125,62.375,62.625,62.875,63.125,63.375,63.625,63.875,64.125,64.375,64.625,64.875,65.125,65.375,65.625,65.875,66.125,66.375,66.625,66.875,67.125,67.375,67.625,67.875,68.125,68.375,68.625,68.875,69.125,69.375,69.625,69.875,70.125,70.375,70.625,70.875,71.125,71.375,71.625,71.875,72.125,72.375,72.625,72.875,73.125,73.375,73.625,73.875,74.125,74.375,74.625,74.875,75.125,75.375,75.625,75.875,76.125,76.375,76.625,76.875,77.125,77.375,77.625,77.875,78.125,78.375,78.625,78.875,79.125,79.375,79.625,79.875,80.125,80.375,80.625,80.875,81.125,81.375,81.625,81.875,82.125,82.375,82.625,82.875,83.125,83.375,83.625,83.875,84.125,84.375,84.625,84.875])

    # Creating weights for histo: y1_E_0
    y1_E_0_weights = 4*np.array([1.484875e-07,3.563699e-07,1.484875e-07,2.375799e-07,2.672774e-07,2.078824e-07,3.563699e-07,3.563699e-07,7.127398e-07,1.484875e-07,3.563699e-07,2.078824e-07,2.672774e-07,2.078824e-07,4.157649e-07,2.375799e-07,1.781849e-07,1.781849e-07,2.969749e-07,2.375799e-07,2.672774e-07,2.078824e-07,3.266724e-07,2.375799e-07,2.078824e-07,1.484875e-07,2.078824e-07,1.1879e-07,2.672774e-07,3.266724e-07,2.969749e-07,1.781849e-07,3.266724e-07,2.375799e-07,3.266724e-07,1.1879e-07,4.157649e-07,2.672774e-07,3.860674e-07,9.503197e-07,1.930337e-06,3.207329e-06,7.068003e-06,1.568028e-05,2.84502e-05,5.119847e-05,8.321237e-05,0.0001279071,0.0001774425,0.0002310168,0.0002751473,0.0003106061,0.000318565,0.0003073393,0.0002706035,0.0002252852,0.0001803529,0.0001258877,8.154931e-05,5.342579e-05,2.984598e-05,1.645241e-05,8.64197e-06,4.127951e-06,2.197614e-06,6.830423e-07,5.048573e-07,2.375799e-07,2.672774e-07,2.078824e-07,8.909247e-08,1.484875e-07,1.484875e-07,1.781849e-07,5.939498e-08,1.1879e-07,1.781849e-07,2.078824e-07,8.909247e-08,1.1879e-07,8.909247e-08,3.266724e-07,2.078824e-07,2.078824e-07,1.781849e-07,1.781849e-07,8.909247e-08,2.078824e-07,8.909247e-08,8.909247e-08,2.078824e-07,1.1879e-07,1.484875e-07,2.078824e-07,2.078824e-07,1.1879e-07,2.078824e-07,1.1879e-07,2.078824e-07,1.781849e-07])

    a = np.sum(y1_E_0_weights)
    # print(a)
    y1_E_0_weights = y1_E_0_weights*(1e5/0.00295)


    # Histo binning
    xBinning2 = np.linspace(60.0,85.0,101,endpoint=True)

    # Creating data sequence: middle of each bin
    xData2 = np.array([60.125,60.375,60.625,60.875,61.125,61.375,61.625,61.875,62.125,62.375,62.625,62.875,63.125,63.375,63.625,63.875,64.125,64.375,64.625,64.875,65.125,65.375,65.625,65.875,66.125,66.375,66.625,66.875,67.125,67.375,67.625,67.875,68.125,68.375,68.625,68.875,69.125,69.375,69.625,69.875,70.125,70.375,70.625,70.875,71.125,71.375,71.625,71.875,72.125,72.375,72.625,72.875,73.125,73.375,73.625,73.875,74.125,74.375,74.625,74.875,75.125,75.375,75.625,75.875,76.125,76.375,76.625,76.875,77.125,77.375,77.625,77.875,78.125,78.375,78.625,78.875,79.125,79.375,79.625,79.875,80.125,80.375,80.625,80.875,81.125,81.375,81.625,81.875,82.125,82.375,82.625,82.875,83.125,83.375,83.625,83.875,84.125,84.375,84.625,84.875])

    # Creating weights for histo: y1_E_0
    y1_E_0_weights2 = 4 * np.array([6.16794e-09,7.812724e-09,8.22392e-09,8.121121e-09,9.663106e-09,8.429518e-09,8.326719e-09,9.765905e-09,9.046312e-09,1.120509e-08,1.06911e-08,1.110229e-08,9.560307e-09,9.765905e-09,1.03827e-08,1.120509e-08,1.161629e-08,1.377507e-08,1.387786e-08,1.192468e-08,1.295267e-08,1.593384e-08,1.727023e-08,1.994301e-08,1.665344e-08,1.829822e-08,2.01486e-08,1.994301e-08,2.220458e-08,2.210178e-08,2.600815e-08,3.05313e-08,3.09425e-08,3.526006e-08,3.669924e-08,4.235319e-08,4.502596e-08,5.684785e-08,6.466057e-08,7.319289e-08,8.090281e-08,9.765905e-08,1.214056e-07,1.377507e-07,1.68796e-07,2.069344e-07,2.472316e-07,2.914352e-07,3.380031e-07,3.549649e-07,3.997853e-07,4.203451e-07,4.225039e-07,4.083176e-07,3.900194e-07,3.607217e-07,3.076774e-07,2.64913e-07,2.238962e-07,1.949069e-07,1.485446e-07,1.233588e-07,1.035186e-07,8.24448e-08,6.712775e-08,5.571706e-08,4.841833e-08,4.368957e-08,3.176489e-08,3.248448e-08,2.580255e-08,2.323257e-08,2.107379e-08,1.788703e-08,1.696183e-08,1.583105e-08,1.326107e-08,1.192468e-08,1.254148e-08,1.00743e-08,8.22392e-09,8.943513e-09,7.812724e-09,8.326719e-09,7.915523e-09,7.093131e-09,6.373538e-09,5.653945e-09,6.16794e-09,4.831553e-09,5.551146e-09,4.009161e-09,3.392367e-09,5.756744e-09,3.597965e-09,3.495166e-09,4.214759e-09,4.214759e-09,4.728754e-09,4.009161e-09])

    a2 = np.sum(y1_E_0_weights2)
    print(a2)
    y1_E_0_weights2 = y1_E_0_weights2*(1e5/7.28e-6)

    print(np.sum(y1_E_0_weights),np.sum(y1_E_0_weights2))


    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,9),dpi=80)
    frame = gridspec.GridSpec(1,1)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y1_E_0_weights,\
             label="$defaultset$", histtype="step", rwidth=1.0,\
             color="red", edgecolor='#5954d8', linewidth=3, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    pad.hist(x=xData2, bins=xBinning2, weights=y1_E_0_weights2,\
             label="$defaultset$", histtype="step", rwidth=1.0,\
             color="#5954d8", edgecolor='red', linewidth=3, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"$E_\gamma$ (GeV) ",\
               fontsize=24,color="black",fontfamily='serif')
    plt.ylabel(r'Events/0.25GeV',\
               fontsize=24,color="black",fontfamily='serif')

    pad.text(61,4.5*1e4,r'$10^5$ MC Events                 $\sqrt{s} = 240$ GeV',fontsize=29,fontfamily='serif')
    # pad.text(61,2e4,r'$\Gamma_{Z^\prime}=0.007$ GeV,$\sigma E=\sqrt{(0.004E)^2+E*0.101^2}$',fontsize=26)
    pad.text(70,4*9e0,r'$\Gamma_{Z^\prime}=7.5$ MeV', fontsize=26,color='#5954d8',fontfamily='serif')
    pad.text(70,10e0,r'$g^V_\chi$ = 0.01', fontsize=26,color='#5954d8',fontfamily='serif')
    pad.text(77.5,4*5e2,r'$\Gamma_{Z^\prime}=2.97$ GeV', fontsize=26,color='red',fontfamily='serif')
    pad.text(78,8e3,r'$g^V_\chi$ = 1', fontsize=26,color='red',fontfamily='serif')


    # Boundary of y-axis

    ymax=(y1_E_0_weights).max()*1.1
    #ymin=0 # linear scale
    ymin=min([x for x in (y1_E_0_weights) if x])/100. # log scale
    plt.gca().set_ylim(ymin,ymax)

    # Log/Linear scale for X-axis
    plt.gca().set_xscale("linear")
    #plt.gca().set_xscale("log",nonposx="clip")



    # Log/Linear scale for Y-axis
    #plt.gca().set_yscale("linear")
    plt.gca().set_yscale("log",nonposy="clip")
    xminorLocator = plt.MultipleLocator(0.5)
    pad.xaxis.set_minor_locator(xminorLocator)

    pad.set_xlim(60,85)
    pad.set_ylim(4e0,4e5)
    pad.spines['top'].set_linewidth(1.5)
    pad.spines['bottom'].set_linewidth(1.5)
    pad.spines['left'].set_linewidth(1.5)
    pad.spines['right'].set_linewidth(1.5)
    pad.xaxis.set_tick_params(width=1.5, which='minor')
    pad.xaxis.set_tick_params(width=1.5)
    pad.yaxis.set_tick_params(width=1.5, which='minor')
    pad.yaxis.set_tick_params(width=1.5)

    # ax.set_xlabel(xlabel, fontsize=24)
    # ax.set_ylabel(ylabel, fontsize=24)

    pad.tick_params(which='major', length=17, direction='in', top=True, right=True)
    pad.tick_params(which='minor', length=10, direction='in', top=True, right=True)

    for tick in pad.xaxis.get_major_ticks():
        tick.label.set_fontsize(18)
        tick.label.set_fontname('serif')

    for tick in pad.xaxis.get_minor_ticks():
        tick.label.set_fontsize(18)
        tick.label.set_fontname('serif')

    for tick in pad.yaxis.get_major_ticks():
        tick.label.set_fontsize(18)
        tick.label.set_fontname('serif')

    for tick in pad.yaxis.get_minor_ticks():
        tick.label.set_fontsize(18)
        tick.label.set_fontname('serif')
    # Saving the image

    # Saving the image
    # plt.savefig('/home/xyh/texworkbench/cepc/paperdraft/figs/delphes_histo_egamma.pdf',format = 'pdf')

    plt.show()
    # plt.savefig('../../PDF/MadAnalysis5job_0/selection_1.png')
    # plt.savefig('../../DVI/MadAnalysis5job_0/selection_1.eps')

# Running!
if __name__ == '__main__':
    selection_1()
