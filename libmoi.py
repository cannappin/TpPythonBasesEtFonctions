from datetime import date
import re

def Mail(nom , prenom) :
    return prenom[0].upper() + "." + nom.lower() +"@baton-rouge.fr"




def Cat(age):
    dico = {"Poussin": 12, "Cadet": 18, "Junior": 24, "Semi-Pro":30, "Pro": 40}
    if age < 6 or age > 40:
        return "Non Admis"
    for i in dico:
        if age < dico[i]:
            return i 

def Inscription():
    
        nom = input("Entrez le nom de la personne\n")
        if not nom.isalpha() :
            # or not re.search("[-]", nom)
            print("---caractères spéciaux non autorisés----")
            nom = input("Entrez le nom de la personne\n")
            
        prenom = input("Entrez le prénom de la personne\n")
        while not prenom.isalpha() :
            # or not re.search("[-]", prenom)
            print("---caractères spéciaux non autorisés----")
            prenom = input("Entrez le prénom de la personne\n")
            
        while True:
            try:
                annee = int(input("Entrez l'année de naissance de la personne\n"))                       
                    
            except ValueError:
                print("-----Entrer un nombre entier svp !-------")               

            else:
                break    
        while True:                 
            if len(str(annee)) !=4 :
                print("--------l'année n'est pas valide !-------")
                annee = int(input("Entrez l'année de naissance de la personne\n"))
            else:
                break                  
            
        a = Mail(nom, prenom) 
        b = Cat((date.today().year - annee))

        print(f"Nom: {nom}\nPrénom: {prenom}\nMail: {a}\nCatégorie: {b}\n")

