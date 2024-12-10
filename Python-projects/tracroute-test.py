from scapy.all import *

# defining target host
print("work 1")

targetHost = input("TARGET HOST -")
# setting the maximum hop
maxHops = 30
# setting the timeout value
print("work 2")

timeout = 2
# setting the starting ttl value
ttl = 1
# setting a flag to indicate if the target host has been reached
reached = False

print("work 1")
# Performing the trace route
while not reached and ttl<=maxHops:
    # sending an ICMP packet with the current value of the ttl
    response = sr1(IP(dst=targetHost, ttl=ttl)/ICMP(), timeout=timeout)
    
    # printing the ip address if the host responds
    if response is not None:
        print(f"Hop{ttl}: {response.src}")
        
        if response.src == targetHost:
            reached=True
    # if no response is received,  print ' * '
    else:
        print(f"Hop {ttl}: *")
        # increment the ttl value
    ttl += 1
    
if not reached:
    print(f"Target host {targetHost} not reached") 