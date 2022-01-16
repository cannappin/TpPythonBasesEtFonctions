import re
import csv
from os import *
from libmoi import *
from datetime import date

# def find_csv( chemin, fin=".csv" ):
#     filenames = listdir(chemin)
#     return [ filename for filename in filenames if filename.endswith(fin) ]

# inscrit = find_csv("C:/Users/strik/Desktop/New folder/TpPythonBasesEtFonctions")
# for name in inscrit:
#     print(name)


# lire le repertoire puis copier les informations de chaque fichier csv dans un nouveau fichier csv et verifier qu'il est pqs de doublon 
fin  = ".csv"
repertoire = os.listdir()
for i in repertoire:
    if i.endswith(fin):
        print(i)
