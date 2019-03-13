ignore = ['duplex', 'alias', 'Current configuration']
def ignore_command(command, ignore):
    return any(word in command for word in ignore)
def get_dict(cfg):
    cfg_dict = {}
    with open(cfg) as f:
        for line in f:
            if '!' not in line and not ignore_command(line, ignore):
                if line.startswith('  '):
                    if len(lvl3) == 0:
                        cfg_dict[lvl1] = {i:[] for i in cfg_dict[lvl1]}
                        lvl3 = (line.strip('\n'))
                        cfg_dict[lvl1][lvl2].append(lvl3)
                    else:
                        lvl3 = (line.strip('\n'))
                        cfg_dict[lvl1][lvl2].append(lvl3)
                elif line.startswith(' '):
                    lvl2 = (line.strip('\n'))
                    cfg_dict[lvl1].append(lvl2)
                else:
                    lvl1 = line.strip('\n')
                    cfg_dict[lvl1] = []
                    lvl2 = []
                    lvl3 = []
    return cfg_dict
print (get_dict('config_r1.txt'))















































