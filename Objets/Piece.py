# Définition de la classe
class Piece:
    # --- Initialisation
    def __init__(self, id, nom):
        self.id = id
        self.nom = nom
        self.liste_obj = {}

    # --- Get Id
    def get_id(self):
        return self.id

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
    def get_objet_by_id(self, id):
        self.get_liste_objet()[id]

    # --- Ajouter un objet
    def ajouter_objet(self, objet):
        self.liste_obj[objet.get_id()] = objet