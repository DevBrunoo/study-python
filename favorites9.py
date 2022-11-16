import csv 

from cs50 import SQL #Aqui e uma funcao SQL, isso porque bibliotrcas de terceiros dentro desse contexto podem ser mais dificeis do que o nescessario.

db = SQL("sqlite:///") #Variavel db para SQL, que fara o seguinte se aparecer uma URL porem que abre um BD no disco. Ou seja com essa linha importaremos seu CSV para SQLite. 

title = input("Title: ") #Pedindo ao ususario que digite um titulo 

db.execute("SELECT COUNT(*) FROM favorites WHERE title LIKE?", title) #Usaremos db execute para executar um comando sql dentro do Python, 

row = rows[0] #Pegando a primeira linha

print(row["counter"])