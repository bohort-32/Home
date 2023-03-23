# Définition de la classe
class Maison:
    # --- Initialisation
    def __init__(self, ip=None):
        self.ip = ip
        self.liste_piece = []

    # --- Get liste piece
    def get_liste_piece(self):
        return self.liste_piece
    
    # --- Get ip
    def get_ip(self):
        return self.ip
    
    # --- Set ip
    def get_ip(self, nv_ip):
        self.ip = nv_ip