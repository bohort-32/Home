import Fonctions.system as FONC_SYS
import Fonctions.utilisateur as FONC_USR

if __name__ == "__main__":
    # Chargement du fichier
    SAV = FONC_SYS.charger()
    rep_usr = None

    menu_principal = '(-1 pour stopper)\n1 - Test\n2 - Salut\n\n Choix : '

    while rep_usr != -1:
        try:
            rep_usr = int(input(menu_principal))
        except:
            rep_usr = None
        if rep_usr == 1 or rep_usr == 3:
            print(rep_usr)
        elif rep_usr != -1:
            print('Mauvaise saisie')