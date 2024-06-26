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

    def __eq__(self, other):
        return self.get_total() == other.get_total()

    def __gt__(self, other):
        return self.get_total() > other.get_total()


# Test Data
def main():

    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)
    t3 = Triathlete('Alan Wren', 23)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    t2.add_time('swim', 300)
    t2.add_time('cycle', 100)
    t2.add_time('run', 200)

    t3.add_time('swim', 150)
    t3.add_time('cycle', 120)
    t3.add_time('run', 100)

    print(t1)
    print(t2)
    print(t3)

    assert(t1 == t3)
    assert(t1 < t2)
    assert(t2 > t3)

if __name__ == '__main__':
    main()