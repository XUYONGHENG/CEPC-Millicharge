import numpy as np
import pandas as pd
import re as re
import cut as cut
import os as os
import codecs as codecs
import re as re
import smearer as smear
from tools import *
from rematchpatterns import *

def raw_to_momentum(loaded):
    tmp = np.zeros(shape=(12,))
    tmp[0],tmp[4],tmp[8]=loaded[0],loaded[5],loaded[10]
    tmp[1],tmp[2],tmp[3]=loaded[4]*loaded[1],loaded[4]*loaded[2],loaded[4]*loaded[3]
    tmp[5], tmp[6], tmp[7] = loaded[9] * loaded[6], loaded[9] * loaded[7], loaded[9] * loaded[8]
    tmp[9], tmp[10], tmp[11] = loaded[14] * loaded[11], loaded[14] * loaded[12], loaded[14] * loaded[13]
    return tmp


def cos_theta_l1(p):
    return p[3]/p[0]

def cos_theta_l2(p):
    return p[7]/p[4]

def cos_theta_a(p):
    return p[11]/p[8]

def phi(p):
    return np.arctan(p[1]/p[2])

def eta(theta):
    return -np.log(np.tan(theta/2))

def lepton_invariant_mass(p):
    return (p[0]+p[4])**2-(p[1]+p[5])**2-(p[2]+p[6])**2-(p[3]-p[7])**2

def pt(p):
    return np.sqrt(p[1]**2+p[2]**2)


# print(cos_theta_a(data939[0]))
# data = [data939,data984]


# for j in range(2):
# ob = np.zeros(shape=(data.shape[0], 16))
def ob_gen(p):
    ob = np.zeros(shape=(16,))
    ob[0] = p[0]
    ob[1] = p[4]
    ob[2] = p[8]
    ob[3] = cos_theta_l1(p)
    ob[4] = cos_theta_l2(p)
    ob[5] = cos_theta_a(p)
    ob[6] = pt(p)
    ob[7] = pt(p[4:])
    ob[8] = pt(p[8:])
    ob[9] = eta(ob[3])
    ob[10] = eta(ob[4])
    ob[11] = eta(ob[5])
    ob[12] = lepton_invariant_mass(p)
    ob[13] = phi(p)
    ob[14] = phi(p[4:])
    ob[15] = phi(p[8:])
    return ob

def washer_with_weight(datafile,weightfile,savename,lines=0):
    disposed = []
    if not os.path.exists(savename+"tmp.csv"):
        if not lines:
            with open(datafile) as file_object:
                raw = file_object.readlines()
                for i in raw:
                    j = re.sub(r'\s+',', ',i.lstrip())
                    disposed.append(j[:-2]+"\n")

        else:
            index = 0
            with open(datafile) as file_object:
                raw = file_object.readlines()
                for i in raw:
                    j = re.sub(r'\s+',', ',i.lstrip())
                    disposed.append(j[:-2]+"\n")
                    index += 1
                    if index == lines:
                        break

        with open(savename + "tmp.csv", 'w') as f:
            f.writelines(disposed)

    print('bing!')
    a = np.array(pd.read_csv(savename + "tmp.csv"))
    w = np.array(pd.read_csv(weightfile))
    survivors = 0
    if a.shape[1] == 15:
        for i in range(w.shape[0]):
            if w[i] :
                survivors += 1
        print(survivors)
        input("x")
        c = 0
        disposed2 = np.zeros(shape=(survivors,29))
        for i in range(w.shape[0]):
            if w[i]:
                disposed2[c,:12] = raw_to_momentum(a[i])
                disposed2[c,-1] = w[i]
                disposed2[c,12:-1]= ob_gen(disposed2[c,:12])
                c += 1
        print(disposed2.shape)
        input("x")
        np.save("plotCSV/p"+savename+'w',disposed2)
    elif a.shape[1] == 4 or a.shape[1]== 6:
        for i in range(w.shape[0]):
            if w[i]:
                survivors += 1
        print(survivors)
        c = 0
        disposed2 = np.zeros(shape=(survivors,3))
        for i in range(w.shape[0]):
            if w[i]:
                disposed2[c,0],disposed2[c,1],disposed2[c,2] = a[i,3],a[i,2],w[i]
                c += 1
                # print(w[i])
        print(disposed2[:10,2])
        np.savetxt("plotCSV/p" + savename + ".csv", disposed2[:,:2], delimiter=', ')
        np.savetxt("plotCSV/p"+ savename + "w.csv",disposed2[:,2])
    # np.savetxt("plotCSV/"+savename+".csv",np.column_stack((disposed2[:,8],disposed2[:,17])),delimiter=', ')
    # np.savetxt("plotCSV/"+savename+"w.csv",disposed2[:,8])




def washer(datafile,savename,cut=None,lines=0,type = 0):
    disposed = []
    if not os.path.exists("/store/tmp/"+savename+"tmp.npy"):
        if not lines:
            with open(datafile) as file_object:
                raw = file_object.readlines()
                for i in raw:
                    j = re.sub(r'\s+',', ',i.lstrip())
                    disposed.append(j[:-2]+"\n")
        else:
            index = 0
            with open(datafile) as file_object:
                raw = file_object.readlines()
                for i in raw:
                    j = re.sub(r'\s+',', ',i.lstrip())
                    disposed.append(j[:-2]+"\n")
                    index += 1
                    if index == lines:
                        break


        with open("/store/tmp/"+savename+"tmp.csv", 'w') as f:
            f.writelines(disposed)

        a = np.array(pd.read_csv("/store/tmp/"+savename+"tmp.csv"))
        np.save("/store/tmp/"+savename+"tmp.npy", a)

    a = np.load("/store/tmp/"+savename+"tmp.npy")

    if a.shape[1] == 15:
        if cut == None:
            p = np.zeros(shape=(a.shape[0],12))
            for i in range(a.shape[0]):
                p[i] = raw_to_momentum(loaded=a[i])
                np.save("/store/tmp"+savename,p)
        else:
            flag = np.zeros(shape=(a.shape[0],))
            for i in range(a.shape[0]):
                if cut(a[i]):
                    flag[i] = 1
            number_of_survivors = np.sum(flag)
            print(str(number_of_survivors)+ " events survived the cut!")
            p = np.zeros(shape=(int(number_of_survivors),12))
            c = 0
            for i in range(a.shape[0]):
                if flag[i]:
                    p[c] = raw_to_momentum(a[i])
                    c += 1
            cutname = input('Please input cut name:/n')
            np.save("/store/tmp/p"+savename+cutname,p)
        obsevable = np.zeros(shape=(p.shape[0],16))
        for i in range(p.shape[0]):
            obsevable[i] = ob_gen(p[i])
        # try:
        #     np.save("/store/eevva/p"+savename+cutname+"withob",np.hstack((p,obsevable)))
        # except NameError:
        #     np.save("/store/eevva/p"+savename+"withob",np.hstack((p,obsevable)))
        e_gamma_extract(np.hstack((p,obsevable)),savename=savename)

    elif a.shape[1] == 4:
        flag = np.zeros(shape=(a.shape[0],))
        for i in range(a.shape[0]):
            if cut(a[i]):
                flag[i] = 1
        number_of_survivors = np.sum(flag)
        print(str(number_of_survivors) + " events survived the cut!")
        p = np.zeros(shape=(int(number_of_survivors), 2))
        c = 0
        for i in range(a.shape[0]):
            if flag[i]:
                p[c] = np.column_stack((a[i,-1],a[i,-2]))
                c += 1
        cutname = input('Please input cut name:/n')
        np.savetxt("plotCSV/p"+savename+".csv",p,delimiter=', ')


def e_gamma_extract(data,savename):
    np.savetxt("plotCSV/p"+savename+".csv",np.column_stack((data[:,8], data[:,17])),delimiter=', ')


def washer_inhomogenous(datafile,cut,savename):
    try:
        a = np.load(datafile)
    except OSError:
        a = np.array(pd.read_csv(datafile))

    survivors = 0
    flags = np.zeros(shape=(a.shape[0],1))
    for i in range(a.shape[0]):
        if cut(a[i]):
            survivors += 1
            flags[i] = 1
    print(survivors)
    b = np.zeros(shape=(survivors,2))
    c = 0
    for i in range(a.shape[0]):
        if flags[i]:
            b[c,0],b[c,1] = a[i,-2],a[i,-1]
            c += 1
    np.savetxt("plotCSV/p"+savename+"k.csv",b,delimiter=', ')


def e_gamma_xx(p):
    return p[8]

def pt_gamma_xx(p):
    return np.sqrt(p[9]**2+p[10]**2)

def z_gamma_xx(p):
    return p[-1]/np.sqrt(p[9]**2+p[10]**2+p[11]**2)

def m_missing_xx(p):
    tmp =  (np.array([500,0,0,0])-p[8:])
    # print(tmp)
    return np.sqrt(tmp[0]**2-tmp[1]**2-tmp[2]**2-tmp[3]**2)


def theta(p):
    return np.arccos(p[-1]/np.sqrt(p[1]**2+p[2]**2+p[3]**2))


def phi(p):
    return np.arccos(p[1]/np.sqrt(p[1]**2+p[2]**2))


def ob_output(data,savename,energy=240):
    output = np.zeros(shape=(data.shape[0], 4))
    for i in range(data.shape[0]):
        output[i] = np.array(
            [e_gamma_xx(data[i]), pt_gamma_xx(data[i]), z_gamma_xx(data[i]), ivmass_xx(p = data[i],energy=energy)])

    np.save('/store/eeeea/' + savename + 'd.npy', output)


def ob_output_240(data,savename):
    output = np.zeros(shape=(data.shape[0], 4))
    for i in range(data.shape[0]):
        output[i] = np.array(
            [e_gamma_xx(data[i]), pt_gamma_xx(data[i]), z_gamma_xx(data[i]), m_missing_240_xx(data[i])])

    np.save('/store/eeeea/' + savename + 'd.npy', output)


def ob_output_ew(data,savename,crossection,energy=240):
    output = np.zeros(shape=(data.shape[0], 5))
    for i in range(data.shape[0]):
        output[i] = np.array(
            [e_gamma_xx(data[i]), pt_gamma_xx(data[i]), z_gamma_xx(data[i]), ivmass_xx(p = data[i],energy=energy),crossection/data.shape[0]])
    print(output.shape)
    np.save('/store/disposed/' + savename + 'd.npy', output)


## Output function for mumugamma final state.
def ob_output_ew_mu(data,savename,crossection,energy=240):
    output = np.zeros(shape=(data.shape[0], 5))
    for i in range(data.shape[0]):
        output[i] = np.array(
            [e_gamma_xx(data[i]), pt_gamma_xx(data[i]), z_gamma_xx(data[i]), np.sqrt(inner_product(data[i,:4]+data[i,4:8],data[i,:4]+data[i,4:8])),crossection/data.shape[0]])
    print(output.shape)
    np.save('/store/disposed/' + savename + 'd.npy', output)



def lhegz_wash_to_ob(datafile,cut,savename,s=False,cepc=False):
    survivors = 0
    with open(datafile) as file_object:
        a = file_object.readlines()
    length = len(a)
    print("length: ",length)


    # Count how many events are there in the list.
    for i in range(length):
        # Remove the spaces at the beginning of each line
        a[i] = a[i].strip()
        if a[i] == '<event>':
            survivors += 1

    print('survivors: ',survivors)

    disposed = np.zeros(shape=(survivors,12))
    c = 0
    bad_data = []
    beginning = 0

    for i in range(length):
        if a[i] == '<event>':
            beginning = i
            break


    print('Beginning from line %d'%beginning)
    for i in range(beginning,length):
        # print(i)
        if a[i] == '<event>':
            tmp = np.zeros(shape=(12,))
            continue

        if a[i] == '</event>':
            disposed[c] = tmp
            c += 1
            continue
        # write something that saves here.
        # Initialise the array object once meet '<event>'.
        # save some time with continues.

        if re.match(pattern_gamma,a[i]):
            try:
                tmp[8:] = pattern_0.findall(a[i])[:4]
            except ValueError:
                bad_data.append(c)
        if re.match(pattern_chi,a[i]):
            try:
                tmp[:4] = pattern_0.findall(a[i])[:4]
            except ValueError:
                bad_data.append(c)

        if re.match(pattern_chibar,a[i]):
            try:
                tmp[4:8] = pattern_0.findall(a[i])[:4]
            except ValueError:
                bad_data.append(c)

    # print(tmp)
    # print(tmp[0]+tmp[4]+tmp[8])
    # print(tmp[1]+tmp[5]+tmp[9])
    # print(tmp[2]+tmp[6]+tmp[10])
    # print(tmp[3]+tmp[7]+tmp[11])
    # print(disposed[-1])
    # for i in range(disposed.shape[0]):
    #     if (disposed[i,0]+disposed[i,4]+disposed[i,8]>1e-6) or (disposed[i,1]+disposed[i,5]+disposed[i,9]>1e-6) or (disposed[i,2]+disposed[i,6]+disposed[i,10]>1e-6) or (disposed[i,3]+disposed[i,7]+disposed[i,11] - 1000 >1e-6):
    #         print('bing!')
    #     if (disposed[i,0]**2+disposed[i,1]**2+disposed[i,2]**2-disposed[i,3]**2)>1e-5:
    #         print('ding!')
    #     if (disposed[i,4]**2+disposed[i,5]**2+disposed[i,6]**2-disposed[i,7]**2)>1e-5:
    #         print('ging!')
    #     if (disposed[i,8]**2+disposed[i,9]**2+disposed[i,10]**2-disposed[i,11]**2)>1e-5:
    #         print('king!')
    # # for i in bad_data:
    #     if disposed[i,0] == 0:
    #         disposed[i,0] = -(disposed[i,4]+disposed[i,8])
    #         disposed[i,1] = -(disposed[i,5]+disposed[i,9])
    # print(len(bad_data))

    # np.save('/store/eexxa/'+savename+'raw.npy',disposed)
    #
    disposed=disposed[:-1]
    disposed1 = np.zeros_like(disposed)
    disposed1[:,0] = disposed[:,3]
    disposed1[:,1:4] = disposed[:,:3]
    disposed1[:,4] = disposed[:,7]
    disposed1[:,5:8]=disposed[:,4:7]
    disposed1[:,8] = disposed[:,11]
    disposed1[:,9:]=disposed[:,8:11]
    # np.save('/store/eexxa/' + savename , disposed1)
    # This measure has been validated.
    # print(np.max(disposed1[:,8]))
    np.save('/store/tmp/'+savename+'tmp.npy',disposed1)
    if s:
        print('smearing!')
        # Cuts are applied to true data at first place, so these with zero weight from FC are ignored.
        for i in range(disposed1.shape[0]):
            disposed1[i] = smear.smear_cepc_0(disposed1[i])

    c = 0
    flags = np.zeros(shape=(disposed1.shape[0],))
    for i in range(disposed1.shape[0]):
        if cut(disposed1[i]):
            c += 1
            flags[i] = 1
    print('After Cut: ',c)
    disposed2 = np.zeros(shape=(c,12))
    d = 0
    for i in range(disposed1.shape[0]):
        if flags[i]:
            disposed2[d] = disposed1[i]
            d += 1

        # Smearing data if required.
    # if s:
    #     print('smearing!')
    #     # Cuts are applied to true data at first place, so these with zero weight from FC are ignored.
    #     a = disposed2[:]
    #     # print(sum(flags))
    #     # input('halt')
    #     smeared_data = np.zeros(shape=(np.int(sum(flags)), 12))
    #     c = 0
    #     for i in range(a.shape[0]):
    #         if flags[i]:
    #             tosmear = a[i, -4:]
    #             # Calculate the true angular coordinates of the data to smear.
    #             truetheta = theta(tosmear)
    #             truephi = phi(tosmear)
    #             stheta = smear.smear_angle(E=tosmear[0], t=truetheta)
    #             se = smear.smear(E=tosmear[0])
    #             smeared_data[c, 8:12] = np.array([se, se * np.sin(stheta) * np.cos(truephi),
    #                                               se * np.sin(stheta) * np.sin(truephi), se * np.cos(stheta)])
    #             smeared_data[c, :8] = a[i, :8]
    #             c += 1
    #
    #     # Apply cuts again.
    #     flags2 = np.zeros(shape=(smeared_data.shape[0]))
    #     for i in range(flags2.shape[0]):
    #         if cut(smeared_data[i, :12]):
    #             flags2[i] = 1
    #
    #     truesurvivors = np.zeros(shape=(np.int(np.sum(flags2)), 4))
    #     c = 0
    #     a = smeared_data[:]
    #     for i in range(flags2.shape[0]):
    #         if flags2[i]:
    #             truesurvivors[c] = np.array(
    #                 [e_gamma_xx(a[i, :12]), pt_gamma_xx(a[i, :12]), z_gamma_xx(a[i, :12]), m_missing_xx(a[i, :12])])
    #             c += 1
    #     np.save('/store/eeeea/' + savename + 'ds.npy', truesurvivors)
    #     return 0
    # To tunes the output data file, modify this part.
    # In this work (CEPC-DM) we're currently only interested in 4 observables.
    # E_\gamma, p_{\gamma T}, z_\gamma and m_{\text{miss}}.
    if not cepc:
        ob_output(data=disposed2, savename=savename)
    else:
        ob_output_240(data=disposed2, savename=savename)

# lhegz_wash_to_ob(datafile="/store/eexxa/xdxd1.lhe",cut=None,savename='xdxd1')

def fcoutput_to_ob(datafile,weightfile,cut=cut.cut_nocut,savename='test',lines=False):
    disposed = []
    if not os.path.exists("/store/tmp/"+savename+"tmp.npy"):
        if not lines:
            with open(datafile) as file_object:
                raw = file_object.readlines()
                for i in raw:
                    j = re.sub(r'\s+',', ',i.lstrip())
                    disposed.append(j[:-2]+"\n")
        else:
            index = 0
            with open(datafile) as file_object:
                raw = file_object.readlines()
                for i in raw:
                    j = re.sub(r'\s+',', ',i.lstrip())
                    disposed.append(j[:-2]+"\n")
                    index += 1
                    if index == lines:
                        break


        with open("/store/tmp/"+savename+"tmp.csv", 'w') as f:
            f.writelines(disposed)

        a = np.array(pd.read_csv("/store/tmp/"+savename+"tmp.csv"))
        np.save("/store/tmp/"+savename+"tmp.npy", a)
    a = np.load("/store/tmp/"+savename+"tmp.npy")

    # print(a[0])
    # input('halt')
    for i in range(a.shape[0]):
        if a[i,8] > 160:
            print('bing!')

    w = np.array(pd.read_csv(weightfile))

    survivors = 0
    flags = np.zeros(shape=(a.shape[0],1))
    for i in range(a.shape[0]):
        if cut(a[i]):
            flags[i] = 1
            survivors += 1
    print(survivors)
    b = np.zeros(shape=(survivors,5))
    c = 0
    for i in range(a.shape[0]):
        if flags[i]:
            b[c,:4]=np.array([e_gamma_xx(a[i]), pt_gamma_xx(a[i]), z_gamma_xx(a[i]), m_missing_xx(a[i])])
            b[c,4] = w[i]
            c += 1

    np.save('/store/eeeea/'+savename+'d.npy',b)


def lhegz_wash_to_ob_w(datafile,cut,xsection,savename,energy,s=False,smearer=smear.no_smear):
    survivors = 0
    with open(datafile) as file_object:
        a = file_object.readlines()
    length = len(a)
    print("length: ",length)


    # Count how many events are there in the list.
    for i in range(length):
        # Remove the spaces at the beginning of each line
        a[i] = a[i].strip()
        if a[i] == '<event>':
            survivors += 1

    print('survivors: ',survivors)

    disposed = np.zeros(shape=(survivors,12))
    c = 0
    bad_data = []
    beginning = 0

    for i in range(length):
        if a[i] == '<event>':
            beginning = i
            break


    print('Beginning from line %d'%beginning)
    for i in range(beginning,length):
        # print(i)
        if a[i] == '<event>':
            tmp = np.zeros(shape=(12,))
            continue

        if a[i] == '</event>':
            disposed[c] = tmp
            c += 1
            continue

        if re.match(pattern_gamma,a[i]):
            try:
                tmp[8:] = pattern_0.findall(a[i])[:4]
            except ValueError:
                bad_data.append(c)
        if re.match(pattern_chi,a[i]):
            try:
                tmp[:4] = pattern_0.findall(a[i])[:4]
            except ValueError:
                bad_data.append(c)

        if re.match(pattern_chibar,a[i]):
            try:
                tmp[4:8] = pattern_0.findall(a[i])[:4]
            except ValueError:
                bad_data.append(c)


    disposed=disposed[:-1]
    disposed1 = np.zeros_like(disposed)
    disposed1[:,0] = disposed[:,3]
    disposed1[:,1:4] = disposed[:,:3]
    disposed1[:,4] = disposed[:,7]
    disposed1[:,5:8]=disposed[:,4:7]
    disposed1[:,8] = disposed[:,11]
    disposed1[:,9:]=disposed[:,8:11]

    np.save('/store/tmp/'+savename+'tmp.npy',disposed1)
    if s:
        print('smearing!')
        for i in range(disposed1.shape[0]):
            disposed1[i] = smearer(disposed1[i])

    c = 0
    flags = np.zeros(shape=(disposed1.shape[0],))
    for i in range(disposed1.shape[0]):
        if cut(disposed1[i]):
            c += 1
            flags[i] = 1
    print('After Cut: ',c)
    disposed2 = np.zeros(shape=(c,12))
    d = 0
    for i in range(disposed1.shape[0]):
        if flags[i]:
            disposed2[d] = disposed1[i]
            d += 1

    ob_output_ew(data=disposed2, savename=savename, crossection=xsection,energy=energy)



def lhegz_wash_to_ob_auto(datafile,cut,savename,energy,s=False,smearer=smear.no_smear):
    survivors = 0
    with open(datafile) as file_object:
        a = file_object.readlines()
    length = len(a)
    print("length: ",length)


    # Count how many events are there in the list.
    for i in range(length):
        # Remove the spaces at the beginning of each line
        a[i] = a[i].strip()
        if a[i] == '<event>':
            survivors += 1

    print('survivors: ',survivors)

    disposed = np.zeros(shape=(survivors,12))
    c = 0
    bad_data = []
    beginning = 0

    for i in range(length):
        if a[i] == '<event>':
            beginning = i
            break


    print('Beginning from line %d'%beginning)

    xsection = np.float(pattern_0.findall(a[beginning + 1])[0])

    for i in range(beginning,length):
        # print(i)
        if a[i] == '<event>':
            tmp = np.zeros(shape=(12,))
            continue

        if a[i] == '</event>':
            disposed[c] = tmp
            c += 1
            continue

        if re.match(pattern_gamma,a[i]):
            try:
                tmp[8:] = pattern_0.findall(a[i])[:4]
            except ValueError:
                bad_data.append(c)
        if re.match(pattern_chi,a[i]):
            try:
                tmp[:4] = pattern_0.findall(a[i])[:4]
            except ValueError:
                bad_data.append(c)

        if re.match(pattern_chibar,a[i]):
            try:
                tmp[4:8] = pattern_0.findall(a[i])[:4]
            except ValueError:
                bad_data.append(c)


    disposed=disposed[:-1]
    disposed1 = np.zeros_like(disposed)
    disposed1[:,0] = disposed[:,3]
    disposed1[:,1:4] = disposed[:,:3]
    disposed1[:,4] = disposed[:,7]
    disposed1[:,5:8]=disposed[:,4:7]
    disposed1[:,8] = disposed[:,11]
    disposed1[:,9:]=disposed[:,8:11]

    np.save('/store/tmp/'+savename+'tmp.npy',disposed1)
    if s:
        print('smearing!')
        for i in range(disposed1.shape[0]):
            disposed1[i] = smearer(disposed1[i])

    c = 0
    flags = np.zeros(shape=(disposed1.shape[0],))
    for i in range(disposed1.shape[0]):
        if cut(disposed1[i]):
            c += 1
            flags[i] = 1
    print('After Cut: ',c)
    disposed2 = np.zeros(shape=(c,12))
    d = 0
    for i in range(disposed1.shape[0]):
        if flags[i]:
            disposed2[d] = disposed1[i]
            d += 1

    ob_output_ew(data=disposed2, savename=savename, crossection=xsection,energy=energy)


def lhegz_wash_to_muob_auto(datafile,cut,savename,energy,s=False,smearer=smear.no_smear):
    survivors = 0
    with open(datafile) as file_object:
        a = file_object.readlines()
    length = len(a)
    print("length: ",length)


    # Count how many events are there in the list.
    for i in range(length):
        # Remove the spaces at the beginning of each line
        a[i] = a[i].strip()
        if a[i] == '<event>':
            survivors += 1

    print('survivors: ',survivors)

    disposed = np.zeros(shape=(survivors,12))
    c = 0
    bad_data = []
    beginning = 0

    for i in range(length):
        if a[i] == '<event>':
            beginning = i
            break


    print('Beginning from line %d'%beginning)

    xsection = 0.95*np.float(pattern_0.findall(a[beginning + 1])[0])

    for i in range(beginning,length):
        # print(a[i])
        # if i == beginning+1:
        #     input('halt')
        if a[i] == '<event>':
            tmp = np.zeros(shape=(12,))
            continue

        if a[i] == '</event>':
            disposed[c] = tmp
            c += 1
            continue

        if re.match(pattern_gamma,a[i]):
            # print('gamma!')
            try:
                tmp[8:] = pattern_0.findall(a[i])[:4]
            except ValueError:
                bad_data.append(c)
        if re.match(pattern_mu,a[i]):
            # print('bing!')
            try:
                tmp[:4] = pattern_0.findall(a[i])[:4]
            except ValueError:
                bad_data.append(c)

        if re.match(pattern_mubar,a[i]):
            try:
                tmp[4:8] = pattern_0.findall(a[i])[:4]
            except ValueError:
                bad_data.append(c)


    disposed=disposed[:-1]
    disposed1 = np.zeros_like(disposed)
    disposed1[:,0] = disposed[:,3]
    disposed1[:,1:4] = disposed[:,:3]
    disposed1[:,4] = disposed[:,7]
    disposed1[:,5:8]=disposed[:,4:7]
    disposed1[:,8] = disposed[:,11]
    disposed1[:,9:]=disposed[:,8:11]

    np.save('/store/tmp/'+savename+'tmp.npy',disposed1)
    if s:
        print('smearing!')
        for i in range(disposed1.shape[0]):
            disposed1[i] = smearer(disposed1[i])

    c = 0
    flags = np.zeros(shape=(disposed1.shape[0],))
    for i in range(disposed1.shape[0]):
        if cut(disposed1[i]):
            c += 1
            flags[i] = 1
    print('After Cut: ',c)
    disposed2 = np.zeros(shape=(c,12))
    d = 0
    for i in range(disposed1.shape[0]):
        if flags[i]:
            disposed2[d] = disposed1[i]
            d += 1
    # return disposed2
    ob_output_ew_mu(data=disposed2, savename=savename, crossection=xsection,energy=energy)




def fcoutput_to_ob(datafile,weightfile,cut=cut.cut_nocut,savename='test',lines=False):
    disposed = []
    if not os.path.exists("/store/tmp/"+savename+"tmp.npy"):
        if not lines:
            with open(datafile) as file_object:
                raw = file_object.readlines()
                for i in raw:
                    j = re.sub(r'\s+',', ',i.lstrip())
                    disposed.append(j[:-2]+"\n")
        else:
            index = 0
            with open(datafile) as file_object:
                raw = file_object.readlines()
                for i in raw:
                    j = re.sub(r'\s+',', ',i.lstrip())
                    disposed.append(j[:-2]+"\n")
                    index += 1
                    if index == lines:
                        break


        with open("/store/tmp/"+savename+"tmp.csv", 'w') as f:
            f.writelines(disposed)

        a = np.array(pd.read_csv("/store/tmp/"+savename+"tmp.csv"))
        np.save("/store/tmp/"+savename+"tmp.npy", a)
    a = np.load("/store/tmp/"+savename+"tmp.npy")

    for i in range(a.shape[0]):
        if a[i,8] > 160:
            print('bing!')

    w = np.array(pd.read_csv(weightfile))

    survivors = 0
    flags = np.zeros(shape=(a.shape[0],1))
    for i in range(a.shape[0]):
        if cut(a[i]):
            flags[i] = 1
            survivors += 1
    print(survivors)
    b = np.zeros(shape=(survivors,5))
    c = 0
    for i in range(a.shape[0]):
        if flags[i]:
            b[c,:4]=np.array([e_gamma_xx(a[i]), pt_gamma_xx(a[i]), z_gamma_xx(a[i]), m_missing_xx(a[i])])
            b[c,4] = w[i]
            c += 1

    np.save('/store/eeeea/'+savename+'d.npy',b)



###################
#Prototype fc output parser. Use the general version instead.
###################
def fcoutput_to_ob_w(datafile,weightfile,cut=cut.cut_nocut,savename='test', lines=False, s=False,cepc=False,smearer=smear.smear_cepc_0):
    disposed = []
    print(datafile)
    if not os.path.exists("/store/tmp/"+savename+"tmp.npy"):
        print('bing1')
        if not lines:
            with open(datafile) as file_object:
                raw = file_object.readlines()
                for i in raw:
                    j = re.sub(r'\s+',', ',i.lstrip())
                    disposed.append(j[:-2]+"\n")
        else:
            index = 0
            with open(datafile) as file_object:
                raw = file_object.readlines()
                for i in raw:
                    j = re.sub(r'\s+',', ',i.lstrip())
                    disposed.append(j[:-2]+"\n")
                    index += 1
                    if index == lines:
                        break


        with open("/store/tmp/"+savename+"tmp.csv", 'w') as f:
            f.writelines(disposed)

        a = np.array(pd.read_csv("/store/tmp/"+savename+"tmp.csv"))
        np.save("/store/tmp/"+savename+"tmp.npy", a)
    a = np.load("/store/tmp/"+savename+"tmp.npy")
    w = np.array(pd.read_csv(weightfile))
    print(np.sum(w))
    print(a[0])
    # Smearing data if required.
    if s:
        print('smearing!')
        # Cuts are applied to true data at first place, so these with zero weight from FC are ignored.
        for i in range(a.shape[0]):
            a[i] = smearer(a[i])
    print('Done smearing!')

    c = 0
    flags = np.zeros_like(w)
    for i in range(w.shape[0]):
        if cut(a[i]):
            flags[i] = 1
            c += 1

    b = np.zeros(shape=(c,5))
    c = 0

    if not cepc:
        for i in range(w.shape[0]):
            if flags[i]:
                b[c] = np.array([e_gamma_xx(a[i]), pt_gamma_xx(a[i]), z_gamma_xx(a[i]), m_missing_xx(a[i]),w[i]])
                c += 1
    else:
        for i in range(w.shape[0]):
            if flags[i]:
                # b[c] = np.array([e_gamma_xx(a[i]), pt_gamma_xx(a[i]), z_gamma_xx(a[i]), m_missing_240_xx(a[i]),w[i]])
                b[c] = np.array([e_gamma_xx(a[i]), pt_gamma_xx(a[i]), z_gamma_xx(a[i]), ivmass_xx(a[i]), w[i]])
                c += 1
    print(np.sum(b[:,-1]))
    np.save('/store/disposed/'+savename + 'd.npy', b)


# I have no idea what this was intended to do. DO NOT USE.
def fcoutput_to_ob_sw(datafile,weightfile,cut=cut.cut_nocut,savename='test',lines=False,smear=False):
    disposed = []
    if not os.path.exists("/store/tmp/"+savename+"tmp.npy"):
        if not lines:
            with open(datafile) as file_object:
                raw = file_object.readlines()
                for i in raw:
                    j = re.sub(r'\s+',', ',i.lstrip())
                    disposed.append(j[:-2]+"\n")
        else:
            index = 0
            with open(datafile) as file_object:
                raw = file_object.readlines()
                for i in raw:
                    j = re.sub(r'\s+',', ',i.lstrip())
                    disposed.append(j[:-2]+"\n")
                    index += 1
                    if index == lines:
                        break


        with open("/store/tmp/"+savename+"tmp.csv", 'w') as f:
            f.writelines(disposed)

        a = np.array(pd.read_csv("/store/tmp/"+savename+"tmp.csv"))
        np.save("/store/tmp/"+savename+"tmp.npy", a)
    a = np.load("/store/tmp/"+savename+"tmp.npy")
    w = np.array(pd.read_csv(weightfile))
    c = 0
    for i in range(w.shape[0]):
        if w[i]:
            c += 1
    b = np.zeros(shape=(c,13))
    c = 0
    # print(c)
    for i in range(w.shape[0]):
        if w[i]:
            b[c,:12],b[c,12] = a[i],w[i]
            c += 1

    flags2 = np.zeros(shape=(b.shape[0]))
    c = 0
    d = 0
    for i in range(b.shape[0]):
        if cut(b[i]):
            flags2[i] = 1
            c += 1
            d += b[i,-1]


    e = np.zeros(shape=(c, 5))
    c = 0
    print(d)
    for i in range(b.shape[0]):
        if flags2[i]:
            e[c] = np.array([e_gamma_xx(b[i,:12]), pt_gamma_xx(b[i,:12]), z_gamma_xx(b[i,:12]), m_missing_xx(b[i,:12]), b[i,-1]])
            c += 1

    print(np.sum(e[:,-1]))
    np.save('/store/eeeea/' + savename + 'd.npy', e)

    # np.save('/store/eeeea/' + savename + 'd.npy', b)


def general_dat_parser(datafile):
    os.system('rm /store/tmp/generaltmp.csv')
    disposed = []
    with open(datafile) as file_object:
        raw = file_object.readlines()
        for i in raw:
            j = re.sub(r'\s+', ', ', i.lstrip())
            disposed.append(j[:-2] + "\n")
    with open("/store/tmp/generaltmp.csv", 'w') as f:
        f.writelines(disposed)
    a = np.array(pd.read_csv("/store/tmp/generaltmp.csv"))
    os.system('rm /store/tmp/generaltmp.csv')
    print(a.shape)
    return a


########################
# Working snathced Formcalc .dat file parser.
# Two files required: mom.dat and weight.dat.
########################
def fcoutput_to_ob_w_general(datafile,weightfile,energy,cut=cut.cut_nocut,savename='test', lines=False, s=True,smearer=smear.smear_cepc_0):
    disposed = []
    print(datafile)
    a,w =general_dat_parser(datafile), general_dat_parser(weightfile)
    print(np.sum(w))
    print(a[0])

    if s:
        print('smearing!')
        # Cuts are applied to true data at first place, so these with zero weight from FC are ignored.
        for i in range(a.shape[0]):
            a[i] = smearer(a[i])
    print('Done smearing!')

    c = 0
    flags = np.zeros(shape=(w.shape[0]))
    for i in range(w.shape[0]):
        if cut(a[i]):
            flags[i] = 1
            c += 1

    b = np.zeros(shape=(c,5))
    c = 0


    for i in range(w.shape[0]):
        print(flags[i])
        if flags[i]:
            # b[c] = np.array([e_gamma_xx(a[i]), pt_gamma_xx(a[i]), z_gamma_xx(a[i]), m_missing_240_xx(a[i]),w[i]])
            b[c] = np.array([e_gamma_xx(a[i]), pt_gamma_xx(a[i]), z_gamma_xx(a[i]), ivmass_xx(a[i],energy=energy), w[i]])
            c += 1
    print(np.sum(b[:,-1]))
    np.save('/store/disposed/'+savename + 'd.npy', b)


def fcoutput_to_ob_w_general_multichannel(datafile,weightfile,energy,
                                          cut=cut.cut_nocut,savename='test', s=True,smearer=smear.smear_cepc_0,channels=None):
    print('Now handling: %s !\n'%datafile)
    a,w0 =general_dat_parser(datafile), general_dat_parser(weightfile)
    print('Data preprocessing done!')
    if channels == None:
        channels = np.linspace(0,w0.shape[1],w0.shape+1)
    elif channels == []:
        raise ValueError('You are not calulcating anything! What are you thinking!')
    w = np.zeros(shape=(w0.shape[0],))
    print('Finished assigning weights!')
    for i in range(w.shape[0]):
        for j in channels:
            w[i] += w0[i,j]
    print(np.sum(w0[:,0]),np.sum(w0[:,1]),np.sum(w0[:,2]))
    print(np.sum(w))
    # print(a[0])

    if s:
        print('smearing!')
        # Cuts are applied to true data at first place, so these with zero weight from FC are ignored.
        for i in range(a.shape[0]):
            a[i] = smearer(a[i])
    print('Done smearing!')

    c = 0
    flags = np.zeros_like(w)
    for i in range(w.shape[0]):
        if cut(a[i]):
            flags[i] = 1
            c += 1

    b = np.zeros(shape=(c,5))
    c = 0


    for i in range(w.shape[0]):
        if flags[i]:
            # b[c] = np.array([e_gamma_xx(a[i]), pt_gamma_xx(a[i]), z_gamma_xx(a[i]), m_missing_240_xx(a[i]),w[i]])
            b[c] = np.array([e_gamma_xx(a[i]), pt_gamma_xx(a[i]), z_gamma_xx(a[i]), ivmass_xx(a[i],energy=energy), w[i]])
            c += 1
    print(np.sum(b[:,-1]))
    np.save('/store/disposed/'+savename + 'd.npy', b)


def lhco_wash(datafile,savename):

    if not os.path.exists("/store/tmp/"+savename+"tmp.npy"):
        disposed = []
        print('bing!')
        with open(datafile) as file_object:
            raw = file_object.readlines()
            for i in raw:
                j = re.sub(r'\s+', ', ', i.lstrip())
                # print(j)
                if (pattern_lhco_gflag.findall(j)) and len(j) > 30 :
                    # print(j)
                    jj = pattern_lhco_gdata.findall(j)[:3]
                    # print(jj)
                    # print(jj)
                    for i in range(3):
                        jj[i] = np.float(jj[i])
                        # print(jj[i])
                    if jj:
                        disposed.append(jj)
            np.save('/store/tmp/'+savename+'tmp.npy',disposed)

    else:
        disposed = np.load('/store/tmp/'+savename+'tmp.npy')
    return disposed


# Disposing Delphes generated root file.
def root_wash(datafile,savename,energy = 240):
    os.system('echo hello world')
    os.system('/home/xyh/MG5_aMC_v2_6_2/Delphes/root2lhco '+datafile+' /store/disposed/lhcos/'+savename+'.lhco')
    data = np.array(lhco_wash(datafile='/store/disposed/lhcos/'+savename+'.lhco',savename=savename))
    datad = np.zeros(shape=(data.shape[0],4))
    for i in range(data.shape[0]):
        if data[i,0] == 0:
            print(data[i])
        cos = eta_to_cos(data[i,0])
        theta = np.arccos(cos)
        sin = np.sin(np.arccos(cos))
        egamma = data[i,2]/sin
        pt = data[i,2]
        mmissing = np.sqrt((energy-egamma)**2-egamma*egamma)
        disposed = np.array([egamma,pt,cos,mmissing])
        datad[i] = disposed
    print(datad.shape)
    np.save('/store/disposed/'+savename+'_delpd.npy',datad)



def lhco_wash_mu(datafile,savename):

    if not os.path.exists("/store/tmp/"+savename+"tmp.npy"):
        disposed = []
        print('bing!')
        with open(datafile) as file_object:
            raw = file_object.readlines()
            tmp = []
            for i in range(1,len(raw)):
                linex = raw[i]
                j = re.sub(r'\s+', ', ', linex.lstrip())
                print(j)
                if (pattern_lhco_gflag.findall(j)) and len(j) > 30 :
                    print("gamma!")
                    # print(j)
                    jj = pattern_lhco_gdata.findall(j)[:3]
                    # jjmu1,jjmu2 = pattern_lhco_gdata.findall(j)[:3],pattern_lhco_gdata.findall(j)[:3]
                    # print(jj)
                    # print(jj)
                    for i in range(3):
                        jj[i] = np.float(jj[i])
                        # print(jj[i])
                    if jj:
                        tmp.append(jj)
                    continue

                if (pattern_lhco_mu1flag.findall(j)) and len(j) > 30 :
                    print('mu!')
                    jj = pattern_lhco_gdata.findall(j)[:3]
                    for i in range(3):
                        jj[i] = np.float(jj[i])
                    # if jj[0] == 0 and jj[1] == 0:
                    #     print(jj,j)
                    #     input('halt')
                    if jj:
                        continue

                if (pattern_lhco_mu2flag.findall(j)) and len(j) > 30 :
                    print('mu!')

                    jj = pattern_lhco_gdata.findall(j)[:3]
                    for i in range(3):
                        jj[i] = np.float(jj[i])
                    # if jj[0] == 0 and jj[1] == 0:
                    #     print(jj,j)
                    #     input('halt')
                    if jj:
                        tmp.append(jj)
                    continue

                if (pattern_lhco_mu3flag.findall(j)) and len(j) > 30 :
                    jj = pattern_lhco_gdata.findall(j)[:3]
                    print('mu!')

                    for i in range(3):
                        jj[i] = np.float(jj[i])
                    if jj:
                        tmp.append(jj)
                    continue
                if pattern_lhco_missing.findall(j):
                    continue

                if pattern_lhco_beginning.findall(j) and len(j) < 30:
                    tmp[:3],tmp[-3:] = tmp[-3:],tmp[:3]
                    # if tmp[-1] != 0 and (tmp[0] == 0 and tmp[1] == 0 ):
                    #     print(tmp)
                    #     print(re.sub(r'\s+', ', ', raw[i-3].lstrip()),'\n',re.sub(r'\s+', ', ', raw[i-2].lstrip()),'\n',re.sub(r'\s+', ', ', raw[i-1]))
                    # if not tmp[0] == 0 and tmp[1] == 0:
                    disposed.append(tmp)
                    tmp = []
                    continue
                    # print('!')
                # print('no match!')
                # print(j)
                # input('halt')
            np.save('/store/tmp/'+savename+'tmp.npy',disposed)

    else:
        disposed = np.load('/store/tmp/'+savename+'tmp.npy')
    return disposed[1:]


def p_off_lhco(data,mass=0):
    cosp = eta_to_cos(data[0])
    thetap = np.arccos(cosp)
    sinp = np.sin(thetap)
    pmod = data[2]/sinp
    E = np.sqrt(pmod**2+mass**2)
    pz = data[2]/np.tan(thetap)
    px = data[2]*np.cos(data[1]/(2*np.pi))
    py = data[2]*np.sin(data[1]/(2*np.pi))
    return np.array([E,px,py,pz])


def root_wash_mu(datafile,savename,energy = 240):
    os.system('echo hello world')
    os.system('/home/xyh/MG5_aMC_v2_6_2/Delphes/root2lhco '+datafile+' /store/disposed/lhcos/'+savename+'.lhco')
    data = np.array(lhco_wash_mu(datafile='/store/disposed/lhcos/'+savename+'.lhco',savename=savename))
    print(data[:20])
    print(data.shape)
    datad = np.zeros(shape=(data.shape[0],4))
    for i in range(data.shape[0]):
        if data[i,0] == 0:
            print(data[i])
        pgamma,pmu1,pmu2 = p_off_lhco(data[i,-3:]),p_off_lhco(data[i,:3],mass=0.105),p_off_lhco(data[i,3:6],mass=0.105)
        ivmassmu1mu2 = np.sqrt(pmu1[0]*pmu2[0]-pmu1[1]*pmu2[1]-pmu1[2]*pmu2[1]-pmu1[3]*pmu2[3])
        datad[i] = np.array([pgamma[0],data[i,-1],eta_to_cos(data[i,-3]),ivmassmu1mu2])
    print(datad.shape)
    np.save('/store/disposed/'+savename+'_delpd.npy',datad)


if __name__ == '__main__':
    # mass = 10**np.linspace(0,2,21)
    lhegz_wash_to_ob_auto(datafile='/store/darkphoton2/zp_10GeV_0.01.lhe',
                                   savename = 'zp_10GeV_0.01',energy=240,
                          cut = cut.cut_nocut,s=True,smearer=smear.smear_cepc_0)
    # lhegz_wash_to_ob_auto(datafile='/store/50GeV_histo.lhe',
    #                                savename = '50GeV_histo_smear',energy=240,
    #                       cut = cut.cut_nocut,s=True,smearer=smear.smear_cepc_0)

    # lhegz_wash_to_ob_auto(datafile='/store/74.9GeV_histo.lhe',
    #                                savename = '74.9GeV_histo_nosmear',energy=240,
    #                       cut = cut.cut_nocut,s=False,smearer=smear.no_smear)
    # lhegz_wash_to_ob_auto(datafile='/store/74.9GeV_histo.lhe',
    #                                savename = '74.9GeV_histo_smear',energy=240,
    #                       cut = cut.cut_nocut,s=True,smearer=smear.smear_cepc_0)


    # a = lhegz_wash_to_muob_auto(datafile='/store/darkphoton2/muon2.lhe',
    #                             cut=cut.cut_nocut,energy=240,s=False,
    #                             smearer=smear.smear_cepc_0,savename='muon2_2'
    #                             )
    # print(a.shape)
    # print(a[0],a[-1])
    # root_wash(datafile='/store/darkphoton2/mg5runs/visible/Events/run_07/tag_1_delphes_events.root',
    #           savename='rootwashtest',energy=240)
    # count = 0
    # for i in 10**np.linspace(0,2,21):
    #     fcoutput_to_ob_w(datafile='/store/eeeea/mq132largem%f.dat'%i,weightfile='/store/eeeea/mq132largem%fw.dat'%i,
    #              cut=cut.cut_nocut,savename='mq132dot%d'%count,s=True,cepc=True)
    #     count += 1

    # fcoutput_to_ob_w(datafile='/store/eexxa2/xxcepc1.dat',weightfile='/store/eexxa2/xxcepc1w.dat',
    #                  cut=cut.cut_nocut,savename='xxcepc1',s=True,cepc=True)
    # fcoutput_to_ob_w(datafile='/store/eevva2/vevecepc8.dat',weightfile='/store/eevva2/vevecepc8w.dat',
    #                  cut=cut.cut_nocut,savename='vevecepc8',s=True,cepc=True)
    # fcoutput_to_ob_w(datafile='/store/eevva2/vmvmcepc8.dat',weightfile='/store/eevva2/vmvmcepc8w.dat',
    #                  cut=cut.cut_nocut,savename='vmvmcepc8',s=True,cepc=True)
    # fcoutput_to_ob_w(datafile='/stor/e/eeeea/mq132largem1.000000.dat',weightfile='/store/eeeea/mq132largem1.000000w.dat',
    #                  cut=cut.cut_12_cepc_1_irredu,savename='m1nocut',s=True,cepc=True)
    # root_wash('s')
    #####
    #####
    # root_wash('/store/eevva2/mg5runs/eevlvl1/Events/run_02/tag_1_delphes_events.root',savename='test3')
    # root_wash('/store/eexxa/mg5runs/mqdelrun/Events/run_01/tag_1_delphes_events.root',savename='mqm1del')

    # a = np.array(lhco_wash(datafile='/store/disposed/lhcos/deldata1.lhco',savename='deldata1'))
    # print(a.shape)
    # for i in range(1,22):
    #         root_wash('/store/milliq/deldata%d.root'%i,savename='deldata%d'%i)



    ###ILC data processing.
    # for i in range(50):
    #     mass = np.linspace(1,201,51)[i]
    #     fcoutput_to_ob_w_general(datafile='/store/milliq/ilc2/mqilc132m%f.dat'%mass,
    #                              weightfile='/store/milliq/ilc2/mqilc132m%fw.dat'%mass,
    #     energy=500,cut=cut.cut_nocut,savename='milliq/ilc/mqilc132dot%d'%i,s=True,smearer=smear.smear_ilc)

        # print(mass)
        # print(os.path.exists('/store/milliq/ilc2/mqilc132m%f.dat'%mass))
    # fcoutput_to_ob_w_general(datafile='/store/milliq/ilc/veveilc.dat',
    #                          weightfile='/store/milliq/ilc/veveilcw.dat',
    # energy=500,cut=cut.cut_nocut,savename='milliq/ilc/veveilc',s=True,smearer=smear.smear_ilc)
    # fcoutput_to_ob_w_general(datafile='/store/milliq/ilc/vmvmilc.dat',
    #                          weightfile='/store/milliq/ilc/vmvmilcw.dat',
    # energy=500,cut=cut.cut_nocut,savename='milliq/ilc/vmvmilc',s=True,smearer=smear.smear_ilc)


    ########################
    ####1211paper Validation. Why do we have to do this?
    # xsection = np.array([17.24,17.22,
    #                      17.27,17.25,17.19,17.1,17.01,17.01,17.06,17.07,17.07,
    #                      17.11,17.14,17.14,17.15,17.12,17.04,16.79,16.12,14.36,9.541])
    # print(xsection.shape)
    # for i in range(21):
    #     lhegz_wash_to_ob_w(
    #         datafile='/store/4fermion/validation/1211/data%d.lhe'%(i+1),
    #         savename='1211va/dot%d'%(i+1),energy=250,xsection=xsection[i],
    #         cut=cut.cut_nocut,s=True,smearer=smear.smear_ilc
    #     )
    ##### BG simulation for 1211 validation.
    # fcoutput_to_ob_w_general(datafile='/store/4fermion/validation/bg/veveilcval.dat',
    #                          weightfile='/store/4fermion/validation/bg/veveilcvalw.dat',
    # energy=250,cut=cut.cut_nocut,savename='1211va/veveilc',s=True,smearer=smear.smear_ilc)
    # fcoutput_to_ob_w_general(datafile='/store/4fermion/validation/bg/vmvmilcval.dat',
    #                          weightfile='/store/4fermion/validation/bg/vmvmilcvalw.dat',
    # energy=250,cut=cut.cut_nocut,savename='1211va/vmvmilc',s=True,smearer=smear.smear_ilc)
    # lhegz_wash_to_ob_w(
    #     datafile='/store/4fermion/validation/bg/bgmg5.lhe',
    #     savename='1211va/bgmg5',energy=250,xsection=4.34,
    #     cut=cut.cut_nocut,s=True,smearer=smear.no_smear
    # )





    ######## CEPC Z pole data parser.

    # fcoutput_to_ob_w_general(datafile='/store/milliq/cepcz/vevecepcz.dat',
    #                          weightfile='/store/milliq/cepcz/vevecepczw.dat',
    # energy=91.2,cut=cut.cut_nocut,savename='vevecepcz',s=True,smearer=smear.smear_cepc_0)
    # fcoutput_to_ob_w_general(datafile='/store/milliq/cepcz/vmvmcepcz.dat',
    #                          weightfile='/store/milliq/cepcz/vmvmcepczw.dat',
    # energy=91.2,cut=cut.cut_nocut,savename='vmvmcepcz',s=True,smearer=smear.smear_cepc_0)
    # for i in range(21):
    #     fcoutput_to_ob_w_general(datafile='/store/milliq/cepcz/mqz132m%f.dat'%mass[i],
    #                              weightfile='/store/milliq/cepcz/mqz132m%fw.dat'%mass[i],
    #              cut=cut.cut_nocut,savename='mqcepcz132dot%d'%i,s=True,smearer=smear.smear_cepc_0,
    #                              energy=91.2)
    #
    ##########################




    ######## CEPC W pole data parser.
    #
    # fcoutput_to_ob_w_general(datafile='/store/milliq/cepcw/vevewcepc.dat',
    #                          weightfile='/store/milliq/cepcw/vevewcepcw.dat',
    # energy=160,cut=cut.cut_nocut,savename='milliq/cepcw/vevecepcw',s=True,smearer=smear.smear_cepc_0)
    # fcoutput_to_ob_w_general(datafile='/store/milliq/cepcw/vmvmwcepc.dat',
    #                          weightfile='/store/milliq/cepcw/vmvmwcepcw.dat',
    # energy=160,cut=cut.cut_nocut,savename='milliq/cepcw/vmvmcepcw',s=True,smearer=smear.smear_cepc_0)
    # for i in range(21):
    #     fcoutput_to_ob_w_general(datafile='/store/milliq/cepcw/mqw132m%f.dat'%mass[i],
    #                              weightfile='/store/milliq/cepcw/mqw132m%fw.dat'%mass[i],
    #              cut=cut.cut_nocut,savename='milliq/cepcw/mqw132dot%d'%i,s=True,smearer=smear.smear_cepc_0,
    #                              energy=160)

    #########################


    ######## CEPC 4 operator data parser.
    # vaxsection = np.array([50.44,50.87,50.42,50.87,50.65,50.91,50.91,50.96,51.02,51.08,51.14,50.98,50.4,49.71,48.35,46.63,43.41,38.48,31.12,20.48,7.367])
    # sssection = np.array([36.42,36.73,36.58,36.8,36.79,36.89,36.86,37.11,37.1,37.22,37.05,36.88,36.66,36.13,35.15,33.8,31.84,28.01,22.57,14.81,5.331])
    # stsection = np.array([14.62,14.59,14.61,14.57,14.69,14.73,14.8,14.81,14.79,14.89,14.87,14.83,14.84,14.7,14.64,14.35,13.88,13.1,11.85,9.805,6.24])
    # vvsection = np.array([58.12,58.37,58.55,58.57,58.64,58.83,59.21,59.39,59.4,59.88,59.62,59.88,60.18,60.2,60.54,60.41,60.52,60.24,58.88,54.67,41.44])

    # print(vvsection.shape)
    # print(vaxsection.shape)
    # print(sssection.shape)
    # input('halt')
    # for i in range(1):
    #     lhegz_wash_to_ob_w(
    #         datafile='/store/4fermion/validation/1211/dataav%d.lhe'%(i+1),
    #         savename='cepc4fav/cepc4fav%d'%i,energy=240,xsection=vaxsection[i],
    #         cut=cut.cut_nocut,s=True,smearer=smear.smear_cepc_0
    #     )
    #     lhegz_wash_to_ob_w(
    #         datafile='/store/4fermion/validation/1211/datass%d.lhe'%(i+1),
    #         savename='cepc4fss/cepc4fss%d'%i,energy=240,xsection=sssection[i],
    #         cut=cut.cut_nocut,s=True,smearer=smear.smear_cepc_0
    #     )
    #     lhegz_wash_to_ob_w(
    #         datafile='/store/4fermion/datast%d.lhe'%(i+1),
    #         savename='cepc4fst/cepc4fst%d'%i,energy=240,xsection=stsection[i],
    #         cut=cut.cut_nocut,s=True,smearer=smear.smear_cepc_0
    #     )
    #     lhegz_wash_to_ob_w(
    #         datafile='/store/4fermion/datavv%d.lhe' % (i + 1),
    #         savename='cepc4fvv/cepc4fvv%d' % i, energy=240, xsection=vvsection[i],
    #         cut=cut.cut_nocut, s=True, smearer=smear.smear_cepc_0
        # )
    #
    #########################
    #


    ####### CEPC 4 operator data parser (Z pole mode).
    # zssx = np.array([5.328,5.379,5.418,5.447,5.446,5.443,5.427,5.391,5.33,5.247,5.101,4.848,4.476,3.894,3.029,1.832,0.469])
    # zstx = np.array([1.79,1.78,1.81,1.82,1.82,1.82,1.823,1.82,1.809,1.797,1.771,1.732,1.668,1.557,1.383,1.098,0.603])
    # zvvx = np.array([7.212,7.23,7.253,7.278,7.261,7.29,7.309,7.311,7.355,7.35,7.375,7.372,7.353,7.254,7.03,6.339,4.194])
    # zavx = np.array([7.032,7.22,7.247,7.228,7.249,7.236,7.208,7.165,7.107,7.000,6.773,6.465,5.943,5.174,4.026,2.441,0.626])
    # print(zstx.shape,zavx.shape,zvvx.shape)
    # print(zstx)
    # input('halt')

    # print(vvsection.shape)
    # print(vaxsection.shape)
    # print(sssection.shape):wq
    # input('halt')
    # for i in range(1):
    #     lhegz_wash_to_ob_w(
    #         datafile='/store/4fermion/cepc4fzav%d.lhe'%(i+1),
    #         savename='cepc4fav/cepc4fzav%d'%i,energy=91.2,xsection=zavx[i],
    #         cut=cut.cut_nocut,s=True,smearer=smear.smear_cepc_0
    #     )
    #     lhegz_wash_to_ob_w(
    #         datafile='/store/4fermion/cepc4fzvv%d.lhe'%(i+1),
    #         savename='cepc4fvv/cepc4fzvv%d'%i,energy=91.2,xsection=zvvx[i],
    #         cut=cut.cut_nocut,s=True,smearer=smear.smear_cepc_0
    #     )
    #     lhegz_wash_to_ob_w(
    #         datafile='/store/4fermion/cepc4f/zss/cepc4fzss%d.lhe'%(i+1),
    #         savename='cepc4fss/cepc4fzss%d'%i,energy=91.2,xsection=zssx[i],
    #         cut=cut.cut_nocut,s=True,smearer=smear.smear_cepc_0
    #     )
    #     lhegz_wash_to_ob_w(
    #         datafile='/store/4fermion/cepc4f/zst/cepc4fzst%d.lhe' % (i + 1),
    #         savename='cepc4fst/cepc4fzst%d' % i, energy=91.2, xsection=zstx[i],
    #         cut=cut.cut_nocut, s=True, smearer=smear.smear_cepc_0
    # )

    ########################

    ####### CEPC 4 operator data parser (W pole mode).
    # wssx = np.array(
    #     [18.35,18.41,18.42,18.51,18.56,18.46,18.55,18.54,18.49,18.45,18.23,18.05,17.67,17.04,
    #      15.96,14.34,11.89,8.301,3.726,0.0079])
    # wstx = np.array(
    #     [6.113,6.149,6.152,6.13,6.165,6.19,6.188,6.219,6.184,6.21,6.179,6.159,6.107,5.997,5.814,5.53,5.504,4.284,2.995,0.203])
    # wvvx = np.array(
    #     [24.33,24.54,24.42,24.48,24.60,24.57,24.62,24.63,24.49,
    #      24.48,24.35,24.04,23.52,22.61,21.25,19.09,15.81,11.09,4.97,0.01])
    # wavx = np.array(
    #     [24.45,24.39,24.53,24.5,24.57,24.68,24.73,24.81,24.88,24.79,24.97,25.07,25.13,25.18,25.19,25.02,24.57,23.18,18.97,1.616])
    #
    # # print(wssx.shape,wstx.shape, wavx.shape, wvvx.shape)
    # # print(wvvx)
    #
    # for i in range(17,20):
    #     lhegz_wash_to_ob_w(
    #         datafile='/store/4fermion/cepc4fwav%d.lhe' % (i + 1),
    #         savename='cepc4fav/cepc4fwav%d2' % i, energy=160, xsection=wavx[i],
    #         cut=cut.cut_nocut, s=True, smearer=smear.smear_cepc_0
    #     )
    #     lhegz_wash_to_ob_w(
    #         datafile='/store/4fermion/cepc4fwvv%d.lhe' % (i + 1),
    #         savename='cepc4fvv/cepc4fwvv%d2' % i, energy=160, xsection=wvvx[i],
    #         cut=cut.cut_nocut, s=True, smearer=smear.smear_cepc_0
    #     )
    #     lhegz_wash_to_ob_w(
    #         datafile='/store/4fermion/cepc4f/wss/cepc4fss%d.lhe' % (i + 1),
    #         savename='cepc4fss/cepc4fwss%d2' % i, energy=160, xsection=wssx[i],
    #         cut=cut.cut_nocut, s=True, smearer=smear.smear_cepc_0
    #     )
    #     lhegz_wash_to_ob_w(
    #         datafile='/store/4fermion/cepc4f/wst/cepc4fst%d.lhe' % (i + 1),
    #         savename='cepc4fst/cepc4fwst%d2' % i, energy=160, xsection=wstx[i],
    #         cut=cut.cut_nocut, s=True, smearer=smear.smear_cepc_0
    #     )

    ########################


    ################################
    # CEPC constraints on dark photon model by all 3 configurations.
    # \epsilon = 0.01, m_\text{z'}=150 GeV.

    # dfzx = np.array([0.005295,0.005297,0.00531,0.005337,0.005328,
    #         0.005351,0.005356,0.005374,0.005374,
    #                  0.005385,0.005413,0.005412,0.005407,0.005351,0.005189,0.004731])
    # dfwx = np.array([1.293,1.293,1.292,1.292,1.292,1.292,1.292,
    #                  1.292,1.292,1.291,1.293,1.292,1.293,1.291,1.291,1.29,1.288,1.28,1.259,0.029])
    # dfhx = np.array([
    #     0.06395,0.063980,0.06393,0.06393,0.06379,0.06398,0.06403,0.06382,0.06392,0.06394,
    #     0.0639,0.06399,0.0641,0.06399,0.06388,0.06402,0.06394,0.06382,0.06343,0.01111,0.006292
    # ])

    # input('halt')

    # for i in range(21):
        # lhegz_wash_to_ob_w(
        #     datafile='/store/darkphoton/cepcdfh%d.lhe' % (i + 1),
        #     savename='darkphoton/cepcdfh%d' % i, energy=240, xsection=dfhx[i],
        #     cut=cut.cut_nocut, s=True, smearer=smear.smear_cepc_0
        # )
        # data = np.load('/store/disposed/darkphoton/cepcdfh%dd.npy'%i)
        # data[:,-1] = (dfhx[i]/data.shape[0])*np.ones_like(data[:,-1])
        # np.save('/store/disposed/darkphoton/cepcdfh%dd.npy'%i,data)
        # if i !=20:
            # lhegz_wash_to_ob_w(
            #     datafile='/store/darkphoton/cepcdfw%d.lhe' % (i + 1),
            #     savename='darkphoton/cepcdfw%d' % i, energy=160, xsection=dfwx[i],
            #     cut=cut.cut_nocut, s=True, smearer=smear.smear_cepc_0
            # )
            # data = np.load('/store/disposed/darkphoton/cepcdfw%dd.npy' % i)
            # data[:, -1] = (dfwx[i]/data.shape[0])* np.ones_like(data[:, -1])
            # np.save('/store/disposed/darkphoton/cepcdfw%dd.npy' % i, data)
        # if i < 16:
        #     lhegz_wash_to_ob_w(
            #     datafile='/store/darkphoton/cepcdfz%d.lhe' % (i + 1),
            #     savename='darkphoton/cepcdfz%d' % i, energy=91.2, xsection=dfzx[i],
            #     cut=cut.cut_nocut, s=True, smearer=smear.smear_cepc_0
            # )
            # data = np.load('/store/disposed/darkphoton/cepcdfz%dd.npy' % i)
            # data[:, -1] = (dfzx[i]/data.shape[0]) * np.ones_like(data[:, -1])
            # np.save('/store/disposed/darkphoton/cepcdfz%dd.npy' % i, data)



    ###############################
    ###########################
    # for i in range(101):
    #     print(i)
    #     lhegz_wash_to_ob(datafile='/store/mldataset/xxee100/%d.lhe'%i,cut=cut.cut_cepc_basicadvacncd,
    #                  savename='mlxxee%d'%i,s=True,cepc=True)
    # washer(datafile="/store/eeeea/ee18.dat",savename="ee18",cut=cut.cut_besiii_4)
    # washer_with_weight(datafile="/store/eeeea/ee18.dat",weightfile="/store/eeeea/ee18w.dat",savename="ee18")
    # washer_inhomogenous(datafile='/store/eeeea/ee19.csv',cut=cut.cut_normal,savename='ee19_2')
    # test = np.load("data/pqed250GeV2939withob.npy")
    # print(test[0])
    # print(test.shape)
    # for i in range(test.shape[0]):
    #     if (test[i][0]+test[i][4]+test[i][8])-250>1e-8:
    #         print("Bing!")
    #     if (test[i][1]+test[i][5]+test[i][9])>1e-8:
    #         print("Bing!")
    #     if (test[i][2]+test[i][6]+test[i][10])>1e-8:
    #         print("Bing!")
    #     if (test[i][3]+test[i][7]+test[i][11])>1e-8:
    #         print("Bing!")

    ####################################
    ####################################
    # # Dark photon
    # lhegz_wash_to_ob_w(datafile='/store/visibledecay/bgmg5.lhe',
    #                    cut=cut.cut_nocut,energy=240,savename='dfvisiblebgmg5',
    #                    xsection=1.777,s=True,smearer=smear.smear_cepc_0)
    # fcoutput_to_ob_w_general(datafile='/store/visibledecay/fcruns/bgf.dat',weightfile='/store/visibledecay/fcruns/bgfw.dat',
    #                          cut=cut.cut_nocut,s=True,smearer=smear.smear_cepc_0,energy=240,savename='dfbgf')
    # a = general_dat_parser('/store/visibledecay/fcruns/massz/mom0.000125.dat')
    # print(np.sum(a[:,0]),np.sum(a[:,1]),np.sum(a[:,2]))
    #######################################
    ## Dark photon visible decay FC
    # for i in [177,250,354,500,707,1000]:
    #     if i >= 1000:
    #         fcoutput_to_ob_w_general_multichannel(datafile='/store/visibledecay/fcruns/massz/mom0.00%d.dat' % i,
    #                                               weightfile='/store/visibledecay/fcruns/massz/weight0.00%d.dat'%i,
    #                                               cut=cut.cut_nocut, s=True, smearer=smear.smear_cepc_0,
    #                                               energy=240, savename='dfmzg%dnp' % i,channels=[1,2])
    #     else:
    #         fcoutput_to_ob_w_general_multichannel(datafile='/store/visibledecay/fcruns/massz/mom0.000%d.dat'%i,
    #                                               weightfile='/store/visibledecay/fcruns/massz/weight0.000%d.dat'%i,
    #                                               cut=cut.cut_nocut,s=True,smearer=smear.smear_cepc_0,
    #                                               energy=240,savename='dfmzg%dnp'%i,channels=[1,2])
    #     os.system('mv /store/disposed/dfmzg%dnpd.npy /store/disposed/visibledecay/massz/'%i)



    # print(os.listdir('/store/visibledecay/fcruns/mass150/'))
    # datalist = os.listdir('/store/visibledecay/fcruns/mass150/')
    # datapair = {}
    # for filename in datalist:
    #     if 'mom' in filename:
    #         datapair[filename] = 'weight'+filename[3:]
    # # print(datapair['mom0.004419.dat'])
    # for filename in datapair.keys():
    #     couple = float(pattern_2.findall(filename)[0])
    #     print(couple)
    #
    #     # input('halt')
    #     fcoutput_to_ob_w_general_multichannel(datafile='/store/visibledecay/fcruns/mass150/'+filename,
    #                                                   weightfile='/store/visibledecay/fcruns/mass150/'+datapair[filename],
    #                                                   cut=cut.cut_nocut, s=True, smearer=smear.smear_cepc_0,
    #                                                   energy=240, savename='dfm150g%fnp_pure'%couple,channels=[1])
    #     fcoutput_to_ob_w_general_multichannel(datafile='/store/visibledecay/fcruns/mass150/'+filename,
    #                                                   weightfile='/store/visibledecay/fcruns/mass150/'+datapair[filename],
    #                                                   cut=cut.cut_nocut, s=True, smearer=smear.smear_cepc_0,
    #                                                   energy=240, savename='dfm150g%fnp_int'%couple,channels=[2])

    # os.system('mkdir /store/disposed/visibledecay/mass150')
    # os.system('mv /store/disposed/dfm150* /store/disposed/visibledecay/mass150')
    # fcoutput_to_ob_w_general_multichannel(datafile='/store/visibledecay/dfbgz.dat',
    #                                               weightfile='/store/visibledecay/dfbfzw.dat',
    #                                               cut=cut.cut_nocut, s=True, smearer=smear.smear_cepc_0,
    #                                               energy=91.2, savename='dfbgz',channels=[0])

    # fcoutput_to_ob_w_general(datafile='/store/eeeea/ee240_107.dat',
    #                          weightfile='/store/eeeea/ee240_107w.dat',cut=cut.cut_12_cepc_0_irredu,
    #                          s=True,smearer=smear.smear_cepc_0,
    #                          energy=240,savename='ee240_107')
    # fcoutput_to_ob_w_general(datafile='/store/milliq/cepch/mqh132m0.1.dat',
    #                          weightfile='/store/milliq/cepch/mqh132m0.1w.dat',cut=cut.cut_12_cepc_0_irredu,
    #                          s=True,smearer=smear.smear_cepc_0,
    #                          energy=240,savename='milliq/cepch/mqh132m0.1')
    # fcoutput_to_ob_w_general(datafile='/store/milliq/cepcz/mqz132m0.1.dat',
    #                          weightfile='/store/milliq/cepcz/mqz132m0.1w.dat',cut=cut.cut_12_cepc_0_irredu,
    #                          s=True,smearer=smear.smear_cepc_0,
    #                          energy=91.2,savename='milliq/cepcz/mqz132m0.1')
    # fcoutput_to_ob_w_general(datafile='/store/milliq/cepcw/mq2132m0.1.dat',
    #                          weightfile='/store/milliq/cepcw/mqw132m0.1w.dat',cut=cut.cut_12_cepc_0_irredu,
    #                          s=True,smearer=smear.smear_cepc_0,
    #                          energy=160,savename='milliq/cepcw/mqw132m0.1')
    #
    #
    #
    # fcoutput_to_ob_w_general(datafile='/store/milliq/cepch/mqh132m0.5.dat',
    #                          weightfile='/store/milliq/cepch/mqh132m0.5w.dat',cut=cut.cut_12_cepc_0_irredu,
    #                          s=True,smearer=smear.smear_cepc_0,
    #                          energy=240,savename='milliq/cepch/mqh132m0.5')
    # fcoutput_to_ob_w_general(datafile='/store/milliq/cepcz/mqz132m0.5.dat',
    #                          weightfile='/store/milliq/cepcz/mqz132m0.5w.dat',cut=cut.cut_12_cepc_0_irredu,
    #                          s=True,smearer=smear.smear_cepc_0,
    #                          energy=91.2,savename='milliq/cepcz/mqz132m0.5')
    # fcoutput_to_ob_w_general(datafile='/store/milliq/cepcw/mqw132m0.5.dat',
    #                          weightfile='/store/milliq/cepcw/mqw132m0.5w.dat',cut=cut.cut_12_cepc_0_irredu,
    #                          s=True,smearer=smear.smear_cepc_0,
    #                          energy=160,savename='milliq/cepcw/mqw132m0.5')
    # fcoutput_to_ob_w_general(datafile='/store/milliq/cepch/mqh132m0.1_eta244.dat',
    #                              weightfile='/store/milliq/cepch/mqh132m0.1_eta244w.dat',cut=cut.cut_nocut,
    #                              s=True,smearer=smear.smear_cepc_0,
    #                              energy=240,savename='milliq/cepch/mqh132m0.1eta244')
    #
    #
    # fcoutput_to_ob_w_general(datafile='/store/milliq/cepch/mqh132m0.1_eta313.dat',
    #                              weightfile='/store/milliq/cepch/mqh132m0.1_eta313w.dat',cut=cut.cut_nocut,
    #                              s=True,smearer=smear.smear_cepc_0,
    #                              energy=240,savename='milliq/cepch/mqh132m0.1eta313')
    #
    #
    # fcoutput_to_ob_w_general(datafile='/store/milliq/cepch/mqh132m0.5_eta244.dat',
    #                              weightfile='/store/milliq/cepch/mqh132m0.5_eta244w.dat',cut=cut.cut_nocut,
    #                              s=True,smearer=smear.smear_cepc_0,
    #                              energy=240,savename='milliq/cepch/mqh132m0.5eta244')
    #
    #
    # fcoutput_to_ob_w_general(datafile='/store/milliq/cepch/mqh132m0.5_eta313.dat',
    #                              weightfile='/store/milliq/cepch/mqh132m0.5_eta313w.dat',cut=cut.cut_nocut,
    #                              s=True,smearer=smear.smear_cepc_0,
    #                              energy=240,savename='milliq/cepch/mqh132m0.5eta313')
    # dfhx_add = 1e-2*np.array([6.20,6.13,6.04,5.92,5.78,5.59,5.38,5.08,4.73,4.25,
    #                      3.61,2.65,1.53,1.14,1.00,0.92,0.86,0.80,0.74,0.68,0.63])
    # for i in range(1,22):
    #     lhegz_wash_to_ob_w(datafile='/store/darkphoton/cepcdfh%i_add.lhe'%i,
    #                        savename='darkphoton/cepcdfh%i_add'%i,
    #                        energy=240, xsection=dfhx_add[i-1],
    #                         cut=cut.cut_nocut, s=True, smearer=smear.smear_cepc_0
    #                        )
    # for i in range(1,6):
    #     lhegz_wash_to_ob_auto(datafile='/store/zprime/coupxlings%d_gvf001.lhe'%i,
    #                           savename='couplings%d_gvf001'%i,energy=240,
    #                           cut=cut.cut_nocut,s=True,smearer=smear.smear_cepc_0)
    # for i in range(1,6):
    #     lhegz_wash_to_ob_auto(datafile='/store/zprime/couplings%d2_gvxgvf001.lhe'%i,
    #                           savename='couplings%d2_gvxgvf001'%i,energy=240,
    #                           cut=cut.cut_nocut,s=True,smearer=smear.smear_cepc_0)
    # for i in range(1,4):
        # lhegz_wash_to_ob_auto(datafile='/store/zprime/couplings%d2_gvf001.lhe'%i,
        #                       savename='couplings%d_gvf001_2'%i,energy=240,
        #                       cut=cut.cut_nocut,s=True,smearer=smear.smear_cepc_0)
    # for i in range(1,52):
    #     lhegz_wash_to_ob_auto(datafile='/store/darkphoton/run2/cepcdfh%d2.lhe'%i,
    #                       savename='cepcdfh%d_run2'%i,energy=240,
    #                       cut=cut.cut_nocut,s=True,smearer=smear.smear_cepc_0)
    # for i in range(1,32):
    #     lhegz_wash_to_ob_auto(datafile='/store/zprime/run3/couplings%d_gvf_run3.lhe'%i,
    #                           savename='couplings_v_run3_%d'%i,energy=240,
    #                           cut=cut.cut_nocut,s=True,smearer=smear.smear_cepc_0)
    #     lhegz_wash_to_ob_auto(datafile='/store/zprime/run3/couplings%d_gvxgvf_run3.lhe'%i,
    #                           savename='couplings_iv_run3_%d'%i,energy=240,
    #                           cut=cut.cut_nocut,s=True,smearer=smear.smear_cepc_0)
    # for i in range(1,201):
    #     lhegz_wash_to_ob_auto(datafile='/store/darkphoton2/mz150_mx%d_run5.lhe'%i,
    #                           savename='cepcdfh_iv_mz150_mx%d_run5'%i,energy=240,
    #                           cut=cut.cut_nocut,s=True,smearer=smear.smear_cepc_0)
    # lhegz_wash_to_ob_auto(datafile='/store/darkphoton2/run5_add.lhe',
    #                       savename='run5_add2',energy=240,
    #                       cut=cut.cut_nocut,s=False,smearer=smear.smear_cepc_0)

    # lhegz_wash_to_muob_auto(datafile='/store/darkphoton2/mz150mx50_visible_muon2.lhe',savename='muonparsertest',energy=240,
    #                         cut=cut.cut_cepc_mu_pre,s=True,smearer=smear.smear_cepc_mu)
    # fcoutput_to_ob_w_general(datafile='/store/finalpush/zprimem50mom.dat',
    #                              weightfile='/store/finalpush/zprimem50weight.dat',cut=cut.cut_nocut,
    #                              s=True,smearer=smear.smear_cepc_0,
    #                              energy=240,savename='zp132m50')
    # lhegz_wash_to_ob_auto(datafile='/store/4fermion/vvm50add.lhe',
    #                       savename='vvmx50add',energy=240,
    #                       cut=cut.cut_nocut,s=False,smearer=smear.smear_cepc_0)
    # lhegz_wash_to_ob_auto(datafile='/store/darkphoton2/bg_invisible.lhe',
    #                                savename = 'bg_invisible',energy=240,
    #                       cut = cut.cut_nocut,s=True,smearer=smear.smear_cepc_0)
    # lhegz_wash_to_muob_auto(datafile='/store/darkphoton2/bg_invisible.lhe',
    #                                savename = 'bg_invisible',energy=240,
    #                       cut = cut.cut_nocut,s=True,smearer=smear.smear_cepc_mu)
    # fcoutput_to_ob_w_general(datafile='/store/darkphoton2/visiblebg.dat',weightfile='/store/darkphoton2/visiblebg_weight.dat',\
    #                          savename='darkphoton_visiblebg_mumua',cut=cut.cut_nocut,s=True,smearer=smear.smear_cepc_0,energy=240)