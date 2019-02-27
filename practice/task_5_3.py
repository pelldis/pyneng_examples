
mode = {'mode': (input('Enter interface mode (acces/trunk): '))}

type = {'type': (input('Enter interface type and number: '))}

vlans = {'vlans': (input('Enter vlan(s): '))}


access_template = ['switchport mode access',
'switchport access vlan {}',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable']



trunk_template = ['switchport trunk encapsulation dot1q',
'switchport mode trunk',
'switchport trunk allowed vlan {}']

modes = { 'access' : access_template, 'trunk': trunk_template }

print ('interface ' + type['type'])
print ( (str('\n'.join(modes[mode['mode']]))).format(vlans['vlans']))


















