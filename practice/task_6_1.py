ip = (input('vvedite ip address: ')).split('.')
if int(ip[0]) > 0 and int(ip[0]) < 224:
    print ('unicast')
elif int(ip[0]) > 223:
    print ('multicast')
elif '0' in ip[0] and '0' in ip[1] and '0' in ip[2] and '0' in ip[3]:
    print ('unassigned')
else:
    print ('unused')







































