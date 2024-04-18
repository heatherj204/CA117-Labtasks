class MP3Track(object):

    def __init__(self, title, duration, artist):
        self.title = title
        self.duration = duration
        self.artist = artist

    def __str__(self):
        return f'Title: {self.title}\nBy: {", ".join(self.artist)}\nDuration: {self.duration}'

class MP3Collection(object):

    def __init__(self):
        self.collection = {}

    def add(self, song):
        self.collection[song.title] = song

    def remove(self, title):
        if title in self.collection:
            del(self.collection[title])

    def lookup(self, title):
        if title in self.collection:
            return self.collection[title]
        return None

    def __add__(self, other):
        c = MP3Collection()

        for track in self.collection.values():
            c.add(track)

        for track in other.collection.values():
            c.add(track)

        return c


# test data
from mp3collection_v2_122 import MP3Track, MP3Collection

def main():
    t1 = MP3Track('Fools Gold', 604, ['The Stone Roses'])
    t2 = MP3Track('Shallow', 197, ['Lady Gaga', 'Bradley Cooper'])
    t3 = MP3Track('Telephone', 220, ['Beyonce', 'Lady Gaga'])

    c1 = MP3Collection()
    c1.add(t1)
    c1.add(t2)

    c2 = MP3Collection()
    c2.add(t3)

    # Make a new collection from two existing ones
    c3 = c1 + c2
    assert(isinstance(c3, MP3Collection))
    assert(c3 is not c1)
    assert(c3 is not c2)

if __name__ == '__main__':
    main()