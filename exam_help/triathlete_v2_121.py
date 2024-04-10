class Triathlete(object):

    def __init__(self, name, tid) -> None:
        self.name = name
        self.tid = tid
        self.times = {}

    def add_time(self, disaplin, t):
        self.times[disaplin] = t

    def get_time(self, d):
        return self.times[d]

    def get_total(self):
        return sum(self.times.values())

    def __str__(self) -> str:
        return (f'Name: {self.name}\nID: {self.tid}\nRace time: {self.get_total()}')

# test data
def main():

    t1 = Triathlete('Ian Brown', 21)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    print('Cycle: {}'.format(t1.get_time('cycle')))
    print(t1)

if __name__ == '__main__':
    main()