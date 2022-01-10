

def Mail(nom , prenom) :
    return prenom[0].upper() + "." + nom.lower() +"@baton-rouge.fr"


def Categorie(annee):
    if annee < 6 and annee > 40 :
        return "Non Admis"
    elif annee < 12 :
        return "Poussin"
    elif annee < 18 :
        return "Cadet"
    elif annee < 24 :
        return "Junior"
    elif annee < 30 :
        return "Semi-Pro"
    elif annee <= 40 :
        return "Pro"