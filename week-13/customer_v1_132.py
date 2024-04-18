class Customer(object):

    def __init__(self, name, number, balance=0.00) -> None:
        self.name = name
        self.number = number
        self.balance = balance

    def __str__(self) -> str:
        return (f'Name: {self.name}\nNumber: {self.number}\nBalance: {self.balance:0.2f}')
#test data
from customer_v1_132 import Customer

def main():
    c1 = Customer('Alan Wren', 12434655, 100.00)
    c2 = Customer('John Squire', 54211677, 200.22)
    c3 = Customer('Ian Brown', 89766121)

    assert(c1.name == 'Alan Wren')
    assert(c1.number == 12434655)
    assert(c1.balance == 100.00)

    print(c1)
    print(c2)
    print(c3)

if __name__ == '__main__':
    main()