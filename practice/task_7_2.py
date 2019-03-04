from sys import argv
cfg = argv[1]
with open(cfg, 'r') as f:
    for line in f:
        if '!' not in line:
            print (line.rstrip())



































