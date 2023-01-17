import numpy as np
import cut as cut
import tools as tools
import smearer as smear

def sigma0(gvf,gvx,sigmat):
    return sigmat*(18*gvf**2 + 0.745*gvx**2)/(0.745*(gvf**2)*gvx**2)


def sigma0_v(gvf,gvx,sigmat):
    return sigmat*(18*gvf**2 + 0.745*gvx**2)/gvf**4


def sigma_extract(data,cut,mx,mzp):
    # print(np.sum(data[:,-1]))
    data[:,-1] = (128/137)**2*data[:,-1]
    originalxsection = np.sum(data[:,-1])
    sxsection = 0
    for i in range(data.shape[0]):
        if cut(p=data[i],mx=mx,mzp=mzp):
            sxsection += data[i,-1]
    efficiency = sxsection/originalxsection
    return sxsection,efficiency,originalxsection


if __name__ == '__main__':
    gvf = 0.01
    gvxs = 10**np.linspace(-3,0,31)
    print(gvxs)
    b, a = np.load('/store/disposed/vmvmcepc3d.npy'), np.load('/store/disposed/vevecepc3d.npy')
    b[:, -1] = 2 * b[:, -1]
    ivbg = np.vstack((a, b))
    print(ivbg.shape)
    bgxsection = sigma_extract(data=ivbg,cut=cut.cut_zp_iv_150_2,mx=50,mzp=150)
    print(bgxsection,'ivbgxsection')
    bgvxsection = sigma_extract(data=np.load('/store/disposed/dfbgd.npy'),cut=cut.cut_zp_v_150_50,mx=50,mzp=150)
    print(bgvxsection,'vbgxesction')

    visiblemuon = np.load('/store/disposed/muon2_2d.npy')
    # for i in range(visiblemuon.shape[0]):
    #     visiblemuon[i,-2] = smear.after_smear_m(visiblemuon[i,-2])
    # input('!')
    print(sigma_extract(data=visiblemuon,cut=cut.cut_zp_v_150_50,mx=50,mzp=150))
    input('halt')
    for i in range(31):
        sxsection,effciency,ori = sigma_extract(data=np.load('/store/disposed/cepcdfh_run4/cepcdfh_iv_mx_%d_run4d.npy'%(i+1)),
                  cut = cut.cut_zp_iv_150_2,mx=50,mzp=150)
        print(i,sigma0(gvf=gvf,gvx=gvxs[i],sigmat=ori),sxsection,effciency,ori,tools.total_decay_width(mzp=150,mx=50,gvf=gvf,gvx=gvxs[i]))
        # sxsection,efficiency,ori = sigma_extract(data=np.load('/store/disposed/couplings/couplings_v_run3_%dd.npy'%(i+1)),
        #
        #                                          cut=cut.cut_zp_v_150_50,mx=50,mzp=150)
        # print(sigma0_v(gvf=gvf,gvx=gvxs[i],sigmat=sxsection),efficiency,ori,tools.total_decay_width(mzp=150,mx=50,gvf=gvf,gvx=gvxs[i]))
