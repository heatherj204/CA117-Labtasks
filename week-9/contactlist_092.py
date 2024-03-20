class Contact(object):

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self) -> str:
        return (f'{self.name} {self.phone} {self.email}')

class Contactlist(object):

    def __init__(self) -> None:
        self.d = {}

    def add(self, contact:Contact):
        self.d[contact.name] = contact

    def get(self, name):
        if name in self.d:
            return self.d[name]
        return None

    def remove(self, name):
        if name in self.d:
            self.d.pop(name)

    def __str__(self) -> str:
        lines = []
        lines.append('Contact list')
        lines.append('------------')
        contacts = []
        for i in self.d.values():
            contacts.append(str(i))
        contacts.sort()
        lines = lines + contacts
        return '\n'.join(lines)
#test data
# def main():
#     clist = Contactlist()

#     c1 = Contact('Sue', '085-6442378', 'sue@eircom.net')
#     clist.add(c1)

#     c2 = Contact('Jimmy', '086-1223277', 'james@apple.com')
#     clist.add(c2)

#     c3 = Contact('Wendy', '086-9112645', 'wendy@physics.dcu.ie')
#     clist.add(c3)

#     c = clist.get('Wendy')
#     assert(c is c3)

#     clist.remove('Wendy')
#     c = clist.get('Wendy')
#     assert(c is None)

#     c4 = Contact('Abbey', '087-7586344', 'abbey@gmail.com')
#     clist.add(c4)

#     print(clist)

# if __name__ == '__main__':
#     main()