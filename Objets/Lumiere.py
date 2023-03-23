from Objets.Obj import *

# Définition de la classe
class Lumiere(Objet):
    # --- Initialisation
    def __init__(self, nom, description=None):
        # Héritage
        Objet.__init__(self, nom, description)
        # Etat
        self.allume = False
    
    # --- Retourne l'etat de l'objet
    def get_allumer(self):
        return self.allume
    
    # --- Change l'etat de l'objet
    def set_allumer(self, allume_eteint):
        self.allume = allume_eteint

    # --- Change l'etat de l'objet
    def changer_etat(self):
        self.set_allumer((not self.get_allumer())) 