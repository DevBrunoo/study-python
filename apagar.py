# Simulate a sports tournament

import csv
import sys
import random

# Number of simluations to run
N = 1000


def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []
    # TODO: Read teams into memory from file

    counts = {}
    # TODO: Simulate N tournaments and keep track of win counts

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    # TODO


if __name__ == "__main__":
    main()





#Na copa do mundo a fase eliminatoria e composta de 16 equipes, e cada roda uma equipe jogando contra a outra, as equipes que perdem ser excluidas ou seja eliminadas
#Depois da copa as equipes recebem classificacao da FIFA, as classificacoes mais altas significam mais numeros de viroias, com base nessas classificacoes que estao no arquivo ao lado e capaz de simular a proxima equipe vencedora
#Usando as informacoes do lado conseguimos simular todo o torneio, com isso saberemos os times que mais tem chamce de ganhar. 

#Esse aquivo python tem como tarefa simular, e tabelar os times com mais chance de ganhar

#Olhando o arquivo 2018m.csv voce vera 16 equipes e suas classificações 
#esse aquivo posui duas colunas, uma chamada team "com nome do pais" e outra chamada rating(representando a classificação da equipe)
#Vale lembrar que as equipes ja estao em ordem de enfrentamento no arquivo.

#Podemos representar os times em python da seguinte maneira com nome da equipe e a sua classificação, nesse exemplo estamos representando o uruguai {"team": "Uruguay", "rating": 976}
#no arquivo 2019w.csv, contem os dados comentados dos times da copa do mundo da seleção feminina. 

#A variavel N descrita no codigo, representa o numero de simulações que nesse caso serão 1000.
#Simulate_game e a função que aceita dois times de entrada "lembrando que cada time e um dicionario contendo sua classificação e nome"
#A função simulate_round aceita uma lista de times em uma variavel chamada teans, e simula jogos contra cada par de time, entao a funcao retorna uma lista de todas as equipes que venceral a rodada

 