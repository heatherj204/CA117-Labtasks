class Meeting(object):

    def __init__(self, hour, minute, duration) -> None:
        self.hour = hour
        self.minute = minute
        self.duration = duration

    def __str__(self) -> str:
        return f'{self.hour:02}:{self.minute:02} ({self.duration} minutes)'

class Schedule(object):
    def __init__(self) -> None:
        self.meetings = []

    def add(self, meet):
        self.meetings.append(meet)

    def __str__(self) -> str:
        lines = []
        lines.append('Schedule')
        lines.append('--------')
        all_meetings = []
        for i in self.meetings:
            all_meetings.append(str(i))
        all_meetings.sort()
        lines = lines + all_meetings
        total_meet = len(all_meetings)
        lines.append(f'Meetings today: {total_meet}')
        return '\n'.join(lines)

#test data
def main():
    schedule = Schedule()

    m = Meeting(13, 0, 15)
    schedule.add(m)

    m = Meeting(9, 5, 30)
    schedule.add(m)

    m = Meeting(16, 30, 5)
    schedule.add(m)

    print(schedule)

if __name__ == '__main__':
    main()