from string import digits
from itertools import product

for passcode in product(digits, repeat=4):
    print(*passcode)


# Programa que geraria mais de 9999 possibilidades de senhas 
# Imprime todos os produtos possiveis ou potuacões de senhas de 4 digitos
# Podemos imaginar que o hacker usa um computador com cabo para tentar todas as senhas possiveis 