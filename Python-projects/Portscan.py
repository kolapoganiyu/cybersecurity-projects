from scapy.all import *
import ipaddress

ports = [25, 80, 53, 443, 445, 8080, 8443]

def SynScan(host):
    ans, uns = sr(
        IP(dst=host)/TCP(sport=3333, 
            dport=ports, flags="S"),
            timeout=2, verbose=0
            )
            
    print(f"open ports at {host}")
    for (s, r) in ans:
        if s[TCP].dport == r[TCP].sport and r[TCP].flags=="SA":
            print(s[TCP].dport)
            
def DNSScan(host):
    ans, unans = sr(
        IP(dst=host)/
        UDP(dport=53)/
        DNS(rd=1,qd=DNSQR(qname="google.com")),
        timeout=2,verbose=0        
    )
    
    if ans and ans[UDP]:
        print(f"DNS Server at {host}")
        
host = input("Enter IP Address: ")
try:
    ipaddress.ip_address(host)
except:
    print("Invalid address")
    exit(-1)