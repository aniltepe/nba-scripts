import os
import sqlite3
from datetime import datetime

class Season:
    def __init__(self, name, startdate_rs, enddate_rs, startdate_pi, enddate_pi, startdate_po, enddate_po, startdate_f, enddate_f):
        self.name = name
        self.startdate_rs = startdate_rs
        self.enddate_rs = enddate_rs
        self.startdate_pi = startdate_pi
        self.enddate_pi = enddate_pi
        self.startdate_po = startdate_po
        self.enddate_po = enddate_po
        self.startdate_f = startdate_f
        self.enddate_f = enddate_f

dir = os.path.dirname(__file__)
db_connection = sqlite3.connect(dir + "/nba.sqlite")
db_cursor = db_connection.cursor()

seasons = []

create_command = """CREATE TABLE IF NOT EXISTS season (
    name TEXT NOT NULL PRIMARY KEY,
    startdate_rs DATE NOT NULL,
    enddate_rs DATE NOT NULL,
    startdate_pi DATE,
    enddate_pi DATE,
    startdate_po DATE NOT NULL,
    enddate_po DATE NOT NULL,
    startdate_f DATE NOT NULL,
    enddate_f DATE NOT NULL)"""
db_cursor.execute(create_command)


seasons.append(Season("2003–04", datetime(2003, 10, 28).strftime("%Y-%m-%d"), datetime(2004, 4, 14).strftime("%Y-%m-%d"),
    None, None,
    datetime(2004, 4, 17).strftime("%Y-%m-%d"), datetime(2004, 6, 1).strftime("%Y-%m-%d"),
    datetime(2004, 6, 6).strftime("%Y-%m-%d"), datetime(2004, 6, 15).strftime("%Y-%m-%d")))
seasons.append(Season("2004–05", datetime(2004, 11, 2).strftime("%Y-%m-%d"), datetime(2005, 4, 20).strftime("%Y-%m-%d"),
    None, None,
    datetime(2005, 4, 23).strftime("%Y-%m-%d"), datetime(2005, 6, 6).strftime("%Y-%m-%d"),
    datetime(2005, 6, 9).strftime("%Y-%m-%d"), datetime(2005, 6, 23).strftime("%Y-%m-%d")))
seasons.append(Season("2005–06", datetime(2005, 11, 1).strftime("%Y-%m-%d"), datetime(2006, 4, 19).strftime("%Y-%m-%d"),
    None, None,
    datetime(2006, 4, 22).strftime("%Y-%m-%d"), datetime(2006, 6, 3).strftime("%Y-%m-%d"),
    datetime(2006, 6, 8).strftime("%Y-%m-%d"), datetime(2006, 6, 20).strftime("%Y-%m-%d")))
seasons.append(Season("2006–07", datetime(2006, 10, 31).strftime("%Y-%m-%d"), datetime(2007, 4, 18).strftime("%Y-%m-%d"),
    None, None,
    datetime(2007, 4, 21).strftime("%Y-%m-%d"), datetime(2007, 6, 2).strftime("%Y-%m-%d"),
    datetime(2007, 6, 7).strftime("%Y-%m-%d"), datetime(2007, 6, 14).strftime("%Y-%m-%d")))
seasons.append(Season("2007–08", datetime(2007, 10, 30).strftime("%Y-%m-%d"), datetime(2008, 4, 16).strftime("%Y-%m-%d"),
    None, None,
    datetime(2008, 4, 19).strftime("%Y-%m-%d"), datetime(2008, 5, 30).strftime("%Y-%m-%d"),
    datetime(2008, 6, 5).strftime("%Y-%m-%d"), datetime(2008, 6, 17).strftime("%Y-%m-%d")))
seasons.append(Season("2008–09", datetime(2008, 10, 28).strftime("%Y-%m-%d"), datetime(2009, 4, 16).strftime("%Y-%m-%d"),
    None, None,
    datetime(2009, 4, 18).strftime("%Y-%m-%d"), datetime(2009, 5, 30).strftime("%Y-%m-%d"),
    datetime(2009, 6, 4).strftime("%Y-%m-%d"), datetime(2009, 6, 14).strftime("%Y-%m-%d")))
seasons.append(Season("2009–10", datetime(2009, 10, 27).strftime("%Y-%m-%d"), datetime(2010, 4, 14).strftime("%Y-%m-%d"),
    None, None,
    datetime(2010, 4, 17).strftime("%Y-%m-%d"), datetime(2010, 5, 29).strftime("%Y-%m-%d"),
    datetime(2010, 6, 3).strftime("%Y-%m-%d"), datetime(2010, 6, 17).strftime("%Y-%m-%d")))
seasons.append(Season("2010–11", datetime(2010, 10, 26).strftime("%Y-%m-%d"), datetime(2011, 4, 13).strftime("%Y-%m-%d"),
    None, None,
    datetime(2011, 4, 16).strftime("%Y-%m-%d"), datetime(2011, 5, 26).strftime("%Y-%m-%d"),
    datetime(2011, 5, 31).strftime("%Y-%m-%d"), datetime(2011, 6, 12).strftime("%Y-%m-%d")))
seasons.append(Season("2011–12", datetime(2011, 12, 25).strftime("%Y-%m-%d"), datetime(2012, 4, 26).strftime("%Y-%m-%d"),
    None, None,
    datetime(2012, 4, 28).strftime("%Y-%m-%d"), datetime(2012, 6, 9).strftime("%Y-%m-%d"),
    datetime(2012, 6, 12).strftime("%Y-%m-%d"), datetime(2012, 6, 21).strftime("%Y-%m-%d")))
seasons.append(Season("2012–13", datetime(2012, 10, 30).strftime("%Y-%m-%d"), datetime(2013, 4, 17).strftime("%Y-%m-%d"),
    None, None,
    datetime(2013, 4, 20).strftime("%Y-%m-%d"), datetime(2013, 6, 3).strftime("%Y-%m-%d"),
    datetime(2013, 6, 6).strftime("%Y-%m-%d"), datetime(2013, 6, 20).strftime("%Y-%m-%d")))
seasons.append(Season("2013–14", datetime(2013, 10, 29).strftime("%Y-%m-%d"), datetime(2014, 4, 16).strftime("%Y-%m-%d"),
    None, None,
    datetime(2014, 4, 19).strftime("%Y-%m-%d"), datetime(2014, 5, 31).strftime("%Y-%m-%d"),
    datetime(2014, 6, 5).strftime("%Y-%m-%d"), datetime(2014, 6, 15).strftime("%Y-%m-%d")))
seasons.append(Season("2014–15", datetime(2014, 10, 28).strftime("%Y-%m-%d"), datetime(2015, 4, 15).strftime("%Y-%m-%d"),
    None, None,
    datetime(2015, 4, 18).strftime("%Y-%m-%d"), datetime(2015, 5, 27).strftime("%Y-%m-%d"),
    datetime(2015, 6, 4).strftime("%Y-%m-%d"), datetime(2015, 6, 16).strftime("%Y-%m-%d")))
seasons.append(Season("2015–16", datetime(2015, 10, 27).strftime("%Y-%m-%d"), datetime(2016, 4, 13).strftime("%Y-%m-%d"),
    None, None,
    datetime(2016, 4, 16).strftime("%Y-%m-%d"), datetime(2016, 5, 30).strftime("%Y-%m-%d"),
    datetime(2016, 6, 2).strftime("%Y-%m-%d"), datetime(2016, 6, 19).strftime("%Y-%m-%d")))
seasons.append(Season("2016–17", datetime(2016, 10, 25).strftime("%Y-%m-%d"), datetime(2017, 4, 12).strftime("%Y-%m-%d"),
    None, None,
    datetime(2017, 4, 15).strftime("%Y-%m-%d"), datetime(2017, 5, 25).strftime("%Y-%m-%d"),
    datetime(2017, 6, 1).strftime("%Y-%m-%d"), datetime(2017, 6, 12).strftime("%Y-%m-%d")))
seasons.append(Season("2017–18", datetime(2017, 10, 17).strftime("%Y-%m-%d"), datetime(2018, 4, 11).strftime("%Y-%m-%d"),
    None, None,
    datetime(2018, 4, 14).strftime("%Y-%m-%d"), datetime(2018, 5, 28).strftime("%Y-%m-%d"),
    datetime(2018, 5, 31).strftime("%Y-%m-%d"), datetime(2018, 6, 8).strftime("%Y-%m-%d")))
seasons.append(Season("2018–19", datetime(2018, 10, 16).strftime("%Y-%m-%d"), datetime(2019, 4, 10).strftime("%Y-%m-%d"),
    None, None,
    datetime(2019, 4, 13).strftime("%Y-%m-%d"), datetime(2019, 5, 25).strftime("%Y-%m-%d"),
    datetime(2019, 5, 30).strftime("%Y-%m-%d"), datetime(2019, 6, 13).strftime("%Y-%m-%d")))
seasons.append(Season("2019–20", datetime(2019, 10, 22).strftime("%Y-%m-%d"), datetime(2020, 3, 11).strftime("%Y-%m-%d"),
    datetime(2020, 7, 30).strftime("%Y-%m-%d"), datetime(2020, 8, 15).strftime("%Y-%m-%d"),
    datetime(2020, 8, 17).strftime("%Y-%m-%d"), datetime(2020, 9, 27).strftime("%Y-%m-%d"),
    datetime(2020, 9, 30).strftime("%Y-%m-%d"), datetime(2020, 10, 11).strftime("%Y-%m-%d")))
seasons.append(Season("2020–21", datetime(2020, 12, 22).strftime("%Y-%m-%d"), datetime(2021, 5, 16).strftime("%Y-%m-%d"),
    datetime(2021, 5, 18).strftime("%Y-%m-%d"), datetime(2021, 5, 21).strftime("%Y-%m-%d"),
    datetime(2021, 5, 22).strftime("%Y-%m-%d"), datetime(2021, 7, 6).strftime("%Y-%m-%d"),
    datetime(2021, 7, 8).strftime("%Y-%m-%d"), datetime(2021, 7, 22).strftime("%Y-%m-%d")))
seasons.append(Season("2021–22", datetime(2021, 10, 19).strftime("%Y-%m-%d"), datetime(2022, 4, 10).strftime("%Y-%m-%d"),
    datetime(2022, 4, 12).strftime("%Y-%m-%d"), datetime(2022, 4, 15).strftime("%Y-%m-%d"),
    datetime(2022, 4, 16).strftime("%Y-%m-%d"), datetime(2022, 5, 30).strftime("%Y-%m-%d"),
    datetime(2022, 6, 2).strftime("%Y-%m-%d"), datetime(2022, 6, 19).strftime("%Y-%m-%d")))

insert_command = "INSERT INTO season VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
for season in seasons:
    db_cursor.execute(insert_command,
        (season.name, season.startdate_rs, season.enddate_rs, season.startdate_po, season.enddate_po, season.startdate_f, season.enddate_f))
db_connection.commit()