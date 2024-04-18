class Customer(object):

    def __init__(self, name, number, balance=0.00) -> None:
        self.name = name
        self.number = number
        self.balance = balance

    def lodge(self, money):
        self.balance = self.balance + money

    def withdraw(self, money):
        if money <= self.balance:
            self.balance = self.balance - money

    def __str__(self) -> str:
        return (f'Name: {self.name}\nNumber: {self.number}\nBalance: {self.balance:0.2f}')


#test data
def main():
    c1 = Customer('Alan Wren', 12434655, 100.00)

    c1.lodge(1.11)
    print(c1)

    c1.withdraw(200)
    print(c1)

    c1.withdraw(2)
    print(c1)

if __name__ == '__main__':
    main()