class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.times = {}

    def add_time(self, d, t):
        self.times[d] = t

    def get_time(self, d):
        return self.times[d]

    def total_time(self):
        return sum(self.times.values())

    def __str__(self):
        output = []
        output.append('Name: {}'.format(self.name))
        output.append('ID: {}'.format(self.tid))
        output.append('Race time: {}'.format(self.total_time()))
        return '\n'.join(output)

    def __eq__(self, other):
        return self.total_time() == other.total_time()

    def __gt__(self, other):
        return self.total_time() > other.total_time()

def sort_on(t):
    return t.name
    # return t.tid

# TODO: Extend Triathlon class
class Triathlon(object):

    def __init__(self):
        self.d = {}

    def add(self, t):
        # we want to map from t's tid to t
        # t is an instance of Triathlete
        self.d[t.tid] = t

    def remove(self, tid):
        del(self.d[tid])

    def lookup(self, tid):
        # do we have a mapping from tid to a t?
        if tid in self.d:
            return self.d[tid]
        return None

    def __str__(self):
        output = ['{}'.format(t) for t in sorted(self.d.values(), key=sort_on)]
        return '\n'.join(output)

    def best(self):
        return min(self.d.values())

    def worst(self):
        return max(self.d.values())

#test data
# from triathlon_v3_121 import Triathlete, Triathlon

# def main():

#     tn = Triathlon()
#     t1 = Triathlete('Ian Brown', 21)
#     t2 = Triathlete('John Squire', 22)
#     t3 = Triathlete('Alan Wren', 23)

#     t1.add_time('swim', 100)
#     t1.add_time('cycle', 120)
#     t1.add_time('run', 150)

#     t2.add_time('swim', 300)
#     t2.add_time('cycle', 100)
#     t2.add_time('run', 200)

#     t3.add_time('swim', 50)
#     t3.add_time('cycle', 20)
#     t3.add_time('run', 10)

#     tn.add(t1)
#     tn.add(t2)
#     tn.add(t3)

#     print(tn.best())
#     print(tn.worst())

# if __name__ == '__main__':
#     main()