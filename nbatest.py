from selenium import webdriver
import datetime
import os
import sqlite3


class Team:
    def __init__(self, name, conference, division):
        self.name = name
        self.conference = conference
        self.division = division
class Season:
    def __init__(self, name, startdate, enddate):
        self.name = name
        self.startdate = startdate
        self.enddate = enddate
class Player:
    def __init__(self):
        self.id = None
        self.name = None
        self.team = None
        self.primarypos = None
        self.secondarypos = None
        self.height = None
        self.weight = None
        self.country = None
        self.birthdate = None
        self.draftyear = None
        self.draftround = None
        self.draftpick = None
        self.experience = None
        self.pie = None
class PlayerStat:
    def __init__(self):
        self.gameid = None
        self.playerid = None
        self.period = None
        self.minute = None
        self.twoptm = None
        self.twopta = None
        self.threeptm = None
        self.threepta = None
        self.ftm = None
        self.fta = None
        self.ast = None
        self.stl = None
        self.oreb = None
        self.dreb = None
        self.blk = None
        self.to = None
        self.pf = None
        self.plusminus = None
        

dir = os.path.dirname(__file__)
browser = webdriver.Chrome(executable_path = dir + "/chromedriver")

db_connection = sqlite3.connect(dir + "/nba.sqlite")
db_cursor = db_connection.cursor()

# teams = []
# seasons = []
players = []

# def create_teams():
#     create_command = "CREATE TABLE IF NOT EXISTS team (name TEXT NOT NULL PRIMARY KEY, conference TEXT NOY NULL, division TEXT NOT NULL)"
#     db_cursor.execute(create_command)
#     teams.append(Team("Atlanta Hawks", "East", "Southeast"))
#     teams.append(Team("Boston Celtics", "East", "Atlantic"))
#     teams.append(Team("Brooklyn Nets", "East", "Atlantic"))
#     teams.append(Team("Charlotte Hornets", "East", "Southeast"))
#     teams.append(Team("Chicago Bulls", "East", "Central"))
#     teams.append(Team("Cleveland Cavaliers", "East", "Central"))
#     teams.append(Team("Dallas Mavericks", "West", "Southwest"))
#     teams.append(Team("Denver Nuggets", "West", "Northwest"))
#     teams.append(Team("Detroit Pistons", "East", "Central"))
#     teams.append(Team("Golden State Warriors", "West", "Pacific"))
#     teams.append(Team("Houston Rockets", "West", "Southwest"))
#     teams.append(Team("Indiana Pacers", "East", "Central"))
#     teams.append(Team("LA Clippers", "West", "Pacific"))
#     teams.append(Team("Los Angeles Lakers", "West", "Pacific"))
#     teams.append(Team("Memphis Grizzlies", "West", "Southwest"))
#     teams.append(Team("Miami Heat", "East", "Southeast"))
#     teams.append(Team("Milwaukee Bucks", "East", "Central"))
#     teams.append(Team("Minnesota Timberwolves", "West", "Northwest"))
#     teams.append(Team("New Orleans Pelicans", "West", "Southwest"))
#     teams.append(Team("New York Knicks", "East", "Atlantic"))
#     teams.append(Team("Oklahoma City Thunder", "West", "Northwest"))
#     teams.append(Team("Orlando Magic", "East", "Southeast"))
#     teams.append(Team("Philadelphia 76ers", "East", "Atlantic"))
#     teams.append(Team("Phoenix Suns", "West", "Pacific"))
#     teams.append(Team("Portland Trail Blazers", "West", "Northwest"))
#     teams.append(Team("Sacramento Kings", "West", "Pacific"))
#     teams.append(Team("San Antonio Spurs", "West", "Southwest"))
#     teams.append(Team("Toronto Raptors", "East", "Atlantic"))
#     teams.append(Team("Utah Jazz", "West", "Northwest"))
#     teams.append(Team("Washington Wizards", "East", "Southeast"))
#     insert_command = "INSERT INTO team VALUES (?, ?, ?)"
#     for team in teams:
#         db_cursor.execute(insert_command, team)
#     db_connection.commit()
# def create_seasons():
#     create_command = "CREATE TABLE IF NOT EXISTS season (name TEXT NOT NULL PRIMARY KEY, startdate DATE NOT NULL, enddate DATE NOT NULL)"
#     db_cursor.execute(create_command)
#     seasons.append(Season("2002–03", datetime.datetime(2002, 10, 29).strftime("%Y-%m-%d"), datetime.datetime(2003, 6, 15).strftime("%Y-%m-%d")))
#     seasons.append(Season("2003–04", datetime.datetime(2003, 10, 28).strftime("%Y-%m-%d"), datetime.datetime(2004, 6, 15).strftime("%Y-%m-%d")))
#     seasons.append(Season("2004–05", datetime.datetime(2004, 11, 2).strftime("%Y-%m-%d"), datetime.datetime(2005, 6, 23).strftime("%Y-%m-%d")))
#     seasons.append(Season("2005–06", datetime.datetime(2005, 11, 1).strftime("%Y-%m-%d"), datetime.datetime(2006, 6, 20).strftime("%Y-%m-%d")))
#     seasons.append(Season("2006–07", datetime.datetime(2006, 10, 31).strftime("%Y-%m-%d"), datetime.datetime(2007, 6, 14).strftime("%Y-%m-%d")))
#     seasons.append(Season("2007–08", datetime.datetime(2007, 10, 30).strftime("%Y-%m-%d"), datetime.datetime(2008, 6, 17).strftime("%Y-%m-%d")))
#     seasons.append(Season("2008–09", datetime.datetime(2008, 10, 28).strftime("%Y-%m-%d"), datetime.datetime(2009, 6, 14).strftime("%Y-%m-%d")))
#     seasons.append(Season("2009–10", datetime.datetime(2009, 10, 27).strftime("%Y-%m-%d"), datetime.datetime(2010, 6, 17).strftime("%Y-%m-%d")))
#     seasons.append(Season("2010–11", datetime.datetime(2010, 10, 26).strftime("%Y-%m-%d"), datetime.datetime(2011, 6, 12).strftime("%Y-%m-%d")))
#     seasons.append(Season("2011–12", datetime.datetime(2011, 12, 25).strftime("%Y-%m-%d"), datetime.datetime(2012, 6, 21).strftime("%Y-%m-%d")))
#     seasons.append(Season("2012–13", datetime.datetime(2012, 10, 30).strftime("%Y-%m-%d"), datetime.datetime(2013, 6, 20).strftime("%Y-%m-%d")))
#     seasons.append(Season("2013–14", datetime.datetime(2013, 10, 29).strftime("%Y-%m-%d"), datetime.datetime(2014, 6, 15).strftime("%Y-%m-%d")))
#     seasons.append(Season("2014–15", datetime.datetime(2014, 10, 28).strftime("%Y-%m-%d"), datetime.datetime(2015, 6, 16).strftime("%Y-%m-%d")))
#     seasons.append(Season("2015–16", datetime.datetime(2015, 10, 27).strftime("%Y-%m-%d"), datetime.datetime(2016, 6, 19).strftime("%Y-%m-%d")))
#     seasons.append(Season("2016–17", datetime.datetime(2016, 10, 25).strftime("%Y-%m-%d"), datetime.datetime(2017, 6, 12).strftime("%Y-%m-%d")))
#     seasons.append(Season("2017–18", datetime.datetime(2017, 10, 17).strftime("%Y-%m-%d"), datetime.datetime(2018, 6, 8).strftime("%Y-%m-%d")))
#     seasons.append(Season("2018–19", datetime.datetime(2018, 10, 16).strftime("%Y-%m-%d"), datetime.datetime(2019, 6, 13).strftime("%Y-%m-%d")))
#     seasons.append(Season("2019–20", datetime.datetime(2019, 10, 22).strftime("%Y-%m-%d"), datetime.datetime(2020, 10, 11).strftime("%Y-%m-%d")))
#     seasons.append(Season("2020–21", datetime.datetime(2020, 12, 22).strftime("%Y-%m-%d"), datetime.datetime(2021, 7, 22).strftime("%Y-%m-%d")))
#     insert_command = "INSERT INTO season VALUES (?, ?, ?)"
#     for season in seasons:
#         db_cursor.execute(insert_command, season)
#     db_connection.commit()
# def create_players():
#     create_command = "CREATE TABLE IF NOT EXISTS player (id INTEGER NOT NULL PRIMARY KEY, name TEXT NOT NULL, team TEXT NOT NULL REFERENCES team, primarypos TEXT NOT NULL, secondarypos TEXT, height INTEGER NOT NULL, weight INTEGER NOT NULL, country TEXT NOT NULL, birthdate DATE NOT NULL, draftyear INTEGER, draftround INTEGER, draftpick INTEGER, pie REAL)"
#     db_cursor.execute(create_command)

# create_teams()
# create_seasons()
# create_players()

browser.get("https://www.nba.com/players")
page_dropdown = browser.find_elements_by_class_name("DropDown_select__5Rjt0")[-1]
page_dropdown.find_elements_by_tag_name("option")[0].click()
player_items = browser.find_elements_by_xpath("//tbody//tr")
player_links = []
for player_item in player_items:
    player_links.append(player_item.find_elements_by_tag_name("td")[0].find_elements_by_tag_name("a")[0].get_attribute("href"))
for player_link in player_links:
    player = Player()
    player.id = int(player_link.split("https://www.nba.com/player/")[1].split("/")[0])
    browser.get(player_link)
    name_p = browser.find_elements_by_css_selector("p.PlayerSummary_playerNameText__K7ZXO")[0]
    team_p = name_p.parent.find_elements_by_tag_name("p")[0].text
    player.team = team_p.split("|")[0].strip()
    pos_p = team_p.split("|")[2].strip()
    positions = pos_p.split("-")
    player.primarypos = positions[0]
    player.secondarypos  = None  
    if len(positions) == 2:
        player.secondarypos = positions[1]
    first_name = browser.find_elements_by_css_selector("p.PlayerSummary_playerNameText__K7ZXO")[0].text
    last_name = browser.find_elements_by_css_selector("p.PlayerSummary_playerNameText__K7ZXO")[1].text
    player.name = first_name + " " + last_name
    player.pie = float(browser.find_elements_by_css_selector("p.PlayerSummary_playerStatValue__3hvQY")[3].text)
    info_labels = browser.find_elements_by_css_selector("p.PlayerSummary_playerInfoValue__mSfou")
    player.height = int(info_labels[0].text.split(" ")[1].replace("(", "").replace("m)", "").replace(".", ""))
    player.weight = int(info_labels[1].text.split(" ")[1].replace("(", "").replace("kg)", ""))
    player.country = info_labels[2].text
    player.birthdate = datetime.datetime.strptime(info_labels[5].text, "%B %d, %Y")
    if (info_labels[6].text == "Undrafted"):
        player.draftyear = None
        player.draftround = None
        player.draftpick = None
    else:
        player.draftyear = int(info_labels[6].text.split(" ")[0])
        player.draftround = int(info_labels[6].text.split(" ")[1].replace("R", ""))
        player.draftpick = int(info_labels[6].text.split(" ")[3])
    if (info_labels[7].text == "Rookie"):
        player.experience = 0
    else:
        player.experience = int(info_labels[7].text.split(" ")[0])
    players.append(player)


print(players)
start_date = datetime.datetime(2002, 1, 1)
start_date = datetime.datetime(2020, 12, 26)
end_date = datetime.datetime.now()
current_date = start_date
while current_date < end_date:
    browser.get("https://www.nba.com/games?date=" + start_date.strftime("%Y-%m-%d"))
    current_date_games = browser.find_elements_by_class_name("GameCard_card__3jRUe")
    for game in current_date_games:
        scorediv = game.find_elements_by_tag_name("div")[0]
        gamelink = scorediv.find_elements_by_tag_name("a")[2].get_attribute("href")
        browser.get(gamelink)
        teams = browser.find_elements_by_tag_name("h1")
        print(teams)

    current_date = current_date + datetime.timedelta(days=1)
