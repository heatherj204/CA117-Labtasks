class Student(object):
    def __init__(self, name, sid, mark) -> None:
        self.name = name
        self.sid = sid

        self.grades = []
        self.modules = []

        for mod in mark:
            self.modules.append(mod[0])
            self.grades.append(int(mod[1]))

        self.average = sum(self.grades) / len(self.grades)

    def __str__(self):
        return f'Name: {self.name}\nID: {self.sid}\nModules: {", ".join(sorted(self.modules))}\nAverage mark: {round(self.average)}'

#test data
# def main():

#     s1 = Student('Hortense', 22217654, [('CA116', 70), ('CA117', 60)])
#     s2 = Student('Bella', 22218393, [('CA177', 70), ('CA117', 81)])

#     print(s1)
#     print(s2)

# if __name__ == '__main__':
#     main()