from Objets.Maison import Maison
from Objets.Obj import Objet
from Objets.Lumiere import Lumiere




if __name__ == "__main__":
    maison = Maison()
    maison.ajouter_piece('Chambre')
    chambre = maison.get_piece_by_id(0)