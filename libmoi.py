

def Mail(nom , prenom) :
    return prenom[0].upper() + "." + nom.lower() +"@baton-rouge.fr"



def Cat(age):
    dico = {"Poussin": 12, "Cadet": 18, "Junior": 24, "Semi-Pro":30, "Pro": 40}
    if age < 6 or age > 40:
        return "Non Admis"
    for i in dico:
        if age < dico[i]:
            return i 