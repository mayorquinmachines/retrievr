import pexpect
from time import sleep

BD_ADDR = 'AA:BB:CC:DD:EE:FF'  #Bluetooth address of beacon

def sound_alarm():
    child = pexpect.spawn('gatttool -I')
    child.sendline('connect {}'.format(BD_ADDR))
    child.expect('Connection successful', timeout=60)
    child.sendline('char-write-cmd 0x000b 0100111000000001')

if __name__ == "__main__":
    flag = False
    num_attempts = 0
    while not flag and num_attempts < 5:
        print('Attempting to trigger alarm')
        try:
            sound_alarm()
            flag = True
        except:
            sleep(2)
            pass
        num_attempts += 1
    
