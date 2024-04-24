class Actor(object):

    def __init__(self, name, nationality, fee) -> None:
        self.name = name
        self.nationality = nationality
        self.fee = fee

    def __str__(self) -> str:
        return(f'Name: {self.name}\nNationality: {self.nationality}\nFee: {self.fee}')

class Movie(object):

    def __init__(self, title, duration) -> None:
        self.title = title
        self.duration = duration
        self.cast = {}

    def add(self, actor):
        self.cast[actor.name] = actor

    def remove(self, actor):
        if actor in self.cast:
            self.cast.pop(actor)

    def lookup(self, name):
        if name in self.cast:
            return self.cast[name]
        return None

    def payroll(self):
        amount = 0
        for actor in self.cast:
            amount += self.cast[actor].fee
        return amount

    def __str__(self) -> str:
        return (f'Title: {self.title}\nDuration: {self.duration} minute(s)\nCast: {", ".join(sorted(self.cast))}\nPayroll: {self.payroll()}')

# test data
from movie_v2_131 import Actor, Movie

def main():
    a1 = Actor('Cillian Murphy', 'Ireland', 5000)
    a2 = Actor('Florence Pugh', 'UK', 6000)

    m = Movie(title='Oppenheimer', duration=180)

    print(m)

    m.add(a1)
    m.add(a2)

    print(m)

if __name__ == '__main__':
    main()