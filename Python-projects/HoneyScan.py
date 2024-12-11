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

# Code to analyse the packets    
def analyzePackets():
    global blocked
    
    if p.haslayer(IP):
        response = Ether(src=[Ether].dst, dst=p[Ether].src)/\
            IP(src=p[IP].dst, dst=p[IP].src)/\
            TCP(sport=p[TCP].dport, dport=p[TCP].sport, ack=p[TCP].seq+1)
        
        source - p[IP].src
    else:
        response = Ether(src=p[Ether].dst, dst=p[Ether].src)/\
            IP(src=p[IPv6].dst, dst=p[IPv6].src)/\
            TCP(sport=p[TCP].dport, dport=p[TCP].sport, ack=p[TCP].seq+1)
        
        source = p[IPv6].src
        
    if p[TCP].flgs != "S":
        return
    
    port = p[TCP].dport
    if source in blocked:
        if port in ports:
            response[TCP].flags = "RA"
            print("Sending reset")
        elif port in honeys:
            response[TCP].flags = "SA"
        else:
            return
        sendp(response, verbose=False)
        
    else:
        if port not in ports:
            blocked += [source]
            if port in honeys:
                respon[TCP].flags = "SA"
                sendp(response, verbose=False)
    
    f = "dst host"+ip+"and tcp"
    sniff(filter=f, prn=analyzePackets)
        
        
    
    
    
    