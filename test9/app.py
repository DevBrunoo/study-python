from flask import Flask #Importando biblioteca flask

app = Flask('flaskconftest')  #Dando nome da aplicacao

# www.google.com/a 

@app.router('/')
def root():
    return 'Eu sou o CEO'
    
app.run()


#Antes de usar flask, certifiquese de ter instalado suas dependencias