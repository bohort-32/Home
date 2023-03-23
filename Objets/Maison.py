from Fonctions.analyse_reseau import *
from Objets.Piece import Piece

# Définition de la classe
class Maison:
    # --- Initialisation
    def __init__(self, ip=None):
        self.ip = ip
        self.liste_piece = {}
        self.nb_piece = 0

    # --- Get liste piece
    def get_liste_piece(self):
        return self.liste_piece
    
    # --- Get nb piece
    def get_nb_piece(self):
        return self.nb_piece

    # --- Increment nb piece
    def increment_nb_piece(self):
        self.nb_piece = self.get_nb_piece() + 1

    # --- Get piece by id
    def get_piece_by_id(self, id):
        return self.get_liste_piece()[id]

    # --- Get ip
    def get_ip(self):
        return self.ip
    
    # --- Set ip
    def get_ip(self, nv_ip):
        self.ip = nv_ip

    # --- Get liste_appareil connecte
    def get_liste_appareils_connectees(self):
        # Définition de la plage d'adresses IP à analyser
        ip_range = f"{get_wifi_ip()}/24"
        devices = arp_scan(ip_range)
        return len(devices)

    # --- Ajouter piece
    def ajouter_piece(self, nom_piece):
        piece = Piece(self.get_nb_piece(), nom_piece)
        self.increment_nb_piece()
        self.liste_piece[piece.get_id()] = piece