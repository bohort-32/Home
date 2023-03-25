# === Imports EXT === #
import pickle
import os
# === Imports INT === #
from Objets.Maison import *
from Fonctions.utilisateur import *


def sauvegarder(objet, fic_sav='./SAV/fic.sav'):
    # Vérifie si le dossier "SAV" existe
    if not os.path.isdir("SAV"):
        os.makedirs("SAV")
    # Vérifie que le fichier existe
    if not os.path.isfile(fic_sav):
        open(fic_sav, 'x').close()
    # Sauvegarde
    with open(fic_sav, "wb") as f:
        pickle.dump(objet, f)
        


def charger(fic_sav='/SAV/fic.sav'):
    # Un fichier de sauvegarde existe
    if os.path.isfile(fic_sav):
        with open(fic_sav, "rb") as f:
            return (pickle.load(f))
    # Aucun fichier n'est présent
    else:
        # Création d'une maison
        maison = Maison()
        ajouter_piece = True
        # Ajout d'une piece
        while ajouter_piece is True:
            # Nom de la piece
            nom_piece = input_check(
                f"Nom de la pièce numéro {maison.get_nb_piece()+1}", str)
            # Demande pour ajouter une nouvelle piece
            maison.ajouter_piece(nom_piece)
            ajouter_piece = input_YN('Ajouter pièce ?')
