def generate_access_config(access):                                   
    access_template = ['switchport mode access',                      
    'switchport access vlan',                                         
    'switchport nonegotiate',                                         
    'spanning-tree portfast',                                         
    'spanning-tree bpduguard enable']                                 
    cmd_list = []                                                     
    for port, vlan in access.items():                                 
        cmd_list.append('interface ' + port)                          
        for command in access_template:                               
            if 'access vlan' in command:                              
                cmd_list.append((command + ' ' + str(vlan)))          
            else:                                                     
                cmd_list.append(command)                              
    return cmd_list                                                   
                                                                      
                                                                      
access_dict = { 'FastEthernet0/12':10,                                
'FastEthernet0/14':11,                                                
'FastEthernet0/16':17,                                                
'FastEthernet0/17':150 }                                              
generate_access_config(access_dict)
print (generate_access_config(access_dict))                                   
