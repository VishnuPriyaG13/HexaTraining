import csv

players = []
team_runs = {}
total_runs = 0
max_runs = 0
min_runs = 1000
top_player = ""
low_player = ""

max_fours = 0
four_player = ""

max_sixes = 0
six_player = ""

with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        name = row[1]
        team = row[2]
        runs = int(row[4])
        fours = int(row[5])
        sixes = int(row[6])

        players.append([name, runs])

        total_runs += runs

        if runs > max_runs:
            max_runs = runs
            top_player = name

        if runs < min_runs:
            min_runs = runs
            low_player = name

        if fours > max_fours:
            max_fours = fours
            four_player = name

        if sixes > max_sixes:
            max_sixes = sixes
            six_player = name

        if team in team_runs:
            team_runs[team] += runs
        else:
            team_runs[team] = runs

average_runs = total_runs / len(players)

players.sort(key=lambda x: x[1], reverse=True)

with open("cricket_report.txt", "w") as report:

    report.write("SMART CRICKET ANALYTICS REPORT\n\n")

    report.write("Total Players = " + str(len(players)) + "\n")
    report.write("Total Runs = " + str(total_runs) + "\n")
    report.write("Average Runs = " + str(average_runs) + "\n\n")

    report.write("Highest Scorer = " + top_player + "\n")
    report.write("Lowest Scorer = " + low_player + "\n\n")

    report.write("Team Wise Runs\n")
    for team, runs in team_runs.items():
        report.write(team + " : " + str(runs) + "\n")

    report.write("\nTop 5 Players\n")
    for i in range(5):
        report.write(players[i][0] + " : " + str(players[i][1]) + "\n")

    report.write("\nMost Fours = " + four_player + " (" + str(max_fours) + ")\n")
    report.write("Most Sixes = " + six_player + " (" + str(max_sixes) + ")\n")

print("Report generated successfully.")