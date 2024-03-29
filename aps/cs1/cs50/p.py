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
    with open(sys.argv[1], "r") as file:
        # Reader for the csv file
        reader = csv.DictReader(file)
        # For the team and rating in the file
        for row in reader:
            # Append each team and its rating
            row["rating"] = int(row["rating"])
            teams.append(row)

    counts = {}
    # TODO: Simulate N tournaments and keep track of win counts
    rounds = 0
    while rounds < N:
        winner = simulate_tournament(teams)
        # If the winner not in counts
        if winner not in counts:
            # Append the winner and counts
            counts[winner] = 1
        else:
            # Increment the counts
            counts[winner] += 1
        rounds += 1

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
    # Initalize the first round winners
    winners = simulate_round(teams)
    # Initalize the length of the list
    length = len(winners)
    # While the length if greater than 1
    while length > 1:
        # Update winners; recall the function with the old winner as argv
        winners = simulate_round(winners)
        # update the length
        length = len(winners)
    # For the row in winners
    for row in winners:
        # Extract the team string
        champ = row["team"]
        # Return the string
        return champ


if __name__ == "__main__":
    main()