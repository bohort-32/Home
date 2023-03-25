import Fonctions.system as FONC_SYS
import Fonctions.utilisateur as FONC_USR

if __name__ == "__main__":
    # Chargement du fichier
    maison = FONC_SYS.charger()
    if maison != None:
        print(maison.to_string_maison())
        FONC_SYS.afficher_menu_creation(maison)

