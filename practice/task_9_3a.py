def get_int_vlan_map(cfg):
    with open(cfg) as f:
        port_access = {}
        port_trunk = {}
        for line in f:
            if line.startswith('interface') and 'Ethernet' in line:
                intf = line.split()[1]
            if 'access vlan' in line:
                port_access[intf] = int(line.split()[3])
            elif 'mode access' in line:
                port_access[intf] = 1 
            elif 'trunk allowed vlan' in line:
                port_trunk[intf] = [ int(i) for i in line.split()[4].split(',')]
        return port_access, port_trunk

print (get_int_vlan_map('config_sw2.txt'))













































