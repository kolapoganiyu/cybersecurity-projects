from scapy.all import *

# sending an ICMP to an host

ipOfHost = input("Ip Address- ")
response, = sr1(IP(dst=ipOfHost)/ICMP())

print(response)