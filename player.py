class Player:
    def __init__(self, name):
        self.name = name
        self.frames = []  # new player, so frames are empty

    def calc_score(self):
        score = 0
        for i, frame in enumerate(self.frames): # gives both index and frame value
            print(frame.balls, i) # testing - print out each frame
            # want to handle final frame first
            if i == 9:
                if frame.is_strike():
                    score += 10 + frame.balls[1] + frame.balls[2]
                elif frame.is_spare():
                    score += 10 + frame.balls[2]
                else:
                    score += frame.balls[0] + frame.balls[1]
            
            elif frame.is_strike():
                # strike gets 10 points, plus first roll in next frame
                score += 10 + self.frames[i + 1].balls[0]
                # if not a  strike in next frame
                if len(self.frames[i + 1].balls) > 1:
                    # just add both balls
                    score += self.frames[i + 1].balls[1]
                # if *is* a strike in next frame
                else:
                    # add score (10) from strike
                    score += self.frames[i + 2].balls[0]

            elif frame.is_spare():
                score += 10 + self.frames[i + 1].balls[0]

            else: 
                score += frame.balls[0] + frame.balls[1]

        return score