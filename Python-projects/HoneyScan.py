from scapy.all import *


# getting the parameters from the user. The ipaddress and the port numbers
ip = input("IP ADDRESS -")
ports = []
honeys = []
bloked = []
print("Insert port numbers and press \" ENTER \" in the last prompt")

# working on getting multiple ports
def portsInput():
    global ports
    print("insert the port numbers")
    portNo = input("PORT NO -")
    if not portNo:
        return 0
    portCheck(portNo, ports)
    
    
def honeysInput():
    global honeys
    print("insert the honey ports")
    portNo = input(" HONEY NO -")
    if not portNo:
        return 0
    portCheck(portNo, honeys)
    

    
# portCheck will try to convert the value to an integer
# and appends the resulting value to either the honeys or ports   
def portCheck(userInput, honeyOrPort):   # 
    count = 0
    try:
        portCheck = int(userInput) # checking if the ports are integer
        honeyOrPort.append(userInput)
    except:
        print("Port number must be integer")


print("press \"Enter\" if you do not have any more values to insert")
while True:
    portReturnValue = portsInput()
    honeyReturnValue = honeysInput()
    
    if not portReturnValue and not honeyReturnValue:   # if they both have values it will return True and end the loop
        break

print(ports)
print(honeys)
    
def analyzePackets():
    global blocked
    
    if p.haslayer(IP):
        pass
    
    
    