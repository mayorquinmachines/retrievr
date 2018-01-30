#!/usr/bin/env python
import pexpect


def sound_alarm(BD_ADDR):
    child = pexpect.spawn('gatttool -I')
    child.sendline('connect {}'.format(BD_ADDR))
    child.expect('Connection successful', timeout=60)
    child.sendline('char-write-cmd 0x000b 0100111000000001')

if __name__ == "__main__":
    BD_ADDR = 'AA:BB:CC:DD:EE:FF'     #Bluetooth beacon address
    num_attempts = 0
    while num_attempts < 5:
        print('Attempting to trigger alarm')
        try:
            sound_alarm(BD_ADDR)
            break
        except:
            pass
        num_attempts += 1
    
