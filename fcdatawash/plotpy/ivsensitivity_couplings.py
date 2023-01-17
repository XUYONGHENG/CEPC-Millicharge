import os as os
import numpy as np
# import pandas as pd
import re as re

# let mg5 run given times repeatedly with fixed parameter.
# external script needed.
def modify_dm_mass(mx):
    lines = []
    with open('Cards/param_card.dat') as file_object:
        for line in file_object.readlines():
            # print(1)
            if '# mxd' in line or '# MXd' in line:
                print('haha!')
                print(mx)
                print('9000007 %f\n'%mx)
                linex = ('      9000007 %fe+0 # mxd\n'%mx)
            else:
                linex = line
            lines.append(linex)
    # print(lines)
    with open('tmpmodel','w') as file_object:
        file_object.writelines(lines)
    os.system('mv tmpmodel Cards/param_card.dat')

        # print('i\n')
def modify_gvx(gvx):
    lines = []
    with open('Cards/param_card.dat') as file_object:
        for line in file_object.readlines():
            # print(1)
            if '# gVXd' in line:
                print('haha!')
                print(gvx)
                print(line)
                linex = ('   2 %fe+00 # gVXd\n'%gvx)
                print(linex)
            else:
                linex = line
            lines.append(linex)
    # print(lines)
    with open('tmpmodel','w') as file_object:
        file_object.writelines(lines)
    os.system('mv tmpmodel Cards/param_card.dat')



def modify_beam_energy(energy):
    energy = energy/2
    lines = []
    with open('Cards/run_card.dat') as file_object:
        for line in file_object.readlines():
            # print(1)
            if '= ebeam1'  in line:
                print('haha!')
                linex = ('     %f     = ebeam1  ! beam 1 total energy in GeV\n'%energy)
            elif '= ebeam2'  in line:
                print('haha!')
                linex = ('     %f     = ebeam2  ! beam 2 total energy in GeV\n'%energy)
            else:
                linex = line
            lines.append(linex)
    # print(lines)
    with open('tmpmodel','w') as file_object:
        file_object.writelines(lines)
    os.system('mv tmpmodel Cards/run_card.dat')



def gf(mz,mf,nc,c):
    c = 1
    # print(mz,mf,nc,c)
    return nc * c**2 * np.sqrt(0.25*mz**2-mf**2) / (6*np.pi)


def decay_width_sm(mzp,epsilon):
    if mzp*0.5 < 1.28:
        w0 = gf(mzp,0,3,float(2)/3)+2*gf(mzp,0,3,float(-1)/3)+2*gf(mzp,0,1,-1)
    elif 1.28 <= (mzp*0.5) <1.78:
        w0 =  gf(mzp,0,3,float(2)/3)+2*gf(mzp,0,3,float(-1)/3)+2*gf(mzp,0,1,-1) + gf(mzp,1.28,3,float(2)/3)
    elif 1.78<= (mzp*0.5) < 4.18:
        w0 = 2*gf(mzp,0,3,float(2)/3)+2*gf(mzp,0,3,float(-1)/3)+2*gf(mzp,0,1,-1) + gf(mzp,1.28,3,float(2)/3) + gf(mzp,1.78,1,-1)
    else:
        w0 =  gf(mzp,0,3,float(2)/3)+2*gf(mzp,0,3,float(-1)/3)+2*gf(mzp,0,1,-1) + gf(mzp,1.28,3,float(2)/3) + gf(mzp,1.78,1,-1) + gf(mzp,4.18,3,float(-1)/3)

    return epsilon**2*w0



def decay_width_dm(mzp,mx,gvx):
    if mx > (mzp*0.5):
        return 0
    else:
        return gvx**2*gf(mzp,mx,1,1)


def decay_width(mx,gvx):
    if mx >= 75:
        # gf = np.sqrt(0.25*150**2-mass**2)*(150**2+2*mass**2)/(6*np.pi*150**2)
        return decay_width_sm(150,0.01)
    else:
        # print(decay_width_dm(150,mx,gvx),decay_width_sm(150,0.01))

        return decay_width_dm(150,mx,gvx) + decay_width_sm(150,0.01)



def modify_decay_width_zp(width):
    lines = []
    with open('Cards/param_card.dat') as file_object:
        for line in file_object.readlines():
            # print(1)
            if '# WY1' in line or '# wy1' in line:
                print('haha!')
                print(width)
                linex = ('DECAY 9000008 %fe+00 # WY1\n'%width)
            else:
                linex = line
            lines.append(linex)
    # print(lines)
    with open('tmpmodel','w') as file_object:
        file_object.writelines(lines)
    os.system('mv tmpmodel Cards/param_card.dat')


def width_quick(gvx,gvf):
    return (18*gvf**2*150+gvx**2*np.sqrt(150**2-4*50**2))/(12*np.pi)

if __name__ == '__main__':
    os.system('rm -rf Events/run*')
    modify_beam_energy(240)
    modify_dm_mass(mx=50)
    couplings = 10**np.linspace(-3,0,31)
    # print(couplings)
    # input('halt')
    for i in range(1,32):
        width,width_1 = decay_width(mx=50,gvx=couplings[i-1]),width_quick(gvx=couplings[i-1],gvf=1e-2)
        # if width-width_1 >= 1e-4:
        #     print('bing!')
        modify_gvx(gvx=couplings[i-1])
        input('halt')
        modify_decay_width_zp(width)
        os.system('~/MG5_aMC_v2_6_2/bin/mg5_aMC /home/xyh/PycharmProjects/fcdatawash/auto/mg5dfrun_general')
        if i <= 9 :
            os.system('mv Events/run_0%d/*.gz /store/darkphoton2/mz150_%d_run4.lhe.gz'%(i,i))
        else:
            os.system('mv Events/run_%d/*.gz /store/darkphoton2/mz150_%d_run4.lhe.gz'%(i,i))
    #
    os.system('rm -rf Events/run*')
