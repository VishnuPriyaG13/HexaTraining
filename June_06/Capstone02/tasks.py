#Read players.csv and Display all records
import csv
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  
    for row in reader:
        print(row)

#Count total players
count = 0
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        count += 1
print("Total Players =", count)

#Highest run scored
max_runs = 0
top_player = ""
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        runs = int(row[4])
        if runs > max_runs:
            max_runs = runs
            top_player = row[1]
print("Highest Scorer =", top_player)
print("Runs =", max_runs)

#Lowest run scored
min_runs = 1000
low_player = ""
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        runs = int(row[4])
        if runs < min_runs:
            min_runs = runs
            low_player = row[1]
print("Lowest Scorer =", low_player)
print("Runs =", min_runs)

#Average runs scored
total = 0
count = 0
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        total += int(row[4])
        count += 1
average = total / count
print("Average Runs =", average)

#Players Scoring More Than 600 Runs
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    print("Players with runs > 600")
    for row in reader:
        if int(row[4]) > 600:
            print(row[1], row[4])

#Players Scoring Less Than 500 Runs
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    print("Players with runs < 500")
    for row in reader:
        if int(row[4]) < 500:
            print(row[1], row[4])

#Count Players by Team
team_count = {}
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        team = row[2]
        if team in team_count:
            team_count[team] += 1
        else:
            team_count[team] = 1
print(team_count)

#Calculate Total Runs by Team
team_runs = {}
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        team = row[2]
        runs = int(row[4])
        if team in team_runs:
            team_runs[team] += runs
        else:
            team_runs[team] = runs
print(team_runs)

#Find Team with Highest Runs
team_runs = {}
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        team = row[2]
        runs = int(row[4])
        if team in team_runs:
            team_runs[team] += runs
        else:
            team_runs[team] = runs
max_team = max(team_runs, key=team_runs.get)
print("Team with Highest Runs =", max_team)
print("Runs =", team_runs[max_team])

#Find Team with Lowest Runs
team_runs = {}
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        team = row[2]
        runs = int(row[4])
        if team in team_runs:
            team_runs[team] += runs
        else:
            team_runs[team] = runs
min_team = min(team_runs, key=team_runs.get)
print("Team with Lowest Runs =", min_team)
print("Runs =", team_runs[min_team])

#Find Player with Most Fours
max_fours = 0
player = ""
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        fours = int(row[5])
        if fours > max_fours:
            max_fours = fours
            player = row[1]
print("Player with Most Fours =", player)
print("Fours =", max_fours)

#Find Player with Most Sixes
max_sixes = 0
player = ""
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        sixes = int(row[6])
        if sixes > max_sixes:
            max_sixes = sixes
            player = row[1]
print("Player with Most Sixes =", player)
print("Sixes =", max_sixes)

#Calculate Total Fours Hit in Tournament
total_fours = 0
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        total_fours += int(row[5])
print("Total Fours =", total_fours)

#Calculate Total Sixes Hit in Tournament
total_sixes = 0
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        total_sixes += int(row[6])
print("Total Sixes =", total_sixes)

#Store All Player Names in a List and Sort Alphabetically
players = []
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        players.append(row[1])
players.sort()
print("Player Names:")
for i in players:
    print(i)

#Store All Teams in a Set and Display Unique Teams
teams = set()
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        teams.add(row[2])
print("Unique Teams:")
for team in sorted(teams):
    print(team)

#Create Dictionary {team : total_runs}
team_runs = {}
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        team = row[2]
        runs = int(row[4])
        if team in team_runs:
            team_runs[team] += runs
        else:
            team_runs[team] = runs
print(team_runs)

#Create Dictionary {player_name : runs}
player_runs = {}
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        player_runs[row[1]] = int(row[4])
print(player_runs)

#Functions
def find_top_scorer():
    max_runs = 0
    player = ""
    with open("players.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            runs = int(row[4])
            if runs > max_runs:
                max_runs = runs
                player = row[1]
    print("Top Scorer =", player)
    print("Runs =", max_runs)
find_top_scorer()

def calculate_average_runs():
    total = 0
    count = 0
    with open("players.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            total += int(row[4])
            count += 1
    average = total / count
    print("Average Runs =", average)
calculate_average_runs()

def find_best_team():
    team_runs = {}
    with open("players.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            team = row[2]
            runs = int(row[4])
            if team in team_runs:
                team_runs[team] += runs
            else:
                team_runs[team] = runs
    best_team = max(team_runs, key=team_runs.get)
    print("Best Team =", best_team)
    print("Runs =", team_runs[best_team])
find_best_team()

def find_total_boundaries():
    total_fours = 0
    total_sixes = 0
    with open("players.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            total_fours += int(row[5])
            total_sixes += int(row[6])
    print("Total Boundaries =", total_fours + total_sixes)
find_total_boundaries()

#Exception Handling
#Handle Missing CSV File
try:
    with open("players.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("File does not exist.")

#Handle Invalid Run Values
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        try:
            runs = int(row[4])
            print(row[1], runs)
        except ValueError:
            print("Invalid run value for", row[1])

#Handle Invalid Match Counts
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        try:
            matches = int(row[3])
            print(row[1], matches)
        except ValueError:
            print("Invalid match count for", row[1])

#NumPy
import numpy as np
runs = []
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        runs.append(int(row[4]))
arr = np.array(runs)
print("Total Runs =", np.sum(arr))
print("Average Runs =", np.mean(arr))
print("Maximum Runs =", np.max(arr))
print("Minimum Runs =", np.min(arr))
print("Standard Deviation =", np.std(arr))
print("Median =", np.median(arr))

#Pandas
import pandas as pd
df = pd.read_csv("players.csv")
print(df)
top5 = df.sort_values(by="runs", ascending=False)
print(top5.head())
sorted_players = df.sort_values(by="runs", ascending=False)
print(sorted_players)
team_runs = df.groupby("team")["runs"].sum()
print(team_runs)
avg_runs = df.groupby("team")["runs"].mean()
print(avg_runs)
df = pd.read_csv("players.csv")
print(df[df["runs"] > 600])
team_runs = df.groupby("team")["runs"].sum()
print(team_runs.idxmax())
