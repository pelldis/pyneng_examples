ignore = ['duplex', 'alias', 'Current configuration']
def ignore_command(command, ignore):
    return any(word in command for word in ignore)
def get_dict(cfg):
    cfg_dict = {}
    with open(cfg) as f:
        for line in f:
            if '!' not in line and not ignore_command(line, ignore):
                if line.startswith(' '):
                    cfg_dict[gl].append(line.strip('\n'))
                else:
                    gl = line.strip('\n')
                    cfg_dict[gl] = []
    return cfg_dict
print (get_dict('config_sw1.txt'))













































