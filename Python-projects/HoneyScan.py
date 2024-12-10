from scapy.all import *


# getting the parameters from the user. The ipaddress and the port numbers
ip = input("IP ADDRESS -")
ports = []
honeys = []
print("Insert port numbers and press \" ENTER \" in the last prompt")

# working on getting multiple ports
count = 0
while True:
    portNo = input("PORT NO - ")
    honeysNo = input("HONEY NO -")
    try:
        portNo = int(portNo) # converting the string value to integer
        ports.append(portNo)
    except:
        print("Port number must be an integer")
    if not portNo:
        if count > 0:
            break
    
    count += 1
    
    