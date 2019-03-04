from sys import argv
cfg = argv[1]
with open(cfg, 'r') as f:
    list = []
    for line in f:
        if '.' in line:
            list.append(line.rstrip().replace(' DYNAMIC    ', ''))
    list.sort()
    for i in list:
        print (i)
























