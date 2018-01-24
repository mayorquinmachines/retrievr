#!/usr/bin/env python
import sys
from pssh.pssh_client import ParallelSSHClient

pwd = input('>>')
try:
    addr = sys.argv[1]
except:
    addr = '54:BD:79:2A:8D:F9'
hosts = ['192.168.1.226', '192.168.1.5', '127.0.0.1']
client = ParallelSSHClient(hosts, user='funk', password=pwd)

output = client.run_command('btmgmt find | grep {}'.format(addr), sudo=True)

for host in output:
    stdin = output[host].stdin
    stdin.write(pwd + '\n')
    stdin.flush()
client.join(output)

for host, host_output in output.items():
    read_lst = []
    for reading in host_output.stdout:
        if 'rssi' in reading:
            reading = str(reading).split('rssi ')[1]
            reading = reading.split(' flags')[0]
            read_lst.append(int(reading))
    try:
        print('Host: {} reading: {}'.format(host,sum(read_lst) / len(read_lst)))
    except:
        print('Host: {} reading: N/A'.format(host))
