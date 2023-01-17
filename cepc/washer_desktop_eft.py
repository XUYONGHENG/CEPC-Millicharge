import washer_new as washer
import cut as cut


if __name__ == '__main__':
    # for i in range(52,101):
    #     washer.fcoutput_to_ob_w_general(datafile='/store/finalpush/4fermion/av/h/ssm%d.dat'%i,
    #                             weightfile='/store/finalpush/4fermion/av/h/ssm%dw.dat'%i,
    #                             cut = cut.cut_nocut,savename='finalpush/4fermion/av/h/av%d'%i,energy=240)
    # for i in range(21):
    #     washer.fcoutput_to_ob_w_general(datafile='/store/finalpush/4fermion/st/h/stm%d.dat'%i,
    #                             weightfile='/store/finalpush/4fermion/st/h/sstm%dw.dat'%i,
    #                             cut = cut.cut_nocut,savename='finalpush/4fermion/st/h/st%d'%i,energy=240)
    # for i in range(100):
    #     washer.fcoutput_to_ob_w_general(datafile='/store/finalpush/4fermion/av/h/ssm%d.dat'%(i+1),
    #                             weightfile='/store/finalpush/4fermion/av/h/ssm%dw.dat'%(i+1),
    #                             cut = cut.cut_nocut,savename='finalpush/4fermion/av/h/av%d'%i,energy=240)
    # for i in range(100):
    #     washer.fcoutput_to_ob_w_general(datafile='/store/finalpush/4fermion/vv/h/ssm%d.dat'%(i+1),
    #                             weightfile='/store/finalpush/4fermion/vv/h/ssm%dw.dat'%(i+1),
    #                             cut = cut.cut_nocut,savename='finalpush/4fermion/vv/h/vv%d'%i,energy=240)
    # for i in range(10,21):
    #     washer.fcoutput_to_ob_w_general(datafile='/store/finalpush/4fermion/st/h/stm%d.dat'%(i),
    #                             weightfile='/store/finalpush/4fermion/st/h/stm%dw.dat'%(i),
    #                             cut = cut.cut_nocut,savename='finalpush/4fermion/st/h/vv%d'%i,energy=240)
    # for i in range(21):
    #     washer.fcoutput_to_ob_w_general(datafile='/store/finalpush/4fermion/ss/h/ssm%d.dat' % i,
    #                                     weightfile='/store/finalpush/4fermion/ss/h/ssm%dw.dat' % i,
    #                                     cut=cut.cut_nocut, savename='finalpush/4fermion/ss/h/ss%d' % i, energy=240)
    # for i in range(21):
    #     washer.fcoutput_to_ob_w_general(datafile='/store/finalpush/4fermion/vv/h/vvm%d.dat' % i,
    #                                     weightfile='/store/finalpush/4fermion/vv/h/vvm%dw.dat' % i,
    #                                     cut=cut.cut_nocut, savename='finalpush/4fermion/vv/h/vv%d' % i, energy=240)
    # for i in range(19):
    #     washer.fcoutput_to_ob_w_general(datafile='/store/finalpush/4fermion/st/w/stm%d.dat' % i,
    #                                     weightfile='/store/finalpush/4fermion/st/w/stm%dw.dat' % i,
    #                                     cut=cut.cut_nocut, savename='finalpush/4fermion/st/w/st%d' % i, energy=160)
    # for i in range(19):
    #     washer.fcoutput_to_ob_w_general(datafile='/store/finalpush/4fermion/av/w/avm%d.dat' % i,
    #                                     weightfile='/store/finalpush/4fermion/av/w/avm%dw.dat' % i,
    #                                     cut=cut.cut_nocut, savename='finalpush/4fermion/av/w/av%d' % i, energy=160)
    # for i in range(19):
    #     washer.fcoutput_to_ob_w_general(datafile='/store/finalpush/4fermion/vv/w/vvm%d.dat' % i,
    #                                     weightfile='/store/finalpush/4fermion/vv/w/vvm%dw.dat' % i,
    #                                     cut=cut.cut_nocut, savename='finalpush/4fermion/vv/w/vv%d' % i, energy=160)
    # for i in range(19):
    #     washer.fcoutput_to_ob_w_general(datafile='/store/finalpush/4fermion/ss/w/ssm%d.dat' % i,
    #                                     weightfile='/store/finalpush/4fermion/ss/w/ssm%dw.dat' % i,
    #                                     cut=cut.cut_nocut, savename='finalpush/4fermion/ss/w/ss%d' % i, energy=160)
    # for i in range(11,19):
    #     washer.fcoutput_to_ob_w_general(datafile='/store/finalpush/4fermion/av/w/avm%d.dat' % i,
    #                                     weightfile='/store/finalpush/4fermion/av/w/avm%dw.dat' % i,
    #                                     cut=cut.cut_nocut, savename='finalpush/4fermion/av/w/av%d' % i, energy=160)
    # for i in range(17):
    #     washer.fcoutput_to_ob_w_general(datafile='/store/finalpush/4fermion/st/z/stm%d.dat' % i,
    #                                     weightfile='/store/finalpush/4fermion/st/z/stm%dw.dat' % i,
    #                                     cut=cut.cut_nocut, savename='finalpush/4fermion/st/z/st%d' % i, energy=91.2)
    # for i in range(11,17):
    #     washer.fcoutput_to_ob_w_general(datafile='/store/finalpush/4fermion/av/z/avm%d.dat' % i,
    #                                     weightfile='/store/finalpush/4fermion/av/z/avm%dw.dat' % i,
    #                                     cut=cut.cut_nocut, savename='finalpush/4fermion/av/z/av%d' % i, energy=91.2)
    # for i in range(17):
    #     washer.fcoutput_to_ob_w_general(datafile='/store/finalpush/4fermion/ss/z/ssm%d.dat' % i,
    #                                     weightfile='/store/finalpush/4fermion/ss/z/ssm%dw.dat' % i,
    #                                     cut=cut.cut_nocut, savename='finalpush/4fermion/ss/z/ss%d' % i, energy=91.2)
    for i in range(17):
        washer.fcoutput_to_ob_w_general(datafile='/store/finalpush/4fermion/vv/z/vvm%d.dat' % i,
                                        weightfile='/store/finalpush/4fermion/vv/z/vvm%dw.dat' % i,
                                        cut=cut.cut_nocut, savename='finalpush/4fermion/vv/z/vv%d' % i, energy=91.2)
