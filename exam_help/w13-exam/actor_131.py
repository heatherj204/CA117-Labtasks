class Actor(object):

    def __init__(self, name, nationality, fee) -> None:
        self.name = name
        self.nationality = nationality
        self.fee = fee

    def __str__(self) -> str:
        return(f'Name: {self.name}\nNationality: {self.nationality}\nFee: {self.fee}')
#test data
from actor_131 import Actor

def main():
    a1 = Actor('Cillian Murphy', 'Ireland', 5000)
    a2 = Actor('Florence Pugh', 'UK', 6000)

    assert(isinstance(a1, Actor))
    assert(a1.name == 'Cillian Murphy')
    assert(a1.nationality == 'Ireland')
    assert(a1.fee == 5000)

    print(a1)
    print(a2)

if __name__ == '__main__':
    main()