#Generate top_players.csv
import csv
from tasks import *
from reports import *
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    with open("top_players.csv", "w", newline="") as file1:
        writer = csv.writer(file1)
        next(reader)
        writer.writerow(["player_id", "player_name", "team", "matches", "runs", "fours", "sixes"])
        for row in reader:
            if int(row[4]) > 600:
                writer.writerow(row)
print("top_players.csv created successfully")

#Generate team_summary.csv

team_runs = {}
team_count = {}
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        team = row[2]
        runs = int(row[4])
        if team in team_runs:
            team_runs[team] += runs
            team_count[team] += 1
        else:
            team_runs[team] = runs
            team_count[team] = 1
with open("team_summary.csv", "w", newline="") as file1:
    writer = csv.writer(file1)
    writer.writerow(["Team", "Total Runs", "Average Runs", "Player Count"])
    for team in team_runs:
        average = team_runs[team] / team_count[team]
        writer.writerow([team, team_runs[team], average, team_count[team]])
print("team_summary.csv created successfully")

#Menu-Driven Application
while True:
    print("\n1. Player Analysis")
    print("2. Team Analysis")
    print("3. Boundary Analysis")
    print("4. Export Reports")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        find_top_scorer()
        calculate_average_runs()

    elif choice == 2:
        find_best_team()

    elif choice == 3:
        find_total_boundaries()

    elif choice == 4:
        generate_report()     # Function containing report generation code
        print("Report generated successfully")

    elif choice == 5:
        print("Thank You")
        break

    else:
        print("Invalid Choice")