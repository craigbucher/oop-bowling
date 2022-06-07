from game import Game
from frame import Frame
from player import Player



players = []
for player in ['Alice', 'Bob', 'Carol', 'Dan']: #  "should really be a map, not a for loop"
    players.append(Player(player))
the_game = Game(players)
the_game.play()

print('finished bowling')
