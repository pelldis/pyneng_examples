template = '''
{0:<25}{1:<25}
{2:<25}{3:<25}
{4:<25}{5:<25}
{6:<25}{7:<25}
{8:<25}{9:<25}
{10:<25}{11:<25}
'''
with open('ospf.txt') as f:
    for line in f:
        line = [ i.strip('[],') for i in line.split()]
        print (template.format('Protocol:', 'OSPF', 'Prefix:', line[1], 'AD/Metric:', line[2],\
        'Next-hop:', line[4], 'Last update:', line[5], 'Outbound Interface:', line[6] ))




































