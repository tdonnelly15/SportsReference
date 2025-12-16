
import json

f = open("/Users/donnetom/Downloads/sportsreference.json", "r")
data = json.load(f)
teams = sorted(data.keys())
#Create Column Width(2 spaces)
col_width = max(len(team) for team in teams)+2

#Create Header
header = " " * col_width
for team in teams:
    header += team.ljust(col_width)
print(header)

#Create Rows
for team in teams:
    row = team.ljust(col_width)
    for opponent in teams:
        if team == opponent:
            cell = "-"
        else:
            record = data[team].get(opponent)
            if record:
                cell = f"{record['W']}"
            else:
                cell = "0"
        row += cell.ljust(col_width)
    print(row)
