# Définition de la classe
class Objet:
    # --- Initialisation
    def __init__(self, nom, description=None):
        # Nom
        self.nom = nom
        # Description
        self.description = description

    # --- Get Nom
    def get_nom(self):
        return self.nom
    
    # --- Get Description
    def get_description(self):
        return self.description