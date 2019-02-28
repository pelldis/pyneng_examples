#!/usr/bin/python3

device = (input('Enter device name: '))


london_co = {
'r1' : {
'location': '21 New Globe Walk',
'vendor': 'Cisco',
'model': '4451',
'ios': '15.4',
'ip': '10.255.0.1'
},
'r2' : {
'location': '21 New Globe Walk',
'vendor': 'Cisco',
'model': '4451',
'ios': '15.4',
'ip': '10.255.0.2'
},
'sw1' : {
'location': '21 New Globe Walk',
'vendor': 'Cisco',
'model': '3850',
'ios': '3.6.XE',
'ip': '10.255.0.101',
'vlans': '10,20,30',
'routing': True
}
}
parameter = (input('Enter parameter name ' + str(tuple(london_co[device].keys())) + ': '))
print (london_co[device].get(parameter, 'There is no such parameter!'))

