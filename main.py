from Fonctions.analyse_reseau import *



if __name__ == "__main__":
    nombre_appareils = 0
    # Définition de la plage d'adresses IP à analyser
    ip_range = f"{get_wifi_ip()}/24"
    devices = arp_scan(ip_range)
print(len(devices))