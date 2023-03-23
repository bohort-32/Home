# Définition de la classe
class Piece:
    # --- Initialisation
    def __init__(self, nom):
        self.nom = nom
        self.liste_obj = []

    # --- Get Nom
    def get_nom(self):
        return self.nom
    
    # --- Set Nom
    def set_nom(self, nv_nom):
        self.nom = nv_nom