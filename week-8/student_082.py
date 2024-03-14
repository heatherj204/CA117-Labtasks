class Student(object):
    def __init__(self, sid, name, modlist=None):
        self.sid = sid
        self.name = name
        if modlist:
            self.modlist = modlist
        else:
            self.modlist = []

    def add_module(self, mod):
        if mod not in self.modlist:
            self.modlist.append(mod)

    def del_module(self, mod):
        if mod in self.modlist:
            self.modlist.remove(mod)

    def __str__(self):
        return f"ID: {self.sid}\nName: {self.name}\nModules: {', '.join(sorted(self.modlist))}"
