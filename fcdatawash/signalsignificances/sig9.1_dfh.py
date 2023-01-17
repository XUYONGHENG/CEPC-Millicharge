import numpy as np
import pandas as pd
import cut as cut



# print(bg.shape)
# print(np.sum(bg[:,-1]))
def signal_significance_cepcdfh_invisible(s,bg,mass,cut=cut.cut_cepc_darkphoton_h,dataamount=5e6,splusb=False):
    print(np.sum(s[:,-1]))
    ssection = 0
    # count = 0


    for i in range(s.shape[0]):
        if cut(s[i],mass):
            ssection += s[i,-1]
            # count += 1
    print(ssection)
    print('s')


    bgsection = 0
    for i in range(bg.shape[0]):
        if cut(bg[i],mass):
            bgsection += bg[i,-1]
    print(bgsection)
    print('b')

    if not splusb:
        # print(ssection*dataamount/np.sqrt(bgsection*dataamount))
        return (np.sqrt(2/(ssection*dataamount/np.sqrt(bgsection*dataamount)))*0.01),ssection,bgsection
    elif splusb:
        # print(ssection*dataamount/np.sqrt((bgsection+ssection)*dataamount))
        return (np.sqrt(2/(ssection*dataamount/np.sqrt((bgsection+ssection)*dataamount)))*0.01),ssection,bgsection


if __name__ == '__main__':
    # Loading Backgrounds. Only neutrino backgrounds are loaded since other backgrounds concerning
    # visible particles will be safely wiped out by our advanced cut.

    b, a = np.load('/store/disposed/vmvmcepc3d.npy'), np.load('/store/disposed/vevecepc3d.npy')
    print(np.sum(a[:,-1]))
    b[:, -1] = 2 * b[:, -1]
    bg = np.vstack((a, b))
    print(np.sum(bg[:,-1]))

    # bg = np.load('/store/disposed/1211va/bgmg5d.npy')

    # print(masses)
    dots = np.zeros(shape=(51, 4))



  # Original 1-100
    masses = 10**np.linspace(0,2,51)

    for i in range(1,52):


#         Standard mq data. Generated w/ larger cut Formcalc.
#         data = np.load('/store/disposed/milliq/cepcz/mqcepcz132dot%dd.npy'%i)
        data = np.load('/store/disposed/cepcdfh%d_run2d.npy'%i)
        print(np.sum(data[:,-1]))
        data[:,-1] = 0.93*data[:,-1]
        print(np.sum(data[:,-1]))
        dots[i-1,1:] = signal_significance_cepcdfh_invisible(s=data,
                            bg=bg,mass=masses[i-1],cut=cut.cut_cepc_darkphoton_h,dataamount=5e6,splusb=False)

        dots[i-1,0] = masses[i-1]
        print(dots[i-1])
    np.save('../plotformalCSV/cepcdarkphoton/sbdotscepcdfh_run2.npy',dots)

#

# Add-on 40-100
#     for i in range(1,22):
#         masses = np.linspace(40,100,21)
#
#         data = np.load('/store/disposed/darkphoton/cepcdfh%d_addd.npy'%i)
#         data[:,-1] = 0.93*data[:,-1]
#         print(np.sum(data[:,-1]))
#         dots[i-1,1:] = signal_significance_cepcdfh_invisible(s=data,
#                             bg=bg,mass=masses[i-1],cut=cut.cut_cepc_darkphoton_h,dataamount=5e6,splusb=False)
#
#         dots[i-1,0] = masses[i-1]
#         print(dots[i-1])
#     np.save('../plotformalCSV/cepcdarkphoton/sbdotscepcdfh_add.npy',dots)
    # tmp = []
    # for i in range(dots.shape[0])
    # with open('../plotformalCSV/cepcdarkphoton/sbdotscepcdfh.ltxtb','w') as file_object:
    #     file_object.writelines()