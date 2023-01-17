import re as re

pattern_0 = re.compile(r'\D\d+\.\d+e\D\d{2}',re.I)
pattern_1 = re.compile(r'\D*\d')
pattern_2 = re.compile(r'\d+.\d+')


pattern_lhco_beginning = re.compile(r'^0',re.I)
pattern_lhco_gflag = re.compile(r'^1, 0', re.I)
pattern_lhco_g2flag = re.compile(r'^1, 0', re.I)
pattern_lhco_mu1flag = re.compile(r'^2, 2', re.I)
pattern_lhco_mu2flag = re.compile(r'^3, 2', re.I)
pattern_lhco_mu3flag = re.compile(r'^4, 2', re.I)
pattern_lhco_gdata = re.compile(r'-*\d+\.\d+',re.I)
pattern_lhco_missing = re.compile(r'^4, 6', re.I)


pattern_gamma = re.compile(r'22',re.I)
pattern_chi = re.compile(r'\s5000521',re.I)
pattern_chibar = re.compile(r'-5000521',re.I)
pattern_mu = re.compile(r'13',re.I)
pattern_mubar = re.compile(r'-13',re.I)