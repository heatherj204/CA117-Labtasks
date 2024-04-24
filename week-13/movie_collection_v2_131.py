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
        actors = []
        mins_duration = 0
        for movieTitle in self.collection:
            movie = self.collection[movieTitle]
            mins_duration = mins_duration + movie.duration
            for actor in movie.d:
                if actor not in actors:
                    actors.append(actor)
        hours, minutes = divmod(mins_duration, 60)

        return (f"Movies: {len(self.collection)}\nActors: {len(actors)}\nDuration: {hours:01} hour(s) {minutes:02} minute(s)")

#test data
from movie_collection_v2_131 import Actor, Movie, MovieCollection

def main():
    a1 = Actor('Cillian Murphy', 'Ireland', 5000)
    a2 = Actor('Florence Pugh', 'UK', 6000)
    a3 = Actor('Franka Potente', 'Germany', 3000)
    a4 = Actor('Matt Damon', 'USA', 12000)

    m1 = Movie(title='Oppenheimer', duration=180)
    m1.add(a1)
    m1.add(a2)
    m1.add(a4)

    mc = MovieCollection()

    mc.add(m1)
    print(mc)

    m2 = Movie(title='The Bourne Identity', duration=125)
    m2.add(a3)
    m2.add(a4)

    mc.add(m2)
    print(mc)

if __name__ == '__main__':
    main()