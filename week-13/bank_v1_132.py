class Customer(object):

    def __init__(self, name, number, balance=0.00) -> None:
        self.name = name
        self.number = number
        self.balance = balance

    def __str__(self) -> str:
        return (f'Name: {self.name}\nNumber: {self.number}\nBalance: {self.balance:0.2f}')

class Bank(object):
    def __init__(self) -> None:
        self.customers = {}

    def add(self, c):
        self.customers[c.number] = c

    def lookup(self, number):
        if number in self.customers:
            return self.customers[number]
        return None

    def remove(self, number):
        if number in self.customers:
            self.customers.pop(number)

# test data
def main():
    c1 = Customer('Alan Wren', 12434655, 100.00)
    c2 = Customer('John Squire', 54211677, 200.22)

    b = Bank()

    b.add(c1)
    b.add(c2)

    c = b.lookup(12434655)
    assert(isinstance(c, Customer))
    assert(c.name == 'Alan Wren')
    assert(c.number == 12434655)
    assert(c.balance == 100.00)

    b.remove(12434655)
    c = b.lookup(12434655)
    assert(c is None)

if __name__ == '__main__':
    main()