from Objets.Maison import Maison
from Objets.Obj import Objet
from Objets.Lumiere import Lumiere
from Fonctions.system import *


if __name__ == "__main__":
    '''
    maison = Maison()
    maison.ajouter_piece('Chambre')
    chambre = maison.get_piece_by_id(0)
    '''

    if charger('/SAV/fic.sav') == None:
        maison = Maison()
        ajouter_piece = True
        while ajouter_piece is True:
            nom_piece = input(f"Nom de la pièce numéro {maison.get_nb_piece()} : ")
            maison.ajouter_piece(nom_piece)
            ajouter_piece = input('Ajouter pièce ? ')