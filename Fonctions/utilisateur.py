# --- Input for Yes or Not
def input_YN(question):
    # Réponse de l'utilisateur
    rep_usr = input(f"{question} [Y/N] : ")

    if rep_usr == 'Y' or rep_usr == 'y':
        rep_usr = True
    elif rep_usr == 'N' or rep_usr == 'n':
        rep_usr = False
    else:
        rep_usr = input_YN(question)

    return rep_usr


# --- Input for checking
def input_check(question, type):
    # Rep for user
    rep_usr = input(f"{question} : ")
    # Check for type
    if not isinstance(rep_usr, type):
        rep_usr = input_check(f"{question} : ")
    # Return answer
    return rep_usr



def input_int(question):
    # Essaye l'input en int
    try:
        rep_usr = int(input(question))
    # Si ça ne marche pas : Message erreur + reassaie
    except:
        print('Erreur de saisie')
        rep_usr = input_int(question)
    return rep_usr



def afficher_liste(liste_proposition):
    # Construction du texte à afficher
    text = '0 pour sortir\n'
    proposition_courante = 1
    for proposition in liste_proposition:
        text = f"{text}{proposition_courante} - {proposition}\n"
        proposition_courante = proposition_courante + 1
    text = f"{text}\nVotre choix : "

    return text


