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


#test info
# def main():

#     s1 = Score()
#     s2 = Score(3, 12)
#     s3 = Score(4, 9)

#     assert(s1 < s2)
#     assert(s1 <= s2)
#     assert(s2 > s1)
#     assert(s2 >= s1)
#     assert(s1 != s2)
#     assert(s2 == s3)

# if __name__ == '__main__':
#     main()