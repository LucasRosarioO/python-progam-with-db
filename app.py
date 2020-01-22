import sqlite3

conn = sqlite3.connect('games.db')

cursor = conn.cursor()

# cursor.execute("""CREATE TABLE games(
#      name string,
#      finished string,
#      rating interger
#  )""")

class Game:
    """A sample game class"""

    def __init__(self, name, finished, rating):
        self.name = name
        self.finished = finished
        self.rating = rating



game = Game

choice = 0

while choice != 4:


    print('''
        ====== 2019 GAMES ======
            1 - Add game
            2 - View games list
            3 - Delete game
            4 - Exit
    ''')

    choice = input('Make your choice:')

    if choice == 1:
        game.name        = raw_input("Game Name: ")
        game.finished    = raw_input("Finished the game?: ")
        game.rating      = raw_input("Rating: ")

        cursor.execute("""INSERT INTO games (name, finished, rating)
             VALUES (?,?,?)""", (game.name, game.finished, game.rating))
             
        conn.commit()

    if choice == 2:
        print("Name             Finished    Rating")
        cursor.execute("SELECT * FROM games ")
        for linha in cursor.fetchall():
            print(linha)
        print('\n\n\n\n')

    if choice == 3:
        cursor.execute("""SELECT * FROM games;""")
        for linha in cursor.fetchall():
            print(linha)
        game.name = raw_input('\nType game name to be deleted: ')
        cursor.execute("""DELETE FROM games WHERE name = ?""", (game.name,))
        conn.commit()
        print('Game deleted!')
        print('\n\n\n\n')

print("Exiting...")