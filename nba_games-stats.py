from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import datetime
import os
import sqlite3
import time
   
class Player:
    def __init__(self, row):
        self.id = row[0]
        self.name = row[1]
        self.team = row[2]
        self.primarypos = row[3]
        self.secondarypos = row[4]
        self.height = row[5]
        self.weight = row[6]
        self.country = row[7]
        self.birthdate = datetime.datetime.strptime(row[8], '%Y-%m-%d').date()
        self.draftyear = row[9]
        self.draftround = row[10]
        self.draftpick = row[11]
        self.experience = row[12]
        self.pie = row[13]
class Season:
    def __init__(self, row):
        self.name = row[0]
        self.startdate_rs = datetime.datetime.strptime(row[1], '%Y-%m-%d').date()
        self.enddate_rs = datetime.datetime.strptime(row[2], '%Y-%m-%d').date()
        self.startdate_po = datetime.datetime.strptime(row[3], '%Y-%m-%d').date()
        self.enddate_po = datetime.datetime.strptime(row[4], '%Y-%m-%d').date()
        self.startdate_f = datetime.datetime.strptime(row[5], '%Y-%m-%d').date()
        self.enddate_f = datetime.datetime.strptime(row[6], '%Y-%m-%d').date()
class Team:
    def __init__(self, row):
        self.name = row[0]
        self.conference = row[1]
        self.division = row[2]
        self.oldname = row[3]
class Game:
    def __init__(self):
        self.id = None
        self.season = None
        self.date = None
        self.away = None
        self.home = None
        self.awayscore = None
        self.homescore = None
        self.result = None
        self.isplayoff = None
        self.isfinals = None
class PlayerStat:
    def __init__(self):
        self.gameid = None
        self.team = None
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
        self.trnovr = None
        self.pf = None
        self.plusminus = None

class element_has_class(object):
  def __init__(self, locator, css_class, step_element):
    self.locator = locator
    self.css_class = css_class
    self.step_element = step_element

  def __call__(self, driver):
    element = self.step_element.find_element(*self.locator)
    if self.css_class in element.get_attribute("class"):
        print("table is not busy")
        return self.step_element
    else:
        print("table is busy")
        return False

dir = os.path.dirname(__file__)
driver = webdriver.Chrome(executable_path = dir + "/chromedriver")

db_connection = sqlite3.connect(dir + "/nba.sqlite")
db_cursor = db_connection.cursor()

players = []
seasons = []
teams = []

games_create_command = """CREATE TABLE IF NOT EXISTS game (
    id TEXT PRIMARY KEY NOT NULL,
    season TEXT NOT NULL REFERENCES season,
    date DATE NOT NULL,
    away TEXT NOT NULL REFERENCES team,
    home TEXT NOT NULL REFERENCES team,
    awayscore INTEGER NOT NULL,
    homescore INTEGER NOT NULL,
    result INTEGER NOT NULL,
    isplayoff INTEGER NOT NULL,
    isfinals INTEGER NOT NULL)"""
db_cursor.execute(games_create_command)

playerstats_create_command = """CREATE TABLE IF NOT EXISTS 'game-player' (
    gameid TEXT NOT NULL REFERENCES game,
    team TEXT NOT NULL REFERENCES team,
    playerid INTEGER NOT NULL REFERENCES player,
    period TEXT NOT NULL,
    minute TEXT NOT NULL,
    twoptm INTEGER NOT NULL,
    twopta INTEGER NOT NULL,
    threeptm INTEGER NOT NULL,
    threepta INTEGER NOT NULL,
    ftm INTEGER NOT NULL,
    fta INTEGER NOT NULL,
    ast INTEGER NOT NULL,
    stl INTEGER NOT NULL,
    oreb INTEGER NOT NULL,
    dreb INTEGER NOT NULL,
    blk INTEGER NOT NULL,
    trnovr INTEGER NOT NULL,
    pf INTEGER NOT NULL,
    plusminus INTEGER NOT NULL)"""
db_cursor.execute(playerstats_create_command)

db_cursor.execute("SELECT * FROM player")
rows = db_cursor.fetchall()
for row in rows:
    players.append(Player(row))

db_cursor.execute("SELECT * FROM season")
rows = db_cursor.fetchall()
for row in rows:
    seasons.append(Season(row))

db_cursor.execute("SELECT * FROM team")
rows = db_cursor.fetchall()
for row in rows:
    teams.append(Team(row))


def fetch_games(date, season, isplayoff, isfinals):
    driver.get("https://www.nba.com/games?date=" + date.strftime("%Y-%m-%d"))
    current_date_games = driver.find_elements_by_class_name("GameCard_card__3jRUe")
    game_links = []
    for current_date_game in current_date_games:
        if current_date_game.find_elements_by_tag_name("a")[2].text == "BOX SCORE":
            game_links.append(current_date_game.find_elements_by_tag_name("a")[2].get_attribute("href"))
    for game_link in game_links:
        game_id = game_link.split("/")[-2].split("-")[-1]
        db_cursor.execute("SELECT * FROM game WHERE id = '" + game_id + "'")
        row = db_cursor.fetchone()
        if row:
            continue

        game = Game()
        game.id = game_id
        driver.get(game_link)
        score_text = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "GameHero_matchup__KSK8r")))
        game.awayscore = int(score_text.text.split("\n")[0])
        game.homescore = int(score_text.text.split("\n")[2])
        game.result = 0 if game.awayscore > game.homescore else 1
        range_box = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "Block_tag__s36Yi")))
        stats_box = range_box.parent
        team_name = stats_box.find_element_by_xpath("//section[2]//div[1]//h1[1]").text
        away_team = next(team for team in teams if team.name == team_name or team.oldname == team_name)
        game.away = away_team.name
        team_name = stats_box.find_element_by_xpath("//section[3]//div[1]//h1[1]").text
        home_team = next(team for team in teams if team.name == team_name or team.oldname == team_name)
        game.home = home_team.name
        game.date = date
        game.season = season.name
        game.isplayoff = isplayoff
        game.isfinals = isfinals

        playerstats = []
        
        time_splits = driver.find_element_by_css_selector("select.DropDown_select__5Rjt0[name='period']").find_elements_by_tag_name("option")
        time_splits = [splt for splt in time_splits if splt.text.startswith("Q") or splt.text.startswith("OT")]
        for time_split in time_splits:
            time_split.click()
            combobox = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "select.DropDown_select__5Rjt0[name='period']")))
        
            away_box = stats_box.find_elements_by_tag_name('section')[2].find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")
            home_box = stats_box.find_elements_by_tag_name('section')[3].find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")
            for player_item in away_box + home_box:
                if player_item.text.startswith("TOTALS"):
                    continue
                item_cell = player_item.find_elements_by_tag_name("td")
                player_item_link = item_cell[0].find_element_by_tag_name("a").get_attribute("href")
                player_item_id = int(player_item_link.split("/")[-2])
                existed_player = next((plyr for plyr in players if plyr.id == player_item_id), False)
                if (not existed_player):
                    continue
                stat = PlayerStat()
                stat.gameid = game.id
                stat.team = game.away if player_item in away_box else game.home
                stat.playerid = existed_player.id
                stat.period = time_split.text
                stat.minute = item_cell[1].text
                stat.twoptm = int(item_cell[2].text) - int(item_cell[5].text)
                stat.twopta = int(item_cell[3].text) - int(item_cell[6].text)
                stat.threeptm = int(item_cell[5].text)
                stat.threepta = int(item_cell[6].text)
                stat.ftm = int(item_cell[8].text)
                stat.fta = int(item_cell[9].text)
                stat.ast = int(item_cell[14].text)
                stat.stl = int(item_cell[15].text)
                stat.oreb = int(item_cell[11].text)
                stat.dreb = int(item_cell[12].text)
                stat.blk = int(item_cell[16].text)
                stat.trnovr = int(item_cell[17].text)
                stat.pf = int(item_cell[18].text)
                stat.plusminus = int(item_cell[20].text)

                playerstats.append(stat)

        playerstats_insert_command = "INSERT INTO 'game-player' VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        for stat in playerstats:
            db_cursor.execute(playerstats_insert_command,
            (stat.gameid, stat.team, stat.playerid, stat.period, stat.minute, stat.twoptm, stat.twopta,
            stat.threeptm, stat.threepta, stat.ftm, stat.fta, stat.stl, stat.ast, stat.oreb, stat.dreb,
            stat.blk, stat.trnovr, stat.pf, stat.plusminus))

        game_insert_command = "INSERT INTO game VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        db_cursor.execute(game_insert_command,
            (game.id, game.season, game.date, game.away, game.home, game.awayscore, game.homescore, game.result, game.isplayoff, game.isfinals))
        db_connection.commit()       


for season in seasons[-2:-1]:
    start_date = season.startdate_rs
    end_date = season.enddate_rs
    if end_date > datetime.datetime.today().date():
        end_date = datetime.datetime.today().date() - datetime.timedelta(days=1)
    while start_date <= end_date:
        fetch_games(start_date, season, False, False)
        start_date = start_date + datetime.timedelta(days=1)

    start_date = season.startdate_po
    end_date = season.enddate_po
    if end_date > datetime.datetime.today().date():
        end_date = datetime.datetime.today().date() - datetime.timedelta(days=1)
    while start_date <= end_date:
        fetch_games(start_date, season, True, False)
        start_date = start_date + datetime.timedelta(days=1)

    start_date = season.startdate_f
    end_date = season.enddate_f
    if end_date > datetime.datetime.today().date():
        end_date = datetime.datetime.today().date() - datetime.timedelta(days=1)
    while start_date <= end_date:
        fetch_games(start_date, season, False, True)
        start_date = start_date + datetime.timedelta(days=1)

driver.quit()