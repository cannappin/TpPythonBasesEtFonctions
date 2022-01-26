from libmoi import *
from datetime import date


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
        # prenom = input("Entrez le prénom de la personne\n")
        # while True:
        #     try:
        #         annee = int(input("Entrez l'année de naissance de la personne\n"))
        #     except ValueError:
        #         print("-----Entrer un nombre entier svp !-------")
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
        
Inscrit_total()
    