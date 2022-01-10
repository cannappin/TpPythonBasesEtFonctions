

def Mail(nom , prenom) :
    return prenom[0].upper() + "." + nom.lower() +"@baton-rouge.fr"


def Categorie(age):
    if age < 6 or age > 40 :
        return "Non Admis"
    elif age < 12 :
        return "Poussin"
    elif age < 18 :
        return "Cadet"
    elif age < 24 :
        return "Junior"
    elif age < 30 :
        return "Semi-Pro"
    elif age <= 40 :
        return "Pro"