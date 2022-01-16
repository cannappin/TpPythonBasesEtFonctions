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
total =[]
repertoire = listdir()
for i in repertoire:
    if i.endswith('.csv'):
        with open(total[i], 'r') as csv_file:
                csv_reader = csv.reader(csv_file)

                with open ('inscrits_total.csv') as new_file:
                    csv_writer = csv.writer(new_file,delimiter =';')

                    for line in csv.reader:
                        csv.writer.writerow(line)