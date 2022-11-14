import csv

titles = set()

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        title = row["title"].strip().upper()
        titles.add(title)

for title in sorted(titles):
    print(title)
        
#Usaremos DictReader que serve para criar um dicionario apartir de cada linha, permitindo acessar cada coluna pelo nome 
#Uma nova lista chamada titles e criada, e so adicionara titulos se nao estiver na lista
#Python tem uma estrutura chamada set que faz que todos os dados sejam exclusivos
#Para classificar titulos podemos apenas alterar nosso loop para for title in sorted(titles) que classificara nosso conjuto antes de interarmos ele  
#Agora com esse codigo deixamos os titulos em ordem alfabetica