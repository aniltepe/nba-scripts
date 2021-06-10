class Statistic:
    def __init__(self, code, name):
        self.code = code
        self.name = name


statistics = []


def create_statistics():
    create_command = "CREATE TABLE IF NOT EXISTS statistics (code TEXT NOT NULL PRIMARY KEY, name TEXT NOT NULL)"
    db_cursor.execute(create_command)
    statistics.append(Statistic("Min", "Minutes Played"))
    statistics.append(Statistic("2PM", "2 Points Made"))
    statistics.append(Statistic("2PA", "2 Points Attempted"))
    statistics.append(Statistic("3PM", "3 Points Made"))
    statistics.append(Statistic("3PA", "3 Points Attempted"))
    statistics.append(Statistic("FTM", "Free Throws Made"))
    statistics.append(Statistic("FTA", "Free Throws Attempted"))
    statistics.append(Statistic("OREB", "Offensive Rebounds"))
    statistics.append(Statistic("DREB", "Deffensive Rebounds"))
    statistics.append(Statistic("AST", "Assists"))
    statistics.append(Statistic("STL", "Steals"))
    statistics.append(Statistic("BLK", "Blocks"))
    statistics.append(Statistic("TO", "Turnovers"))
    statistics.append(Statistic("PF", "Personal Fouls"))
    statistics.append(Statistic("PITP", "Points In The Paint"))
    statistics.append(Statistic("FBPS", "Fast Break Points"))
    statistics.append(Statistic("BNCPS", "Bench Points"))
    statistics.append(Statistic("BIGLD", "Biggest Lead"))
    statistics.append(Statistic("TMREB", "Team Rebounds"))
    statistics.append(Statistic("TMTO", "Team Turnovers"))
    statistics.append(Statistic("PSOFTO", "Points Off Turnovers"))
    insert_command = "INSERT INTO statistics VALUES (?, ?)"
    for stat in statistics:
        db_cursor.execute(insert_command, stat)
    db_connection.commit()