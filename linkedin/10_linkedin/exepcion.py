def validar_x(x):
    if x < 1:
        raise Exception("La variabre x debe ser mayor a 1")
    else:
        print("x es mayor a 1")

x = 2
validar_x(x) #aqui estamos validando um numero ou x para que se de correta a nossa funcao. Validamos x aonde ele recebera a funcao