import Fonctions.system as FONC_SYS
import Fonctions.utilisateur as FONC_USR

if __name__ == "__main__":
    # Chargement du fichier
    SAV = FONC_SYS.charger()
    print(FONC_USR.afficher_menu(['Test', 'Hola']))