ip = str(input('vvedite ip address: ')).split('.')

if len(ip) == 4:
    try:
        ip = [int(i) for i in ip]
        IP = True
        for i in ip:
            if i >= 0 and i < 256:
                continue
            else:
                IP = False
                print('Incorrect IPv4 address')
                break
        if IP == True:
            if ip[0] > 0 and ip[0] < 224:
                print ('unicast')
            elif ip[0] > 223:
                print ('multicast')
            elif ip[0] == 0 and ip[1] == 0 and ip[2] == 0 and ip[3] == 0:
                print ('unassigned')
            else:
                print ('unused')
    except ValueError:
        print('Incorrect IPv4 address')

else:
    print('Incorrect IPv4 address')







































