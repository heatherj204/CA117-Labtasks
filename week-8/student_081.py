class Student(object):

    def set_attributes(self, sid, name, modlist):
        self.sid = sid
        self.name = name
        self.modlist = modlist

    def print_attributes(self):
        print(f'ID: {self.sid}')
        print(f'Name: {self.name}')
        print('Modules:', ', '.join(self.modlist))

    def add_module(self, module):
        self.modlist.append(module)

    def del_module(self, module):
        self.modlist.remove(module)
