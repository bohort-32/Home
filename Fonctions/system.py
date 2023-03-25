# === Imports EXT === #
import pickle
import os
# === Imports INT === #
from Objets.Maison import Maison
from Objets.Lumiere import Lumiere
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


def charger(fic_sav='./SAV/fic.sav'):
    # Un fichier de sauvegarde existe
    if os.path.isfile(fic_sav):
        with open(fic_sav, "rb") as f:
            return (pickle.load(f))
    # Aucun fichier n'est présent
    else:
        creer_maison = input_YN('Créer une maison')
        if creer_maison == True:
            return initialiser_maison()


def initialiser_maison():
    # Création d'une maison
    maison = Maison()
    ajouter_piece = True
    # Ajout d'une piece
    while ajouter_piece is True:
        # Nom de la piece
        nom_piece = input_check(f"Nom de la pièce numéro {maison.get_nb_piece()+1}", str)
        # Demande pour ajouter une nouvelle piece
        maison.ajouter_piece(nom_piece)
        ajouter_piece = input_YN('Ajouter pièce ?')
    
    return maison



def afficher_menu_creation(maison):
    liste_proposition = ['Créer une pièce','Créer une lumiere']
    text = afficher_liste(liste_proposition)
    # Choix utilisateur
    rep_usr = None
    while rep_usr != 0:
        rep_usr = input_int(text)
        if rep_usr in range(1,len(liste_proposition)+1):
            # Ajout d'une pièce
            if rep_usr == 1:
                maison.ajouter_piece(input_check('Nom de la piece'))
        elif rep_usr != 0:
            print('Erreur de saisie')