import pickle

def sauvegarder(fic_sav, objet):
    with open(fic_sav, "wb") as f:
        pickle.dump(objet, f)

def charger(fic_sav):
    with open(fic_sav, "rb") as f:
        return (pickle.load(f))