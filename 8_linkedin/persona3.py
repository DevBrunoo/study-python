class Pesona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cumplir_anios(self):
        self.edad += 1
        print(f"Feliz cumpleanos #{self.edad} {self.nombre}")

paco = Persona(nombre="Paco", edad=20)
paco.cumplir_anios()