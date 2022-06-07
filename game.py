import random

def lucky_rand(n):
    return max(random.randint(0,n), random.randint(0, n)) # takes largest of two randoms (to simulate good bowlers)

class Game:
    def __init__(self, players):
        self.players = players
        self.current_frame = 0

    def play(self):
        for i in range(10):     # not even using 'i', just doing something 10 times
            self.bowl_frame()
        for player in self.players:
            print(f'The final score for {player.name} is {player.calc_score()}.') # Never actually saving the score - just calculate it from raw data whenever it's needed

    def bowl_frame(self):
        # if self.current_frame <= 9:
            self.current_frame += 1
            for player in self.players:
                balls = []

                #first throw
                balls.append(lucky_rand(10))
                if balls [0] < 10:          # Did not get a strike, so get second ball
                    balls.append(lucky_rand(10 - balls[0]))

                    #on the final frame of the game, get a third ball if roll a spare
                    if balls[0] + balls[1] == 10 and self.current_frame == 10:
                        balls.append(lucky_rand(10))

                #if they get a strike on the last frame, they get 2 exta balls
                if balls[0] == 10 and self.current_frame == 10:
                    balls.append(lucky_rand(10))
                    # if first 10th frame roll is a strike, reset to 10 pins
                    if balls[1] == 10:
                        balls.append(lucky_rand(10))
                    # if first 10th frame roll is not a strike, use remaining pins
                    else:
                        balls.append(lucky_rand(10 - balls[1]))

                player.frames.append(Frame(balls))