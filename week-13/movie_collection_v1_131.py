class Actor(object):

    def __init__(self, name, nationality, fee):
        self.name = name
        self.nationality = nationality
        self.fee = fee

    def __str__(self):
        return (f'Name: {self.name}\nNationality: {self.nationality}\nFee: {self.fee}')

class Movie(object):

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        self.d = {}

    def add(self, a):
        self.d[a.name] = a

    def remove(self, name):
        if name in self.d:
            self.d.pop(name)

    def payroll(self):
        amount = 0
        for actor in self.d:
            amount += self.d[actor].fee
        return amount

    def __str__(self):
        return (f'Title: {self.title}\nDuration: {self.duration} minute(s)\nCast: {", ".join(sorted(self.d))}\nPayroll: {self.payroll()}')

class MovieCollection(object):
    def __init__(self) -> None:
        self.collection = {}

    def add(self, m):
        self.collection[m.title] = m

    def __str__(self):
        mins_duration = 0
        for movieTitle in self.collection:
            movie = self.collection[movieTitle]
            mins_duration = mins_duration + movie.duration
        hours, minutes = divmod(mins_duration, 60)

        return (f"Movies: {len(self.collection)}\nDuration: {hours:01} hour(s) {minutes:02} minute(s)")

#test data
from movie_collection_v1_131 import Movie, MovieCollection

def main():
    m1 = Movie(title='Oppenheimer', duration=180)
    m2 = Movie(title='Dune 2', duration=165)

    mc = MovieCollection()

    mc.add(m1)
    mc.add(m2)
    print(mc)

if __name__ == '__main__':
    main()