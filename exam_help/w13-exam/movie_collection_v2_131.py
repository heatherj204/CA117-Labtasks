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

    def actors(self):
        actor_lst = []
        for movieTitle in self.collection:
            movie = self.collection[movieTitle]
            for actor in movie.cast:
                if actor not in actor_lst:
                    actor_lst.append(actor)
        return len(actor_lst)

    def __str__(self) -> str:
        return (f'Movies: {len(self.collection)}\nActors: {self.actors()}\nDuration: {self.get_hr_min()}')


# test data
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