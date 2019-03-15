
from parse_cdp import parse_cdp_neighbors

def dict_add(dict, file):
    for key, value in (parse_cdp_neighbors(file).items()):
        dict[key] = value
cdp = {}
dict_add(cdp, 'sh_cdp_n_r1.txt')
dict_add(cdp, 'sh_cdp_n_r2.txt')
dict_add(cdp, 'sh_cdp_n_r3.txt')
dict_add(cdp, 'sh_cdp_n_sw1.txt')


print (cdp)



























