class Score(object):

    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def __str__(self):
        return '{} goal(s) and {} point(s)'.format(self.goals, self.points)

    def score2points(self):
        return self.goals * 3 + self.points

    def __eq__(self, other):
        return self.score2points() == other.score2points()

    def __gt__(self, other):
        return self.score2points() > other.score2points()

    def __ge__(self, other):
        return self.score2points() >= other.score2points()

    def __add__(self, other):
        totalGoals = self.goals + other.goals
        totalPoints = self.points + other.points
        return Score(totalGoals, totalPoints)

    def __iadd__(self, other):
        self.goals += other.goals
        self.points += other.points
        return self


#test info
# def main():

#     s1 = Score()
#     s2 = Score(3, 12)
#     s3 = Score(4, 9)
#     s4 = Score(1, 1)

#     s5 = s3 + s4
#     print(s5)
#     assert(isinstance(s5, Score))
#     assert(s5 is not s3)
#     assert(s5 is not s4)

#     before = s2
#     s2 += s4
#     print(s2)
#     assert(isinstance(s2, Score))
#     assert(s2 is before)
#     assert(s2 is not s4)

# if __name__ == '__main__':
#     main()