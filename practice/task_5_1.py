net, mask = input('Enter net/mask: ').split('/')
net = [int(octet) for octet in (net.split('.'))]
mask_list = '1'*int(mask) + '0'*(32-int(mask))
mask_list = [mask_list[:8], mask_list[8:16], mask_list[16:24], mask_list[24:]]
template = '''
Network:
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}

Mask:
/{4}
{5:<10}{6:<10}{7:<10}{8:<10}
{5:08b}  {6:08b}  {7:08b}  {8:08b}
'''

print (template.format(net[0], net[1], net[2], net[3], mask, int(mask_list[0],2), \
int(mask_list[1],2), int(mask_list[2],2), int(mask_list[3],2)))










































