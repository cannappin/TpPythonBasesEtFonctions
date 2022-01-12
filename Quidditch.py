from libmoi import *
from datetime import date
import csv

ok = False
while not ok:
    nombre = input("Combien de personne voulez-vous inscrire ?\n(Si vous ne savez appuyer sur 'k')\n")
    try :
        int(nombre)
    except :  
        if nombre == 'k' :
            ok = True    
    else:
        ok = True
        
if nombre == "k":
    continuer = True
    while continuer :
        Inscription()
        # nom = input("Entrez le nom de la personne\n")
        # if not nom.isalpha() :
        #     # or not re.search("[-]", nom)
        #     print("---caractères spéciaux non autorisés----")
        #     nom = input("Entrez le nom de la personne\n")
            
        # prenom = input("Entrez le prénom de la personne\n")
        # while not prenom.isalpha() :
        #     # or not re.search("[-]", prenom)
        #     print("---caractères spéciaux non autorisés----")
        #     prenom = input("Entrez le prénom de la personne\n")
            
        # while True:
        #     try:
        #         annee = int(input("Entrez l'année de naissance de la personne\n"))                       
                    
        #     except ValueError:
        #         print("-----Entrer un nombre entier svp !-------")               

        #     else:
        #         break    
        # while True:                 
        #     if len(str(annee)) !=4 :
        #         print("--------l'année n'est pas valide !-------")
        #         annee = int(input("Entrez l'année de naissance de la personne\n"))
        #     else:
        #         break                  
            
        # a = Mail(nom, prenom) 
        # b = Cat((date.today().year - annee))

        # print(f"Nom: {nom}\nPrénom: {prenom}\nMail: {a}\nCatégorie: {b}\n")
        
        nombre = input("Avez-vous fini ? :  y/n \n")

        if nombre == "y":
            continuer = False
                
else :
    for i in range(int(nombre)):
        Inscription()
        
        
