import csv

with open("stockerbot.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row[1])
        
        
# Sequencia de comandos para testar o codigo 
# no terminal executar python stork, isso ira copilar o arquivo 
# logo apos isso executar sqlite3 stork.db isso ira criar um banco de dados 
# depois voce pode executar .schema no terminal para ver a estrutura do banco de dados 
# a primeira consulta que voce pode executar no banco de dados e a para ver quantos symbols existe 
# para isso basta executar no terminal SELECT COUNT(symbols) FROM stork; 