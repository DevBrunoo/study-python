class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def cumplir_anos(self):
        self.edad += 1
        print(f"Felz cumplenos #{self.edad} {self.nombre}")

class Empleado(Persona):
    def __init__(self, horas_totales, nombre, edad):
        super(Empleado, self).__init__(nombre, edad)
        self.horas_totales = horas_totales
    
    def trabajar(self, horas_trabajados):
        self.horas_totales += horas_trabajadas
        print(f"Utesd ha tabajado {horas_trabajados} horas")
        print(f"Horas totales: {self.horas_totales}")

    paco = Empleado(nombre="Paco", edad=20, horas_totales=30)
    paco.trabajar(horas_trabajados=8)
    paco.cumplir_anios()


    #