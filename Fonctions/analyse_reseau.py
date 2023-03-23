from scapy.all import *

# Retourne l'IP wifi connectée
def get_wifi_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 1))
    wifi_ip = s.getsockname()[0]
    s.close()
    return wifi_ip


def arp_scan(ip_range):
    # Envoie de requêtes ARP pour chaque adresse IP dans la plage donnée
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_range), timeout=2, verbose=False)
    # Récupération des adresses MAC et IP des appareils connectés
    devices = []
    for snd, rcv in ans:
        devices.append((rcv.sprintf("%Ether.src%"), rcv.sprintf("%ARP.psrc%")))
    return devices