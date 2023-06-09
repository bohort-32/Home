# Définition de la classe
class Objet:
    # --- Initialisation
    def __init__(self, id, nom, description=None):
        # ID
        self.id = id
        # Nom
        self.nom = nom
        # Description
        self.description = description

    # --- Get Id
    def get_id(self):
        return self.id

    # --- Get Nom
    def get_nom(self):
        return self.nom
    
    # --- Get Description
    def get_description(self):
        return self.description
    
    # --- To string Obj
    def to_string_obj(self):
        return f"OBJ{self.get_id()} - {self.get_nom()} - {self.get_description}"