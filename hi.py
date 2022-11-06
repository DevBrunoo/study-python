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