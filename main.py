from flask import Flask, render_template, request
import Fonctions.system as FONC_SYS
from Objets.Maison import Maison
from Objets.Lumiere import Lumiere

# Variables Globales
app = Flask(__name__)
MAISON = None

# ============================== #
# ============ Root ============ #
# ============================== #

@app.route('/')
def index():
    # Chargement de la maison
    global MAISON
    MAISON = FONC_SYS.charger()
    # Maison initialisée
    if MAISON != None :
        return render_template('index.html')
    else:
        MAISON = Maison()
        return render_template('ajouter_piece.html')


# ============================== #
# ====== Ajout d'une pièce ===== #
# ============================== #

# Ajout d'une pièce (affichage graphique)
@app.route('/add_piece_graph')
def add_piece_graph():    
    return render_template('ajouter_piece.html')



# Ajout d'une pièce
@app.route('/add_piece', methods=['POST'])
def add_piece():
    global MAISON
    # Liste des arguments passés par POST
    liste_pieces = request.form
    # Maison a créer
    for key_piece in liste_pieces:
        # Si ce n'est pas le nombre de pièces
        if key_piece != 'nb_piece':
            MAISON.ajouter_piece(liste_pieces[key_piece])
    
    return render_template('index.html')



# ============================== #
# ===== Ajout d'une lumière ==== #
# ============================== #

# Ajout d'une lumière (Graphique)
@app.route('/add_lumiere_graph')
def add_lumiere_graph():
    global MAISON
    liste_pieces = MAISON.get_liste_piece()
    liste_nom_pieces = []
    for piece in liste_pieces:
        liste_nom_pieces.append(liste_pieces[piece].get_nom())

    return render_template('ajouter_lumiere.html', liste_nom_pieces=liste_nom_pieces)

# Ajout d'une lumière
@app.route('/add_lumiere', methods=['POST'])
def add_lumiere():
    global MAISON
    # Liste des arguments passés par POST
    liste_lumiere = request.form
    for key_lumiere in liste_lumiere:
        #TODO : Ajouter lumiere aux pieces
        print("TODO")
    
    return render_template('index.html')

# ============================== #
# ============ Main ============ #
# ============================== #
if __name__ == '__main__':
    app.run(debug=True)
