class Persona: 
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
 
paco = Persona("Paco", 20)
print(paco.nombre)
print(paco.edad)