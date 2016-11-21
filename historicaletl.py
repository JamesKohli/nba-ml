import openpyxl
import csv

data = openpyxl.load_workbook('data/Team-sample.xlsx', read_only=True)
ws = data.active

with open('data/teamdata.csv', 'wb') as csvfile:
    datawriter = csv.writer(csvfile, delimiter=',')
    rowcount = ws.max_row
    #for each row in ws
    for x in range(2, rowcount, 2):

        reg_season = ws['A'+str(x)].value
        home_team = ws['C'+str(x)].value
        away_team = ws['C'+str(x+1)].value

        datawriter.writerow([reg_season, home_team, away_team])
        #datawriter.writerow([Home Team, Away Team, Date, Home 1, Home 2, Home 3, Home 4, Home 5, Away 1, Away 2, Away 3, Away 4, Away 5, Head Ref, Regular Season, Rest Days, Line, Home Wins, Away Wins, Push])
