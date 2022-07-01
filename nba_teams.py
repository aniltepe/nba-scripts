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
    shortname TEXT NOT NULL,
    conference TEXT NOT NULL,
    division TEXT NOT NULL,
    oldname TEXT)"""
db_cursor.execute(create_command)

teams.append(Team("Atlanta Hawks", "Hawks", "East", "Southeast"))
teams.append(Team("Boston Celtics", "Celtics", "East", "Atlantic"))
teams.append(Team("Brooklyn Nets", "Nets", "East", "Atlantic", "New Jersey Nets"))
teams.append(Team("Charlotte Hornets", "Hornets", "East", "Southeast", "Charlotte Bobcats"))
teams.append(Team("Chicago Bulls", "Bulls", "East", "Central"))
teams.append(Team("Cleveland Cavaliers", "Cavaliers", "East", "Central"))
teams.append(Team("Dallas Mavericks", "Mavericks", "West", "Southwest"))
teams.append(Team("Denver Nuggets", "Nuggets", "West", "Northwest"))
teams.append(Team("Detroit Pistons", "Pistons", "East", "Central"))
teams.append(Team("Golden State Warriors", "Warriors", "West", "Pacific"))
teams.append(Team("Houston Rockets", "Rockets", "West", "Southwest"))
teams.append(Team("Indiana Pacers", "Pacers", "East", "Central"))
teams.append(Team("LA Clippers", "Clippers", "West", "Pacific", "Los Angeles Clippers"))
teams.append(Team("Los Angeles Lakers", "Lakers", "West", "Pacific"))
teams.append(Team("Memphis Grizzlies", "Grizzlies", "West", "Southwest"))
teams.append(Team("Miami Heat", "Heat", "East", "Southeast"))
teams.append(Team("Milwaukee Bucks", "Bucks", "East", "Central"))
teams.append(Team("Minnesota Timberwolves", "Timberwolves", "West", "Northwest"))
teams.append(Team("New Orleans Pelicans", "Pelicans", "West", "Southwest", "New Orleans Hornets"))
teams.append(Team("New York Knicks", "Knicks", "East", "Atlantic"))
teams.append(Team("Oklahoma City Thunder", "Thunder", "West", "Northwest", "Seattle SuperSonics"))
teams.append(Team("Orlando Magic", "Magic", "East", "Southeast"))
teams.append(Team("Philadelphia 76ers", "76ers", "East", "Atlantic"))
teams.append(Team("Phoenix Suns", "Suns", "West", "Pacific"))
teams.append(Team("Portland Trail Blazers", "Trail Blazers", "West", "Northwest"))
teams.append(Team("Sacramento Kings", "Kings", "West", "Pacific"))
teams.append(Team("San Antonio Spurs", "Spurs", "West", "Southwest"))
teams.append(Team("Toronto Raptors", "Raptors", "East", "Atlantic"))
teams.append(Team("Utah Jazz", "Jazz", "West", "Northwest"))
teams.append(Team("Washington Wizards", "Wizards", "East", "Southeast"))

insert_command = "INSERT INTO team VALUES (?, ?, ?, ?, ?)"
for team in teams:
    db_cursor.execute(insert_command, (team.name, team.conference, team.division, team.oldname))
db_connection.commit()
