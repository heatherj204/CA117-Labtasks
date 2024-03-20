class Meeting(object):

    def __init__(self, hour, minute, duration) -> None:
        self.hour = hour
        self.minute = minute
        self.duration = duration

    def __str__(self) -> str:
        return f'{self.hour:02}:{self.minute:02} ({self.duration} minutes)'
#test data
# def main():

#     m = Meeting(9, 5, 30)

#     assert(m.hour == 9)
#     assert(m.minute == 5)
#     assert(m.duration == 30)

#     print(m)

# if __name__ == '__main__':
#     main()