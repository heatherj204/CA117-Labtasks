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

class MovieCollection(object):
    def __init__(self) -> None:
        self.collection = {}

    def add(self, movie):
        self.collection[movie.title] = movie

    def get_hr_min(self):
        mins_duration = 0
        for movieTitle in self.collection:
            movie = self.collection[movieTitle]
            mins_duration = mins_duration + movie.duration
        hours, minutes = divmod(mins_duration, 60)
        return f'{hours:01} hour(s) {minutes:02} minute(s)'

    def __str__(self) -> str:
        return (f'Movies: {len(self.collection)}\nDuration: {self.get_hr_min()}')

# test data
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