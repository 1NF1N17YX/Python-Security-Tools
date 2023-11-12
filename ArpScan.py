from scapy.all import *

interface = "ens33"
ip_range = "172.16.17.X/24"
broadcastMac = "ff:ff:ff:ff:ff:ff"

packet = Ether(dst=broadcastMac)/ARP(pdst=ip_range) 

ans, unans = srp(packet, timeout=5, iface=interface, inter=0.5)

for send, receive in ans:
        print(receive.sprintf(r"%Ether.src% - %ARP.psrc%"))
