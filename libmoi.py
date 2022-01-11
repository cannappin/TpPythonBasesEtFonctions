from datetime import date

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
        prenom = input("Entrez le prénom de la personne\n")
        while True:
            try:
                annee = int(input("Entrez l'année de naissance de la personne\n")) 
                while True :
                    try:
                        len(str(annee)) != 4
                    except:  
                        print("L'année n'est pas correct")        
                    else:
                        break          
                    
            except ValueError:
                print("-----Entrer un nombre entier svp !-------")               

            else:
                break     
            
       
        
                 
                      
            
        a = Mail(nom, prenom) 
        b = Cat((date.today().year - annee))

        print(f"Nom: {nom}\nPrénom: {prenom}\nMail: {a}\nCatégorie: {b}\n")

