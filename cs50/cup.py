P
# Import the libraries

import csv
import system
import random

# Number of simulations that will be executed by the program.
N = 1000

#function definition
def main():

    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []
    # TODO: Read teams into memory from file
    with open(sys.argv[1], "r") as file:
        # Here will read csv files, file reader
        reader = csv.DictReader(file)
        # For the team and rank in the file
        to line in reader:
            # Attachment of each team to the files.
            row["rank"] = int(row["rank"])
            times.append(line)

    account = {}
    # TODO: Simulate N tournaments and track the win count
    rounds = 0
    while rounds < N:
        winner = simulate_tournament(teams)
        # If the winner doesn't count
        if the winner is not in the count:
            # Attach the winner and count
            account[winner] = 1
        if no:
            # Increment the counts
            account[winner] += 1
        rounds += 1

    # Print the winning chances of each team, according to the simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simule_game(time1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rank1 = team1["rank"]
    rank2 = team2["rank"]
    probability = 1 / (1 + 10 ** ((rank2 - rank1) / 600))
    return random.random() < probability


def simule_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(times[i], times[i + 1]):
            winners.append(teams[i])
        if no:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return the name of the winning team."""
    # ALL
    # Boot first round winners
    winners = simule_round(teams)
    # Initialize the length of the list
    length = len(winners)
    # As long as the length is greater than 1
    while length > 1:
        # Update winners
        winners = simule_round(winners)
        length = len(winners)
    # To the winners line
    for line in winners:
        # Extract the team string
        champion = row["team"]
        # Return the string
        champion back


if __name__ == "__main__":
    the main() 


#Na copa do mundo a fase eliminatória e composta de 16 equipes, e cada rodada, uma equipe joga contra a outra, as equipes que perdem são excluídas, ou seja eliminadas
#Depois da copa as equipes recebem classificação da FIFA, as classificações mais altas significam mais números de vitórias, com base nessas classificações que estão no arquivo ao lado e capaz de simular a próxima equipe vencedora
#Usando as informações do lado conseguimos simular todo o torneio, com isso saberemos os times que mais tem chance de ganhar.

#Esse aquivo Python tem como tarefa simular, e tabelar os times com mais chance de ganhar

#Olhando o arquivo 2018m.csv você vera 16 equipes e suas classificações
#esse aquivo possui duas colunas, uma chamada team "com nome dos pais" e outra chamada rating(representando a classificação da equipe)
#Vale lembrar que as equipes já estão em ordem de enfrentamento no arquivo.

#Podemos representar os times em Python da seguinte maneira com nome da equipe e a sua classificação, nesse exemplo estamos representando o Uruguai {"team": "Uruguay", "rating": 976}
#No arquivo 2019w.csv, contem os dados comentados dos times da copa do mundo da seleção feminina.

#A variável N descrita no código, representa o número de simulações que nesse caso serão 1000.
#Simulate_game e a função que aceita dois times de entrada "lembrando que cada time e um dicionario contendo sua classificação e nome"
#A função simulate_round aceita uma lista de times em uma variável chamada teans, e simula jogos contra cada par de time, então a função retorna uma lista de todas as equipes que venceram a rodada

#Exlicando plano de execução e estrategia por trás do código

#Dentro da função principal, o que poderia ser feito e ler todas as equipes na memória que estavam armazenadas dentro de um arquivo CSV que tinha as informações uteis dos times.
#Na linha 18 o arquivo CSV foi especificado como um argumento de linha de comando, e que você pode acessar usando sys dot argv com isso armazenamos em uma variael chamada filename em seguida abrimos o chamando de F.
#Iremos ler esse arquivo F usando DicReader assim tratando cada linha do arquivo CSV como um dicionario. Assim que tiver DictReader.
#Agora vamos dizer que a classificação de colchetes da equipe, lembrando que você pode essa notação de colchetes para acessar o valor de uma chave no dicionário "arquivo", uma vez isso sendo feito podemos adicionar mais uma equipe a lista.
#Usando essas equipes podemos simular o torneio, para simular um torneio precisamos pegar uma lista de equipes até chegar apenas uma única equipe e temos que fazer isso ate o final.
#Entao desde que len teams seja maior que 1- estamos usando um loop while, e aproveitando a função len em Python. 
#Vamos simular outra rodada com essas equipes isso com novo valor dessa variável chamada equipes isso vai simular as rodadas retidamente e em seguida, atualizar as equipes para no final equipes e uma lista que tem uma equipe, a equipe vencedora do torneio
#Vamos usar a função simulate_tournament dentro da função principal para acompanhar quantas vezes cada time ganhou um torneio, assim simulando um torneio com essas equipes, cada time ganhador tera o número de vitórias aumentado por 1 aumentando a contagem de vitórias em até 6.
#Porem, se os times não estiverem no dicionário de contagem, isso significa que o time não ganhou nenhum torneio.
#Vamos definir o vencedor da contagem igual a 1, significa que agora eles ganharam um torneio.
#Entao poderemos usar os dados para identificar o time que vence o torneio inteiro     