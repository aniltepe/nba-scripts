from selenium import webdriver
import datetime
import os
import sqlite3
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class Player:
    def __init__(self):
        self.id = None
        self.firstname = None
        self.lastname = None
        self.fullname = None
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
driver = webdriver.Chrome(executable_path = dir + "/chromedriver")

db_connection = sqlite3.connect(dir + "/nba.sqlite")
db_cursor = db_connection.cursor()

players = []

create_command = """CREATE TABLE IF NOT EXISTS player (
    id INTEGER PRIMARY KEY NOT NULL,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    fullname TEXT NOT NULL,
    team TEXT,
    primarypos TEXT,
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

driver.get("https://www.nba.com/players")
page_dropdown = driver.find_elements_by_class_name("DropDown_select__5Rjt0")[-1]
page_dropdown.find_elements_by_tag_name("option")[0].click()
player_items = driver.find_elements_by_xpath("//tbody//tr")
player_links = []
for player_item in player_items:
    player_links.append(player_item.find_elements_by_tag_name("td")[0].find_elements_by_tag_name("a")[0].get_attribute("href"))
for player_link in player_links:
    player = Player()
    player.id = int(player_link.split("https://www.nba.com/player/")[1].split("/")[0])
    db_cursor.execute("SELECT * FROM player WHERE id = '" + str(player.id) + "'")
    row = db_cursor.fetchone()
    if row:
        continue
    driver.get(player_link)
    try:
        test = driver.find_elements_by_css_selector("p.PlayerSummary_playerNameText__K7ZXO")[0]
    except:
        print("problem at getting page", player_link)
        driver.get(player_link)
    name_p = driver.find_elements_by_css_selector("p.PlayerSummary_playerNameText__K7ZXO")[0]
    parent_div = name_p.find_element_by_xpath("./..")
    basic_info_ps = parent_div.find_elements_by_tag_name("p")
    if len(basic_info_ps) == 2:
        player.team = None
        player.primarypos = None
        player.secondarypos  = None
        player.firstname = basic_info_ps[0].text
        player.lastname = basic_info_ps[1].text
    elif len(basic_info_ps) >= 3:
        team_p = basic_info_ps[0].text
        player.team = team_p.split("|")[0].strip()
        pos_p = team_p.split("|")[2].strip() if len(team_p.split("|")) == 3 else team_p.split("|")[1].strip()
        positions = pos_p.split("-")
        player.primarypos = positions[0]
        player.secondarypos  = None  
        if len(positions) == 2:
            player.secondarypos = positions[1]
        player.firstname = basic_info_ps[1].text
        player.lastname = basic_info_ps[2].text
    player.firstname = player.firstname.replace("'", "\'")
    player.lastname = player.lastname.replace("'", "\'")
    player.fullname = player.firstname + " " + player.lastname
    player.pie = None
    stat_p = driver.find_elements_by_css_selector("p.PlayerSummary_playerStatValue__3hvQY")
    if len(stat_p) >= 4:
        player.pie = float(stat_p[3].text)
    info_labels = driver.find_elements_by_css_selector("p.PlayerSummary_playerInfoValue__mSfou")
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

    insert_command = "INSERT INTO player VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    db_cursor.execute(insert_command, (player.id, player.firstname, player.lastname, player.fullname,
                      player.team, player.primarypos, player.secondarypos, player.height, player.weight,
                      player.country, player.birthdate, player.draftyear, player.draftround, player.draftpick,
                      player.experience, player.pie))
    db_connection.commit()


driver.quit()