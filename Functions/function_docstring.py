def perimetro_cuadrado(lado):
    ''' Calcular el perimetrocde un cuadrado.
    
    Esta funcion recibe el valor de un lado de un cuadrado y a partir
    de este calcula y retorna su perimetro

    Args:
       Lado (int):  medida del lado del cuadrado

    Returns:
       perimetro (int): perimetro del cuadrado
     '''

    perimetro = lado * 4
    return perimetro


perimetro_cuadrado(lado=5)