class Contact(object):

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self) -> str:
        return (f'{self.name} {self.phone} {self.email}')

#test data
def main():

    c = Contact('Sue', '085-6442378', 'sue@eircom.net')

    assert(c.name == 'Sue')
    assert(c.phone == '085-6442378')
    assert(c.email == 'sue@eircom.net')

    print(c)

if __name__ == '__main__':
    main()