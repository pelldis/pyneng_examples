def generate_access_config(access, psecurity = False):
    access_template = ['switchport mode access',
    'switchport access vlan',
    'switchport nonegotiate',
    'spanning-tree portfast',
    'spanning-tree bpduguard enable']
    port_security = ['switchport port-security maximum 2',
                     'switchport port-security violation restrict',
                     'switchport port-security']
    cmd_dict = {}
    for port, vlan in access.items():
        intf = 'interface ' + port
        cmd_list = []
        for command in access_template:
            if 'access vlan' in command:
                cmd_list.append((command + ' ' + str(vlan)))
            else:
                cmd_list.append(command)
        if psecurity:
            cmd_list = cmd_list + port_security
        cmd_dict[intf] = cmd_list
    return cmd_dict


access_dict = { 'FastEthernet0/12':10,
'FastEthernet0/14':11,
'FastEthernet0/16':17,
'FastEthernet0/17':150 }
print (generate_access_config(access_dict, True ))










































