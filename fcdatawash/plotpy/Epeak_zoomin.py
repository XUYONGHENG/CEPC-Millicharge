def selection_0():

    # Library import
    import numpy as np
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec


    d50,d50s = np.load('/store/disposed/50GeV_histo_nosmeard.npy'),np.load('/store/disposed/50GeV_histo_smeard.npy')
    d75,d75s = np.load('/store/disposed/75GeV_histo_nosmeard.npy'),np.load('/store/disposed/75GeV_histo_smeard.npy')
    d749,d749s = np.load('/store/disposed/74.9GeV_histo_nosmeard.npy'),np.load('/store/disposed/74.9GeV_histo_smeard.npy')


    d50h,edges = np.histogram(d50,bins=100,range=(71,75),normed=False)
    d50sh, edges= np.histogram(d50s,bins=100,range=(71,75),normed=False)
    d75h, edges= np.histogram(d75,bins=100,range=(71,75),normed=False)
    d75sh, edges= np.histogram(d75s,bins=100,range=(71,75),normed=False)
    d749h, edges= np.histogram(d749,bins=100,range=(71,75),normed=False)
    d749sh, edges= np.histogram(d749s,bins=100,range=(71,75),normed=False)

    print(edges.shape)
    datapoints = 0.02+np.linspace(71,75,100,endpoint=False)
    print(datapoints)

    print(d75h)
    # input('halt')
    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = np.__version__

    # Histo binning
    xBinning = np.linspace(140.0,160.0,101,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = np.array([140.1,140.3,140.5,140.7,140.9,141.1,141.3,141.5,141.7,141.9,142.1,142.3,142.5,142.7,142.9,143.1,143.3,143.5,143.7,143.9,144.1,144.3,144.5,144.7,144.9,145.1,145.3,145.5,145.7,145.9,146.1,146.3,146.5,146.7,146.9,147.1,147.3,147.5,147.7,147.9,148.1,148.3,148.5,148.7,148.9,149.1,149.3,149.5,149.7,149.9,150.1,150.3,150.5,150.7,150.9,151.1,151.3,151.5,151.7,151.9,152.1,152.3,152.5,152.7,152.9,153.1,153.3,153.5,153.7,153.9,154.1,154.3,154.5,154.7,154.9,155.1,155.3,155.5,155.7,155.9,156.1,156.3,156.5,156.7,156.9,157.1,157.3,157.5,157.7,157.9,158.1,158.3,158.5,158.7,158.9,159.1,159.3,159.5,159.7,159.9])

    # Creating weights for histo: y1_M_0
    y2_M_0_weights = np.array([3.593396e-06,2.940052e-06,2.316404e-06,3.237026e-06,2.494589e-06,3.444909e-06,3.118237e-06,2.850959e-06,3.147934e-06,3.534001e-06,4.127951e-06,3.534001e-06,3.801279e-06,4.335834e-06,4.217044e-06,4.217044e-06,3.860674e-06,4.424926e-06,4.424926e-06,4.484321e-06,4.929783e-06,4.929783e-06,5.969196e-06,5.761313e-06,5.642523e-06,6.592843e-06,6.206776e-06,6.652238e-06,6.86012e-06,8.731062e-06,7.632255e-06,8.52318e-06,9.503197e-06,9.978357e-06,1.173051e-05,1.282932e-05,1.464086e-05,1.594755e-05,2.025369e-05,2.322344e-05,2.669804e-05,3.572608e-05,4.629839e-05,5.856345e-05,7.011578e-05,8.745911e-05,0.0001060497,0.000126541,0.0002135844,0.0005423653,0.0005034913,0.000153833,8.885489e-05,7.477828e-05,5.92168e-05,4.683294e-05,3.605275e-05,2.408466e-05,1.603664e-05,1.119595e-05,7.988625e-06,4.603111e-06,3.058842e-06,1.781849e-06,6.830423e-07,6.533448e-07,3.563699e-07,2.672774e-07,1.1879e-07,0.0,0.0,5.939498e-08,0.0,1.1879e-07,0.0,2.969749e-08,2.969749e-08,2.969749e-08,2.969749e-08,0.0,2.969749e-08,0.0,2.969749e-08,5.939498e-08,2.969749e-08,0.0,2.969749e-08,5.939498e-08,0.0,2.969749e-08,2.969749e-08,0.0,2.969749e-08,0.0,0.0,2.969749e-08,5.939498e-08,0.0,0.0,0.0])

    a = (np.sum(y2_M_0_weights))
    y2_M_0_weights = 5 * y2_M_0_weights/a*1e5

    # Histo binning
    xBinning2 = np.linspace(140.0,160.0,101,endpoint=True)
    #
    #     # Creating data sequence: middle of each bin
    xData2 = np.array([140.1,140.3,140.5,140.7,140.9,141.1,141.3,141.5,141.7,141.9,142.1,142.3,142.5,142.7,142.9,143.1,143.3,143.5,143.7,143.9,144.1,144.3,144.5,144.7,144.9,145.1,145.3,145.5,145.7,145.9,146.1,146.3,146.5,146.7,146.9,147.1,147.3,147.5,147.7,147.9,148.1,148.3,148.5,148.7,148.9,149.1,149.3,149.5,149.7,149.9,150.1,150.3,150.5,150.7,150.9,151.1,151.3,151.5,151.7,151.9,152.1,152.3,152.5,152.7,152.9,153.1,153.3,153.5,153.7,153.9,154.1,154.3,154.5,154.7,154.9,155.1,155.3,155.5,155.7,155.9,156.1,156.3,156.5,156.7,156.9,157.1,157.3,157.5,157.7,157.9,158.1,158.3,158.5,158.7,158.9,159.1,159.3,159.5,159.7,159.9])
    #
    print(xBinning.shape,xData.shape,y2_M_0_weights.shape)
    #     # Creating weights for histo: y3_M_0
    y2_M_0_weights2 = np.array([1.141069e-08,1.141069e-08,1.315827e-08,1.336387e-08,1.398066e-08,1.336387e-08,1.531705e-08,1.459746e-08,1.829822e-08,1.541985e-08,1.634504e-08,1.840102e-08,1.675624e-08,1.901781e-08,2.127939e-08,2.03542e-08,2.189619e-08,2.446616e-08,2.477456e-08,2.446616e-08,2.662494e-08,2.559695e-08,2.621374e-08,3.07369e-08,3.690484e-08,3.279288e-08,3.711044e-08,3.762443e-08,4.194199e-08,4.173639e-08,4.882952e-08,5.057711e-08,6.003462e-08,5.571706e-08,6.589416e-08,7.442647e-08,8.25476e-08,8.635116e-08,9.313589e-08,1.054718e-07,1.23256e-07,1.380591e-07,1.476194e-07,1.65198e-07,1.725995e-07,1.912061e-07,2.017944e-07,2.151583e-07,2.319145e-07,2.236906e-07,2.280082e-07,2.202983e-07,2.110463e-07,1.967573e-07,1.885334e-07,1.620112e-07,1.41657e-07,1.328163e-07,1.185272e-07,1.045466e-07,9.539747e-08,8.830434e-08,7.22677e-08,7.278169e-08,5.941782e-08,5.499746e-08,5.211909e-08,4.512876e-08,4.605395e-08,3.423207e-08,3.947482e-08,3.06341e-08,2.970891e-08,3.022291e-08,2.631654e-08,2.662494e-08,2.467176e-08,2.333537e-08,1.809262e-08,1.840102e-08,1.706463e-08,1.912061e-08,1.634504e-08,1.870942e-08,1.336387e-08,1.531705e-08,1.264428e-08,1.243868e-08,1.326107e-08,1.079389e-08,1.284987e-08,1.05883e-08,1.01771e-08,9.457508e-09,9.868704e-09,8.840714e-09,8.018322e-09,9.354709e-09,7.298729e-09,7.401528e-09])
    print(y2_M_0_weights2)
    a2 = np.sum(y2_M_0_weights2)
    y2_M_0_weights2 = 5 * y2_M_0_weights2/a2*1e5

    print(np.sum(y2_M_0_weights2))

    print(a2)
    # input('halt')
    # Creating a new Canvas
    fig   = plt.figure(figsize=(12,9),dpi=80)
    frame = gridspec.GridSpec(1,1)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    print(xBinning.shape,xData.shape,y2_M_0_weights.shape)
    print(edges.shape,datapoints.shape,d50h.shape)
    a = pad.hist(x=datapoints, bins=edges, weights=d50sh,\
             label="$defaultset$", histtype="step", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=3, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")

    b = pad.hist(x=datapoints, bins=edges, weights=d75sh,\
             label="$defaultset$", histtype="step", rwidth=1.0,\
             color="red", edgecolor="red", linewidth=3, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")


    c = pad.hist(x=datapoints, bins=edges, weights=d749sh,\
             label="$defaultset$", histtype="step", rwidth=1.0,\
             color="red", edgecolor="black", linewidth=3, linestyle="solid",\
             bottom=None, cumulative=False, normed=False, align="mid", orientation="vertical")



    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"$E_\gamma$ (GeV) ",\
               fontsize=24,color="black")
    plt.ylabel(r'Events/0.2 GeV (Gev)$^{-1} $',\
               fontsize=24,color="black")
    # plt.legend((a,b,c),('a','b','c'))
    pad.text(72.3,1.5e2,r'Smeared Data',fontsize=29)


    # Boundary of y-axis
    ymax=(y2_M_0_weights).max()*1.1
    #ymin=0 # linear scale
    ymin=min([x for x in (y2_M_0_weights) if x])/100. # log scale
    plt.gca().set_ylim(ymin,ymax)

    # Log/Linear scale for X-axis
    plt.gca().set_xscale("linear")
    #plt.gca().set_xscale("log",nonposx="clip")

    # Log/Linear scale for Y-axis
    #plt.gca().set_yscale("linear")
    plt.gca().set_yscale("log",nonposy="clip")


    xminorLocator = plt.MultipleLocator(0.5)
    pad.xaxis.set_minor_locator(xminorLocator)

    xmajorLocator = plt.MultipleLocator(2.5)
    pad.xaxis.set_major_locator(xmajorLocator)


    # pad.set_xlim(140,160)
    pad.set_ylim(1e2,1e4)
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
    for tick in pad.xaxis.get_minor_ticks():
        tick.label.set_fontsize(18)
    for tick in pad.yaxis.get_major_ticks():
        tick.label.set_fontsize(18)
    for tick in pad.yaxis.get_minor_ticks():
        tick.label.set_fontsize(18)
    # Saving the image
    # plt.savefig('../../HTML/MadAnalysis5job_0/selection_0.png')
    # plt.savefig('../../PDF/MadAnalysis5job_0/selection_0.png')
    plt.savefig('../figformal/peakzoomin_smear.png',format = 'png')
    # plt.savefig('../figformal/peakzoomin_smear.eps',format = 'eps')
    plt.show()

# Running!
if __name__ == '__main__':
    selection_0()
