import random

games = [
        "CSGO",
        "Overcooked 2",
        "Rocket League",
        "Fistful of Frags"
        ]

friends = [
        "friend1",
        "friend2",
        "friend3",
        "friend4",
        "Filetito",
        "no one",
        "a random guy you find on a match"
        ]

random_game = random.choice(games)
random_friend = random.choice(friends)

print(f"Today you will play {random_game} with {random_friend}. Have fun!")
