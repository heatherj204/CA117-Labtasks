class Triathlete(object):

    def __init__(self, name, tid) -> None:
        self.name = name
        self.tid = tid

    def __str__(self) -> str:
        return (f'Name: {self.name}\nID: {self.tid}')

class Triathlon(object):

    def __init__(self) -> None:
        self.d = {}

    def add(self, person):
        self.d[person.tid] = person

    def remove(self, tid):
        del(self.d[tid])

    def lookup(self, tid):
        if tid in self.d:
            return self.d[tid]
        return None

# test data
from triathlon_v1_121 import Triathlete, Triathlon

def main():

    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)

    tn.add(t1)
    tn.add(t2)

    t = tn.lookup(21)
    assert(isinstance(t, Triathlete))
    assert(t.name == 'Ian Brown')
    assert(t.tid == 21)

    tn.remove(21)
    t = tn.lookup(21)
    assert(t is None)

if __name__ == '__main__':
    main()