import subprocess
import ipaddress
from tabulate import tabulate

def check_ip_address(ip_addressess):
    active_lst = []
    unreachable_lst = [] 
    for i in ip_addressess:
        reply = subprocess.run('ping -c 3 -n {ip}'.format(ip=i), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if reply.returncode == 0 and '3 received' in reply.stdout.decode('utf-8'):
            active_lst.append(i)
        else:
            unreachable_lst.append(i)
    print(1)
    return active_lst, unreachable_lst

def check_ip_availability(ip1):
    if '-' in ip1:
        ip_min = ipaddress.ip_address(ip1.split('-')[0])
        ip_last = ip1.split('-')[1]
        try:
            ip_last = ipaddress.ip_address(ip_last)
            ip_num = int(str(ip_last).split('.')[3]) +1 - int(str(ip_min).split('.')[3])
            ip_list = [str(ip_min + i) for i in range(ip_num)]
        except ValueError:
            ip_list = [str(ip_min + i) for i in range (int(ip_last)+ 1 - int(str(ip_min).split('.')[3]))]
    else:
        ip_list = [ip1]  
    return ip_list 

def ip_table(ip_list1, ip_list2):
    print(tabulate({'Reachable': ip_list1, 'Unreachable': ip_list2}, headers='keys', stralign='left'))

if __name__=='__main__':
    ip_list = input('vvedite ip: ') 
    ip_lists = check_ip_address(check_ip_availability(ip_list)) 
    ip_table(ip_lists[0], ip_lists[1]) 
