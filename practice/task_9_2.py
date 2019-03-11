def generate_access_config(trunk):                       
    trunk_template = ['switchport trunk encapsulation dot1q',
    'switchport mode trunk',                             
    'switchport trunk native vlan 999',                  
    'switchport trunk allowed vlan']                     
                                                         
    cmd_list = []                                        
    for port, vlans in trunk.items():                    
        cmd_list.append('interface ' + port)             
        for command in trunk_template:                   
            if 'allowed vlan' in command:                
                cmd_list.append((command + ' ' + ','.join(str(vlan) for vlan in vlans)))
            else:                                        
                cmd_list.append(command)                 
    return cmd_list                                      
                                                         
trunk_dict = { 'FastEthernet0/1':[10,20,30],             
'FastEthernet0/2':[11,30],                               
'FastEthernet0/4':[17] }                                 
                                                         
                                                         
generate_access_config(trunk_dict)                       
print ('\n'.join(generate_access_config((trunk_dict))))  













































