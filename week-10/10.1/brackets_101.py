class Stack(object):

    def __init__(self) -> None:
        self.l = []

    def push(self, e):
        self.l.append(e)

    def top(self):
        return self.l[-1]

    def pop(self):
        return self.l.pop()

    def is_empty(self):
        return len(self.l) == 0

    def __len__(self):
        return len(self.l)

def matcher(line):
    st = Stack()
    left = {'(': ')', '[': ']', '{': '}'}
    right = {')': '(', ']': '[', '}': '{'}
    try:
        for char in line:
            if char in left:
                st.push(char)
            elif char in right and st.top() == right[char]:
                st.pop()
    except:
        return False
    return st.is_empty()

#test data
# import sys
# tests = ['()',
# '(())',
# '(({}))',
# '(())(){}{(([]))}',
# '(()',
# '(()){()]',
# ')(()){([()])}']

# def main():

#     for test in tests:
#         print(matcher(test.strip()))

# if __name__ == '__main__':
#     main()