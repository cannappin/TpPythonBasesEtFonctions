from datetime import date
import re
import csv
import os

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
    
    rex = re.compile("[a-zA-Z]*[-]?[a-zA-Z]*")
    
    nom = input("Entrez le nom de la personne\n")        
    while not rex.fullmatch(nom):            
        print("---caractères spéciaux non autorisés----")
        nom = input("Entrez le nom de la personne\n")
        
    prenom = input("Entrez le prénom de la personne\n")
    
    while not rex.fullmatch(prenom):
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
        
    mail = Mail(nom, prenom) 
    cat = Cat((date.today().year - annee))

    print(f"Nom: {nom}\nPrénom: {prenom}\nMail: {mail}\nCatégorie: {cat}\n")

    champs =['Nom', 'Prénom', 'Mail', 'Catégorie']

    erengistrement = [nom, prenom, mail, cat ]
    
    filename = "inscrits-" + str(date.today()) + ".csv"
    
    # if le fichier n'exister pas il faut le creer.
    repertoire = os.listdir()
    #  tester si dans cette liste (repertoire) il y'a filename
    if not  filename in repertoire:
        
        csvfile = open(filename,'w')
        csvwriter = csv.writer(csvfile, delimiter =";")
        
        csvwriter.writerow(champs)
        csvfile.close()
                
    with open(filename, 'a', newline='') as csvfile :
        csvwriter = csv.writer(csvfile, delimiter =";")           
        
        csvwriter.writerow(erengistrement)