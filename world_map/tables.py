import sqlite3


PATH_DB = "world_map.db"

connection = sqlite3.connect(PATH_DB)

cursor = connection.cursor()


# cream tabelul continents
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS continents(
    continent_id INTEGER PRIMARY KEY AUTOINCREMENT,
    continent_name TEXT NOT NULL,
    continent_code TEXT NOT NULL CHECK(LENGTH(continent_code) = 2)
    );
    '''
)


# cream tabelul countries
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS countries(
    country_code TEXT NOT NULL PRIMARY KEY CHECK(LENGTH(country_code) = 2),
    country_name TEXT NOT NULL,
    continent_id INTEGER,
    population INTEGER NOT NULL,
    FOREIGN KEY (continent_id) REFERENCES continents(continent_id)
    );
    '''
)


connection.commit()
# connection.close() # !!! if connection = closed then sql script from continents.py (for example) won't be able to run
