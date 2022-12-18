import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    '''CREATE DATABASE'''
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print("Error creating database: ", e)

    return connection

def create_table(connection, table):
    '''CREATE TABLE'''
    try:
        cursor = connection.cursor()
        cursor.execute(table)
    except Error as e:
        print("Error creating table: ", e)

def main():
    '''SETUP'''
    database = r"C:\Users\lanav\Documents\school\computer science\mark 3\DB\database.db" #path
    
    create_players_table = """
                        CREATE TABLE IF NOT EXISTS players(
                            username TEXT PRIMARY KEY,
                            password TEXT NOT NULL
                        );
                        """
    create_leaderboard_table = """
                        CREATE TABLE IF NOT EXISTS leaderboard(
                            rank INTEGER PRIMARY KEY,
                            score INTEGER NOT NULL,

                            username TEXT,
                            CONSTRAINT fk_players
                            FOREIGN KEY (username)
                            REFERENCES players(username)
                        );
                        """
    create_game_stats_table = """
                        CREATE TABLE IF NOT EXISTS game_stats(
                            gameID INTEGER PRIMARY KEY,
                            difficulty INTEGER NOT NULL,
                            time_taken INTEGER NOT NULL
                        );
                        """
    create_previous_games_table = """
                        CREATE TABLE IF NOT EXISTS previous_games(
                            username TEXT,
                            gameID INTEGER,
                            CONSTRAINT fk_players
                            FOREIGN KEY (username)
                            REFERENCES players(username)
                            CONSTRAINT fk_gameID
                            FOREIGN KEY (gameID)
                            REFERENCES game_stats(gameID)
                        );
                        """

    connection = create_connection(database)
    if connection is not None:
        create_table(connection, create_players_table)
        print("1/4 players")
        create_table(connection, create_leaderboard_table)
        print("2/4 leaderboard")
        create_table(connection, create_game_stats_table)
        print("3/4 game stats")
        create_table(connection, create_previous_games_table)
        print("4/4 previous games")
    else: 
        print("Error: No connection")

main()