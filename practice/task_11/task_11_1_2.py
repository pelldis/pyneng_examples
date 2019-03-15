def parse_cdp_neighbors(cfg_cdp):
    with open(cfg_cdp) as f:
        cdp_neighbors = {}
        local_device_list = []
        local_intf_list = []
        remote_device_list = []
        remote_intf_list = []
        for line in f:
            if 'show cdp' in line:
                local_host = line.split('>')[0]
            elif 'Eth' in line or 'Fa' in line:
                local_intf = line.split()[1]+ line.split()[2]
                remote_intf = line.split()[8] + line.split()[9]
                remote_host = line.split()[0]
                local_device_list.append(local_host)
                local_intf_list.append(local_intf)
                remote_device_list.append(remote_host)
                remote_intf_list.append(remote_intf)

    cdp_neighbors = dict(zip(zip(local_device_list, local_intf_list),zip(remote_device_list, remote_intf_list)))
    return cdp_neighbors

print (parse_cdp_neighbors('sw1_sh_cdp_neighbors.txt'))





























