from sys import argv
cfg = argv[1]
vlan = (input('vvedite nomer vlan(100, 200, 300, 500): '))
with open(cfg, 'r') as f:
    list = []
    for line in f:
        if '.' in line:
            list.append(line.rstrip().replace(' DYNAMIC    ', ''))
    list.sort()
    for i in list:
        if vlan in i:
            print (i)























