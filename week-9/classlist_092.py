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

class Classlist(object):

    def __init__(self) -> None:
        self.students = {}

    def add(self, s):
        self.students[s.sid] = s

    def __str__(self) -> str:
        lines = []
        sortedDict = dict(sorted(self.students.items(), key=lambda i: i[1].average, reverse=True))
        for student in sortedDict.values():
            lines.append(str(student))

        return "\n".join(lines)

#test data
def main():

    cl = Classlist()

    s1 = Student('Hortense', 22217654, [('CA116', 70), ('CA117', 60)])
    s2 = Student('Bella', 22218393, [('CA177', 70), ('CA117', 81)])

    cl.add(s1)
    cl.add(s2)

    print(cl)


if __name__ == '__main__':
    main()