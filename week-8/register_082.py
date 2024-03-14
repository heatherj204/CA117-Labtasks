class CashRegister(object):
    def __init__(self):
        self.total = 0
        self.count = 0

    def add_item(self, item):
        self.total += item
        self.count += 1

    def clear(self):
        self.total = 0
        self.count = 0

    def __str__(self):
        return f"Items: {self.count}\nTotal: {self.total:.2f}"
