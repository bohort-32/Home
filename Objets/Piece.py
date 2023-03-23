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

    # --- Get liste_objet
    def get_liste_objet(self):
        return self.liste_obj

    # --- Ajouter un objet
    def ajouter_objet(self, objet):
        self.liste_obj.append(objet)