from string import ascii_letters, digits, punctuation
from itertools import product

for passcode in product(ascii_letters + digits + punctuation, repeat=8):
    print(*passcode)

# Programa para descubrir senhas com mais de quadrilhoes de possibilidade
