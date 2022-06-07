class Game:
    def __init__(self, players):
        self.players = players
        self.current_frame = 0

    def play(self):
        for i in range(10):
            self.bowl_frame()
        for players in self.players:
            print(f'The final score for {player.name} is {player.calc_score()}.') # Never actually saving the score - just calculate it from raw data whenever it's needed

    def bowl_fram(self):
        if self.current_frame <= 9:
            self.current_frame += 1
            for player in self.players:
                

class Player:
    def __init__(self, name):
        self.name = name
        self.frames = []  # new player, so frames are empty

    def calc_score(self):
        score = 0
        for i, frame in enumerate(self.frames) # gives both index and frame value
            pass
        return score
        
class Frame:
    def __init__(self, balls):
        self.balls = balls
        #example: [3, 7] is a spare
        #example: [10] is a strike
        
    def is_strike(self):
        return self.balls[0] == 10  # First ball equals 10

    def is_spare(self):
        return len(self.balls) > 1 and self.balls[0] + self.balls[1] == 10 # combination of both balls equals 10


#firstFrame = Frame([3,6]) # example frame