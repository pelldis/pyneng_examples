def get_int_vlan_map(cfg):
    with open(cfg) as f:
        port_access = {}
        port_trunk = {}
        for line in f:
            if line.startswith('interface') and 'Ethernet' in line:
                intf = line.split()[1]
            if 'access vlan' in line:
                port_access[intf] = int(line.split()[3])
            elif 'trunk allowed vlan' in line:
                port_trunk[intf] = [ int(i) for i in line.split()[4].split(',')]
        print (port_access)
        print (port_trunk)
        return port_access, port_trunk

get_int_vlan_map('config_sw1.txt')













































