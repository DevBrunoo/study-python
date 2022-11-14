import csv 

with open("favorites.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader: 
        print(row[1])
        
        
#Esse e um programa para ler o favorites.csv 
#A referencia file apre o arquivo usando a palavra with que fechara o arquivo 
# Usamos next para pular uma linha 
# reader vai criar uma variaavel reader que ira ler o arquivo