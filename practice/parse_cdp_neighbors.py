def parse_cdp_neighbors(cfg_cdp):
    with open(cfg_cdp) as f:
        cdp_neighbors = {}
        for line in f:
            if 'show cdp' in line:
                local_host = line.split('>')[0]
            elif 'Eth' in line or 'Fa' in line:
                local_intf = line.split()[1]+ line.split()[2]
                remote_intf = line.split()[8] + line.split()[9]
                remote_host = line.split()[0]
                cdp_neighbors[(local_host, local_intf)] = (remote_intf, remote_host)
    return cdp_neighbors
if __name__ == '__main__':
    print (parse_cdp_neighbors('sw1_sh_cdp_neighbors.txt'))


































