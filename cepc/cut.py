import numpy as np
from tools import *


### Applied in formal result
def cut_cepc_advance_disposed_5(p, mass):
    if p[0] > (240 ** 2 - 4 * mass ** 2) / (2 * 240):
        return False

    if 95 < p[0] < 110:
        return False

    if mass < 16:
        if p[0] < 110:
            return False

    if p[0] > 0.1 and np.abs(p[2]) < 0.989:
        if (240 - p[0]) / p[0] * 0.15 < np.sin(np.arccos(p[2])):
            return True

    return False


def cut_cepcw_advance_disposed(p, mass):
    if p[0] > (160 ** 2 - 4 * mass ** 2) / (2 * 160):
        return False

    if 50 < p[0] < 60:
        return False

    if mass < 30:
        if p[0] < 60:
            return False

    if p[0] > 0.1 and np.abs(p[2]) < 0.989:
        if (160 - p[0]) / p[0] * 0.15 < np.sin(np.arccos(p[2])):
            return True

    return False


def cut_cepcz_advance_disposed(p, mass):
    if p[0] > (91.2 ** 2 - 4 * mass ** 2) / (2 * 91.2):
        return False

    if p[0] > 0.1 and np.abs(p[2]) < 0.989:
        if (91.2 - p[0]) / p[0] * 0.15 < np.sin(np.arccos(p[2])):
            return True
    return False


def cut_cepc_advance_disposed_2_4f(p, mass):
    if p[0] > (240 ** 2 - 4 * mass ** 2) / (2 * 240):
        return False

    if 95 < p[0] < 110:
        return False


    if p[0] > 0.1 and np.abs(p[2]) < 0.989:
        if (240 - p[0]) / p[0] * 0.15 < np.sin(np.arccos(p[2])):
            return True
    return False


def cut_cepcw_advance_disposed_4f(p, mass):
    if p[0] > (160 ** 2 - 4 * mass ** 2) / (2 * 160):
        return False

    if 50 < p[0] < 60:
        return False

    
    if p[0] > 0.1 and np.abs(p[2]) < 0.989:
        if (160 - p[0]) / p[0] * 0.15 < np.sin(np.arccos(p[2])):
            return True

    return False



def cut_zp_iv_150_3(p,mx,**kwargs):
    if p[0] > (240 ** 2 - 4 * mx ** 2) / (2 * 240):
        return False

    if 95 < p[0] < 105:
        return False

    if mx <= 75:
        if not 147 < p[3] < 153:
            return False

    if p[0] > 0.1 and np.abs(p[2]) < 0.989:
        if (240-p[0])/p[0]*0.15 < np.sin(np.arccos(p[2])):
            return True

    return False


def cut_zp_iv_150_3w(p,mx,**kwargs):
    if p[0] > (160 ** 2 - 4 * mx ** 2) / (2 * 160):
        return False


    if p[0] > 50:
        return False


    if p[0] > 0.1 and np.abs(p[2]) < 0.989:
        if (160-p[0])/p[0]*0.15 < np.sin(np.arccos(p[2])):
            return True

    return False



def cut_zp_iv_150_3z(p,mx,**kwargs):
    if p[0] > (91.2 ** 2 - 4 * mx ** 2) / (2 * 91.2):
        return False


    if p[0] > 0.1 and np.abs(p[2]) < 0.989:
        if (91.2-p[0])/p[0]*0.15 < np.sin(np.arccos(p[2])):
            return True

    return False
#######


def cos_normal(p):
    return np.abs(p[3]/np.sqrt(p[1]**2+p[2]**2+p[3]**2))

def cut1(p):
    if p[10] > 10 and np.abs(p[-2]) < 0.94:
        if np.abs(p[3]) > 0.939 and np.abs(p[8]) > 0.939:
            return True
    return False

def cut2(p):
    if p[10] > 10 and np.abs(p[-2]) < 0.94:
        if np.abs(p[3]) > 0.984 and np.abs(p[8]) > 0.984:
            return True
    return False

def cut_besiii(p):
    if (np.abs(p[-2]) < 0.8 and p[10] > 0.025) or (0.86 < np.abs(p[-2]) < 0.92 and p[10] >0.05):
        if np.abs(p[3])>0.95 and np.abs(p[8])>0.95:
            return True
    return False

def cut_neutrino(p):
    if p[10] > 10 and np.abs(p[-2]) < 0.939:
        return True
    return False

def cut_3(p):
    if np.abs(p[3]) > 0.95 and np.abs(p[8]) > 0.95:
        return True
    return False

def cut_besiii_4(p):
    if (np.abs(p[-2]) < 0.8 and p[3] > 0.025) or (0.86 < np.abs(p[-2]) < 0.92 and p[3] >0.05):
        if np.abs(p[0])>0.95 and np.abs(p[1])>0.95:
            return True
    return False

def cut_neutrino_besiii_4(p):
    if (np.abs(p[-2]) < 0.8 and p[3] > 0.025) or (0.86 < np.abs(p[-2]) < 0.92 and p[3] >0.05):
        return True
    return False

def cut_normal(p):
    if np.abs(p[0]) > 0.95 and np.abs(p[1]) > 0.95:
        if p[-1] > 0.025 and np.abs(p[-2]) < 0.95:
            return True
    return False

def cut_one_collinear(p):
    if (np.abs(p[0])>0.995 and np.abs(p[1])>0.95) or (np.abs(p[1])>0.995 and np.abs(p[0])>0.95):
        if p[-1] > 0.025 and np.abs(p[-2]) < 0.95:
            return True
    return False

def cut_both_collinear(p):
    if np.abs(p[0]) > 0.995 and np.abs(p[1]) > 0.995:
        if p[-1] > 0.025 and np.abs(p[-2]) < 0.95:
            return True
    return False


# def cut_12_984(p):
#     photon being visible
    # if (np.abs(p[8]) > 10 and np.abs(cos_normal(p[8:]))) < 0.984:
    #     if (np.abs(cos_normal(p[:4])) > 0.984 or p[0] < 10) and (np.abs(cos_normal(p[4:] )) > 0.984 or p[4] < 10):
    #         return True
    # return False
def cut_12_1307_cut1(p):
    if not (p[8] > 10 and np.abs(cos_normal(p[8:])) < 0.9848):
        return False
    if not ((np.abs(cos_normal(p[4:])) > 0.9848 or p[4] < 10) and (np.abs(cos_normal(p[4:])) > 0.9986 or p[4] < 50)):
        return False
    if not ((np.abs(cos_normal(p[0:])) > 0.9848 or p[0] < 10) and (np.abs(cos_normal(p[0:])) > 0.9986 or p[0] < 50)):
        return False
    return True

def cut_12_1307_cut11(p):
    if not (p[8] > 10 and np.abs(cos_normal(p[8:])) < 0.9848):
        return False
    if not ((cos_normal(p[4:])) > 0.9848 and cos_normal(p[0:]) > 0.9848):
        return False
    return True


def cut_4_1307_cut2(p):
    if 50 < p[3] < 130:
        return False
    return True

def cut_4_1307_cut3(p):
    sqrt3 = np.sqrt(3)
    if np.abs(p[2]) > sqrt3/2:
        return False
    return True


def cut_4_1307_cut3_1(p):
    sqrt3 = np.sqrt(3)
    if np.abs(p[2]) > 0.985:
        return False
    return True


def cut_4_1307_cut4(p):
    if p[1] < 50:
        return False
    return True


def cut_12_photon(p):
    if p[8] > 10 and np.abs(cos_normal(p[8:])) < 0.984:
        return True
    return False


def cut_12_900(p):
    if p[8] > 10 and np.abs(cos_normal(p[8:])) < 0.984:
        if np.abs(cos_normal(p[4:])) > 0.9 and (np.abs(cos_normal(p))) > 0.9:
            return True
    return False

def cut_12_95(p):
    if p[8] > 10 and np.abs(cos_normal(p[8:])) < 0.984:
        if np.abs(cos_normal(p[4:])) > 0.9 and (np.abs(cos_normal(p))) > 0.9:
            return True
    return False

def cut_12_984(p):
    if p[8] > 10 and np.abs(cos_normal(p[8:])) < 0.984:
        if np.abs(cos_normal(p[4:])) > 0.984 and (np.abs(cos_normal(p))) > 0.984:
            return True
    return False

def cut_nocut(p):
    return True


def cut_denyall(p):
    return False


def cut_12_fuck(p):
    if p[8] > 10 and np.abs(cos_normal(p[8:])) < 0.984:
        if (p[0]<10 or np.abs(cos_normal(p[0:])) > 0.984) and (p[0] < 50 or np.abs(cos_normal(p[0:])) > 0.9986):
            if (p[4] < 10 or np.abs(cos_normal(p[4:])) > 0.984) and (p[4] < 50 or np.abs(cos_normal(p[4:])) > 0.9986):
                return True
    return False


def cut_12_fuck_2(p):
    if p[8] > 10 and np.abs(cos_normal(p[8:])) < 0.984:
        if (p[0] < 50 or np.abs(cos_normal(p[0:])) > 0.9986):
            if (p[4] < 50 or np.abs(cos_normal(p[4:])) > 0.9986):
                return True
    return False


def cut_12_sw(p):
    # photon being visible
    if (p[0] > 50 and np.abs(cos_normal(p)) < 0.9986) or (p[4] > 50 and np.abs(cos_normal(p[4:])) < 0.9986):
        return False
    return True
# test = np.array([ 2.07075480e+00,  1.57736434e+00,  4.95868874e-05,  1.34162110e+00,
#   2.06761612e+00, -1.60152912e+00, -4.95868874e-05, -1.30772355e+00,
#   4.16290839e-02,  2.41647857e-02,  0.00000000e+00 ,-3.38975480e-02])
#
# print(cut_12_984(test))
# print(test[0]+test[4]+test[8])
def cut_12_cepc_0_redu(p):
    if (p[0] < 1 or np.abs(cos_normal(p)) > 0.983) and (p[4] < 1 or np.abs(cos_normal(p[4:])) > 0.983):
        if p[8] > 1 and np.abs(cos_normal(p[8:])) < 0.983:
            return True
    return False

def cut_12_cepc_0_irredu(p):
    if p[8] > 0.1 and np.abs(cos_normal(p[8:])) < 0.989:
        return True
    return False

def cut_custom(p):
    if np.abs(np.cos(np.arcsin((240-p[8])/240))*0.15) < np.abs(cos_normal(p[8:])):
        return False

    return True

def cut_12_cepc_1_irredu(p):
    if p[8] > 0.1 and np.abs(cos_normal(p[8:])) < 0.989:
        return True
    return False




def cut_4_cepc_1_redu(p):
    if np.abs(p[0]) > 0.989 and np.abs(p[1]) > 0.989:
        if np.abs(p[2]) < 0.989 and p[3] > 0.1:
            return True
    return False




##Best so far for millicharged.
def cut_cepc_advance_disposed_2(p,mass):
    if p[0] > (240 ** 2 - 4 * mass ** 2) / (2 * 240):
        return False

    if mass < 16:
        # print('Bing!')
        # if 90< p[0] <110 or p[3] > 70:
        #########0.107
        # if p[0] < 60 or 90<p[0]<110 or 80< p[3] :
        if p[0] < 110:
        #########
        # if  p[0] < 60 or 90 < p[0] < 110:
            return False
    elif mass >= 16:
        # if 90< p[0] <110 or (110 > p[3] > 80):
        if 90<p[0]<110:
            return False


    if p[0] > 0.1 and np.abs(p[2]) < 0.989:
        if (240-p[0])/p[0]*0.15 < np.sin(np.arccos(p[2])):
            return True

    return False



def cut_cepc_advance_disposed_2_eta313(p,mass):
    if p[3] < 2*mass:
        return False

    if mass < 16:
        # print('Bing!')
        # if 90< p[0] <110 or p[3] > 70:
        #########0.107
        # if p[0] < 60 or 90<p[0]<110 or 80< p[3] :
        if p[0] < 110:
        #########
        # if  p[0] < 60 or 90 < p[0] < 110:
            return False
    elif 50 > mass > 16:
        # if 90< p[0] <110 or (110 > p[3] > 80):
        if 90<p[0]<110:
            return False

    elif mass > 50:
        # if 240 - 2*mass < p[0] or 90<p[0]<110 or (p[3] < 110):
        if 240 -2*mass<p[0] or 90 < p[0]:
            return False


    if p[0] > 0.1 and np.abs(p[2]) < 0.996:
        if (240-p[0])/p[0]*0.087 < np.sin(np.arccos(p[2])):
            return True
    return False


def cut_cepc_advance_disposed_2_eta313(p,mass):
    if p[3] < 2*mass:
        return False

    if mass < 16:
        # print('Bing!')
        # if 90< p[0] <110 or p[3] > 70:
        #########0.107
        # if p[0] < 60 or 90<p[0]<110 or 80< p[3] :
        if p[0] < 110:
        #########
        # if  p[0] < 60 or 90 < p[0] < 110:
            return False
    elif 50 > mass > 16:
        # if 90< p[0] <110 or (110 > p[3] > 80):
        if 90<p[0]<110:
            return False

    elif mass > 50:
        # if 240 - 2*mass < p[0] or 90<p[0]<110 or (p[3] < 110):
        if 240 -2*mass<p[0] or 90 < p[0]:
            return False


    if p[0] > 0.1 and np.abs(p[2]) < 0.984:
        if (240-p[0])/p[0]*0.173 < np.sin(np.arccos(p[2])):
            return True
    return False

# Duplicated cut2, with the advacned cut removed.
def cut_cepc_advance_disposed_2p(p,mass):
    if p[3] < 2*mass:
        return False

    if mass < 16:
        # print('Bing!')
        # if 90< p[0] <110 or p[3] > 70:
        #########0.107
        if p[0] < 60 or 90<p[0]<110 or 80< p[3] :
        #########
        # if  p[0] < 60 or 90 < p[0] < 110:
            return False
    elif 50 > mass > 16:
        if 90< p[0] <110 or (110 > p[3] > 80):
            return False
    elif mass > 50:
        if 240 - 2*mass < p[0] or 90<p[0]<110 or (p[3] < 110):
            return False

    return False







def cut_cepc_advance_disposed_3(p,mass):
    if p[3] < 2*mass:
        return False

    if mass < 16:
        # print('Bing!')
        # if 90< p[0] <110 or p[3] > 70:
        #########0.107
        if p[0] < 60 or 90<p[0]<110 or 80 < p[3] :
        #########
        # if  p[0] < 60 or 90 < p[0] < 110:
            return False
    elif 50 > mass > 16:
        if 90< p[0] <110 or (110 > p[3] > 80):
            return False
    elif mass > 50:
        if 240 - 2*mass < p[0] or 90<p[0]<110:
            return False

    if p[0] > 0.1 and np.abs(p[2]) < 0.989:
        if (240-p[0])/p[0]*0.15 < np.sin(np.arccos(p[2])):
            return True
    return False


def cut_cepc_advance_disposed_4(p,mass):
    if p[3] < 2*mass:
        return False

    if mass < 16:
        # print('Bing!')
        # if 90< p[0] <110 or p[3] > 70:
        #########0.107
        if p[0] < 60 or 90<p[0]<110 or 80< p[3] :
        # if p[0] < 110:
        #########
        # if  p[0] < 60 or 90 < p[0] < 110:
            return False
    elif 50 > mass > 16:
        if 90< p[0] <110 or (110 > p[3] > 80):
            return False
    elif mass > 50:
        if 240 - 2*mass < p[0] or 90<p[0]<110 or (p[3] < 110):
            return False

    if p[0] > 0.1 and np.abs(p[2]) < 0.985:
        if (240-p[0])/p[0]*0.173 < np.sin(np.arccos(p[2])):
            return True
    return False




# def cut_cepc_advacne_dispose_4f(p,mass):
#     if p[0] < 240-2*mass:
#         return False
#
#     if




def cut_cepc_basicadvacncd(p,**kwargs):
    if p[0] > 0.1 and np.abs(p[2]) < 0.989:
        if (240-p[0])/p[0]*0.15 < np.sin(np.arccos(p[2])):
            return True
    return False


def cut_cepcz_basicadvacncd(p):
    if p[0] > 0.1 and np.abs(p[2]) < 0.989:
        if np.abs(np.cos(np.arcsin((91.2-p[0])/91.2))*0.15) > np.abs(p[2]):
            return True
    return False





def cut_cepcz_advance_disposed_4f(p,mass):
    if p[0] > 91.2-2*mass:
        return False

    if p[0] > 0.1 and np.abs(p[2]) < 0.989:
        if (91.2-p[0])/p[0]*0.15 < np.sin(np.arccos(p[2])):
            return True
    return False


def cut_cepcw_advance_disposed_4f(p,mass):
    if p[0] > (160**2-4*(mass**2))/320:
        return False

    if  45 < p[0] < 65:
        return False

    if p[0] > 0.1 and np.abs(p[2]) < 0.989:
        if (160-p[0])/p[0]*0.15 < np.sin(np.arccos(p[2])):
            return True
    return False






## Basic ILC detector cut set that ensures the event will be seen by the ILD.
def cut_ilc_12_basic(p):
    if pt_gamma_xx(p) >= 10 and np.abs(pseudo_rapidity(p)) <= 2.5:
        return True
    return False

## Advanced ILC detector cut set.

def cut_ilc_disposed_0(p,mass):
    if p[1] < 20:        return False

    if mass < 20:
        if p[0]< 100 or 225<p[0] < 245:
            return False
    elif 20<mass<40:
        if p[0] > 230 or p[0] < 100:
            return False
    else:
        if p[0] > (300-mass) or p[0] < 80:
            return False

    return True



def cut_ilc_1211val(p,mass):

    if 100 <p[0]<112.5:
        return False

    if p[0] < 8 or np.abs(p[2])>0.995:
        return False

    return True


def cut_ilc_1211val_500(p,mass):

    if 237.5 <p[0]<245:
        return False

    if p[0] < 8 or np.abs(p[2])>0.995:
        return False

    return True


def cut_cepc_darkphoton_h(p,mass):
    ## Removing Z recoil in the irreducible BG>
    if 95 < p[0] < 105:
        return False


    ## Select the Z' recoil in the signal when there is one.
    if mass <50:
        if not 60<p[0]<85:
            return False
    else:
        if p[0] > 240-2*mass:
            return False

    ## Advanced cut set getting rid of reducible BG.
    if p[0] > 0.1 and np.abs(p[2]) < 0.989:
        if (240-p[0])/p[0]*0.15 < np.sin(np.arccos(p[2])):
            return True

    return False



def cut_cepc_darkphoton_w(p, mass):
    if p[0]>30:
        return False

    if p[0] > 0.1 and np.abs(p[2]) < 0.989:
        if (160 - p[0]) / p[0] * 0.15 < np.sin(np.arccos(p[2])):
            return True

    return False


def cut_cepc_darkphoton_z(p, mass):

    if p[0] > 0.1 and np.abs(p[2]) < 0.989:
        if (91.2 - p[0]) / p[0] * 0.15 < np.sin(np.arccos(p[2])):
            return True

    return False

def cut_wlt(p,mass):

    if p[0] > 0.1 and np.abs(p[2]) < 0.989:
        if (mass-2) < p[3] < (mass+2):
            return True

    return False


def cut_zp_iv_150_50(p,mx,**kwargs):
    if 95 < p[0] < 105:
        return False

    if mx<=50:
        if not (60<p[0]<85):
            return False
    else:
        if p[0] > (240**2 - 4*mx**2)/2*240:
            return False

    if p[0] > 0.1 and np.abs(p[2]) < 0.989:
        if (240-p[0])/p[0]*0.15 < np.sin(np.arccos(p[2])):
            return True
    return False


def cut_zp_iv_150_2(p,mx,**kwargs):
    if 95 < p[0] < 105:
        return False

    if mx <= 75:
        if not 147< p[3] < 153:
            return False
    elif mx > 75:
        if p[0] > (240 ** 2 - 4 * mx ** 2) / (2 * 240):
            return False

    if p[0] > 0.1 and np.abs(p[2]) < 0.989:
        if (240-p[0])/p[0]*0.15 < np.sin(np.arccos(p[2])):
            return True

    return False


def cut_zp_v_150_50(p,mzp,**kwargs):
    if p[0] > 0.1 and np.abs(p[2]) < 0.989:
        if  (mzp-0.5)< p[3] < (mzp+0.5):
            return True

    return False



def cut_cepc_mu_pre(p):
    print(pt(p[:4]))
    if pt(p[:4]) < 3 or pt(p[4:8])<3:
        return False
    return True