class MP3Track(object):

    def __init__(self, title, duration, artist):
        self.title = title
        self.duration = duration
        self.artist = artist

    def sec_to_min(self):
        time = self.duration
        seconds = time % 60
        mins = time // 60
        return f'{mins:0>}:{seconds:0>2}'

    def __str__(self):
        return f'Title: {self.title}\nBy: {", ".join(self.artist)}\nDuration: {self.sec_to_min()}'

# Test Data
def main():
    t1 = MP3Track('Fools Gold', 604, ['The Stone Roses'])
    t2 = MP3Track('Shallow', 197, ['Lady Gaga', 'Bradley Cooper'])
    t3 = MP3Track('Telephone', 220, ['Beyonce', 'Lady Gaga'])
    t4 = MP3Track('Her Majesty', 34, ['The Beatles'])
    t5 = MP3Track('Seven Seconds', 7, ['Neneh Cherry'])

    print(t1)
    print(t2)
    print(t3)
    print(t4)
    print(t5)

if __name__ == '__main__':
    main()