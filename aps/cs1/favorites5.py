# Imports titles and genres from CSV into a SQLite database
  
import cs50 #Importamos a biblioteca CS50 para que fique mais facil o codigo
import csv
  
# Create database
open("favorites8.db", "w").close()
db = cs50.SQL("sqlite:///favorites8.db")
  
# Create tables
db.execute("CREATE TABLE shows (id INTEGER, title TEXT NOT NULL, PRIMARY KEY(id))")
db.execute("CREATE TABLE genres (show_id INTEGER, genre TEXT NOT NULL, FOREIGN KEY(show_id) REFERENCES shows(id))")
  
# Open CSV file
with open("favorites.csv", "r") as file:
  
    # Create DictReader
    reader = csv.DictReader(file)
  
    # Iterate over CSV file
    for row in reader:
  
        # Canoncalize title
        title = row["title"].strip().upper()
  
        # Insert title
        show_id = db.execute("INSERT INTO shows (title) VALUES(?)", title)
  
        # Insert genres
        for genre in row["genres"].split(", "):

            db.execute("INSERT INTO genres (show_id, genre) VALUES(?, ?)", show_id, genre)




# O codigo importara cada linha de favorites.csv
# Agora teremos com esse codigo uma tabela SHOWS
# com colunar ID e uma title coluna, podemos especificar que title nao e nulo e essa id e a coluna que queremos usar 
# Assim teremos uma tabela chamada genres, onde havera uma show_id 

#Esse programa usa SQL para importa dados CSV para duas tabelas 