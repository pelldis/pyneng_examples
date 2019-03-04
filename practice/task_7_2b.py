from sys import argv
cfg = argv[1]
ignore = ['duplex', 'alias', 'Current configuration']
with open(cfg, 'r') as f:
   with open('config_sw1_cleared.txt','w') as new_f: 
        for line in f:
            if ignore[0] not in line and ignore[1] not in line and ignore[2] not in line:
                new_f.write(line)


































