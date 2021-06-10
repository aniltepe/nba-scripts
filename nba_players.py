from selenium import webdriver
import datetime
import os
import sqlite3

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

dir = os.path.dirname(__file__)
browser = webdriver.Chrome(executable_path = dir + "/chromedriver")

db_connection = sqlite3.connect(dir + "/nba.sqlite")
db_cursor = db_connection.cursor()

players = []

create_command = """CREATE TABLE IF NOT EXISTS player (
    id INTEGER PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    team TEXT NOT NULL,
    primarypos TEXT NOT NULL,
    secondarypos TEXT,
    height INTEGER NOT NULL,
    weight INTEGER NOT NULL,
    country TEXT NOT NULL,
    birthdate DATE NOT NULL,
    draftyear INTEGER,
    draftround INTEGER,
    draftpick INTEGER,
    experience INTEGER NOT NULL,
    pie REAL)"""
db_cursor.execute(create_command)

browser.get("https://www.nba.com/players")
browser.implicitly_wait(3)
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
    browser.implicitly_wait(3)
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
    player.name = first_name.replace("'", "") + " " + last_name.replace("'", "")
    player.pie = None
    if len(browser.find_elements_by_css_selector("p.PlayerSummary_playerStatValue__3hvQY")) >= 4:
        player.pie = float(browser.find_elements_by_css_selector("p.PlayerSummary_playerStatValue__3hvQY")[3].text)
    info_labels = browser.find_elements_by_css_selector("p.PlayerSummary_playerInfoValue__mSfou")
    player.height = int(info_labels[0].text.split(" ")[1].replace("(", "").replace("m)", "").replace(".", ""))
    player.weight = int(info_labels[1].text.split(" ")[1].replace("(", "").replace("kg)", ""))
    player.country = info_labels[2].text
    player.birthdate = datetime.datetime.strptime(info_labels[5].text, "%B %d, %Y").date()
    if ("R" in info_labels[6].text) and ("Pick" in info_labels[6].text):
        player.draftyear = int(info_labels[6].text.split(" ")[0])
        player.draftround = int(info_labels[6].text.split(" ")[1].replace("R", ""))
        player.draftpick = int(info_labels[6].text.split(" ")[3])
    else:
        player.draftyear = None
        player.draftround = None
        player.draftpick = None
    if (info_labels[7].text == "Rookie"):
        player.experience = 0
    else:
        player.experience = int(info_labels[7].text.split(" ")[0])
    players.append(player)

browser.quit()

insert_command = "INSERT INTO player VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
for player in players:
    db_cursor.execute(insert_command, (player.id, player.name, player.team, player.primarypos, player.secondarypos, player.height, player.weight, player.country, player.birthdate, player.draftyear, player.draftround, player.draftpick, player.experience, player.pie))
db_connection.commit()