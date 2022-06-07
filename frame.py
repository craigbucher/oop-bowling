class Frame:
    def __init__(self, balls):
        self.balls = balls
        #example: [3, 7] is a spare
        #example: [10] is a strike
        
    def is_strike(self):
        return self.balls[0] == 10  # First ball equals 10

    def is_spare(self):
        return len(self.balls) > 1 and self.balls[0] + self.balls[1] == 10 # combination of both balls equals 10
