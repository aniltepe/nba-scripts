import os
import sqlite3

class Team:
    def __init__(self, name, conference, division, oldname = None):
        self.name = name
        self.conference = conference
        self.division = division
        self.oldname = oldname

dir = os.path.dirname(__file__)
db_connection = sqlite3.connect(dir + "/nba.sqlite")
db_cursor = db_connection.cursor()

teams = []

create_command = """CREATE TABLE IF NOT EXISTS team (
    name TEXT NOT NULL PRIMARY KEY,
    conference TEXT NOT NULL,
    division TEXT NOT NULL,
    oldname TEXT)"""
db_cursor.execute(create_command)

teams.append(Team("Atlanta Hawks", "East", "Southeast"))
teams.append(Team("Boston Celtics", "East", "Atlantic"))
teams.append(Team("Brooklyn Nets", "East", "Atlantic", "New Jersey Nets"))
teams.append(Team("Charlotte Hornets", "East", "Southeast", "Charlotte Bobcats"))
teams.append(Team("Chicago Bulls", "East", "Central"))
teams.append(Team("Cleveland Cavaliers", "East", "Central"))
teams.append(Team("Dallas Mavericks", "West", "Southwest"))
teams.append(Team("Denver Nuggets", "West", "Northwest"))
teams.append(Team("Detroit Pistons", "East", "Central"))
teams.append(Team("Golden State Warriors", "West", "Pacific"))
teams.append(Team("Houston Rockets", "West", "Southwest"))
teams.append(Team("Indiana Pacers", "East", "Central"))
teams.append(Team("LA Clippers", "West", "Pacific", "Los Angeles Clippers"))
teams.append(Team("Los Angeles Lakers", "West", "Pacific"))
teams.append(Team("Memphis Grizzlies", "West", "Southwest"))
teams.append(Team("Miami Heat", "East", "Southeast"))
teams.append(Team("Milwaukee Bucks", "East", "Central"))
teams.append(Team("Minnesota Timberwolves", "West", "Northwest"))
teams.append(Team("New Orleans Pelicans", "West", "Southwest", "New Orleans Hornets"))
teams.append(Team("New York Knicks", "East", "Atlantic"))
teams.append(Team("Oklahoma City Thunder", "West", "Northwest", "Seattle SuperSonics"))
teams.append(Team("Orlando Magic", "East", "Southeast"))
teams.append(Team("Philadelphia 76ers", "East", "Atlantic"))
teams.append(Team("Phoenix Suns", "West", "Pacific"))
teams.append(Team("Portland Trail Blazers", "West", "Northwest"))
teams.append(Team("Sacramento Kings", "West", "Pacific"))
teams.append(Team("San Antonio Spurs", "West", "Southwest"))
teams.append(Team("Toronto Raptors", "East", "Atlantic"))
teams.append(Team("Utah Jazz", "West", "Northwest"))
teams.append(Team("Washington Wizards", "East", "Southeast"))

insert_command = "INSERT INTO team VALUES (?, ?, ?, ?)"
for team in teams:
    db_cursor.execute(insert_command, (team.name, team.conference, team.division, team.oldname))
db_connection.commit()
