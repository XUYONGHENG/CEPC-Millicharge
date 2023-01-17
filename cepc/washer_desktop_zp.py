import washer_new as washer
import cut as cut
import smearer as smear


if __name__ == '__main__':
    # for i in range(1,201):
    #     washer.lhegz_wash_to_ob_auto(datafile='/store/finalpush/darkphoton/h/mz150a_mx%d_50-100.lhe'%i,
    #                                  energy=240,savename='finalpush/zp/h/a/mz150a_mx%d_50-100.lhe'%i,
    #                                  s=True,smearer=smear.smear_cepc_0,cut=cut.cut_nocut)
    #     washer.lhegz_wash_to_ob_auto(datafile='/store/finalpush/darkphoton/h/mz150v_mx%d_50-100.lhe'%i,
    #                                  energy=240,savename='finalpush/zp/h/v/mz150v_mx%d_50-100.lhe'%i,
    #                                  s=True, smearer=smear.smear_cepc_0,cut=cut.cut_nocut)
    # for i in range(9):
    #     washer.lhegz_wash_to_ob_auto(datafile='/store/finalpush/darkphoton/h/mz150a_mx%d_1-50.lhe'%(i+1),\
    #                                  energy=240,savename='finalpush/zp/h/a/mz150a_mx%d_1-50'%(i+1),s=True,\
    #                                  smearer=smear.smear_cepc_0,cut=cut.cut_nocut)
    #     washer.lhegz_wash_to_ob_auto(datafile='/store/finalpush/darkphoton/h/mz150v_mx%d_1-50.lhe'%(i+1),\
    #                                  energy=240,savename='finalpush/zp/h/v/mz150v_mx%d_1-50'%(i+1),s=True,\
    #                                  smearer=smear.smear_cepc_0,cut=cut.cut_nocut)
    # for i in range(15):
    #     washer.lhegz_wash_to_ob_auto(datafile='/store/finalpush/darkphoton/w/mzw150a_mx%d_1-70.lhe'%(i+1),\
    #                                  energy=240,savename='finalpush/zp/w/a/mzw150a_mx%d_1-70'%(i+1),s=True,\
    #                                  smearer=smear.smear_cepc_0,cut=cut.cut_nocut)
    #     washer.lhegz_wash_to_ob_auto(datafile='/store/finalpush/darkphoton/w/mzw150v_mx%d_50-100.lhe'%(i+1),\
    #                                  energy=240,savename='finalpush/zp/w/v/mzw150v_mx%d_1-70'%(i+1),s=True,\
    #                                  smearer=smear.smear_cepc_0,cut=cut.cut_nocut)
    for i in range(9):
        washer.lhegz_wash_to_ob_auto(datafile='/store/finalpush/darkphoton/z/a/mzz150a_mx%d_1-40.lhe'%(i+1),\
                                     energy=240,savename='finalpush/zp/z/a/mzz150a_mx%d_1-40'%(i+1),s=True,\
                                     smearer=smear.smear_cepc_0,cut=cut.cut_nocut)
        washer.lhegz_wash_to_ob_auto(datafile='/store/finalpush/darkphoton/z/v/mzz150v_mx%d_1-40.lhe'%(i+1),\
                                     energy=240,savename='finalpush/zp/z/v/mzz150v_mx%d_1-50'%(i+1),s=True,\
                                     smearer=smear.smear_cepc_0,cut=cut.cut_nocut)
