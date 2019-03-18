import subprocess

def check_ip_address(ip_addressess):
    active_lst = []
    unreachable_lst = [] 
    for i in ip_addressess:
        reply = subprocess.run('ping -c 3 -n {ip}'.format(ip=i), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if reply.returncode == 0 and '3 received' in reply.stdout.decode('utf-8'):
            active_lst.append(i)
        else:
            unreachable_lst.append(i)
    return active_lst, unreachable_lst


ip_list = ['ya.ru', '8.8.8.8', '10.0.0.1']
if __name__=='__main__':
    print (check_ip_address(ip_list)) 
      
