class Parent:
    def override(self):
        print('Rodzic override()')

class Child(Parent):
    def override(self):
        print('dziecko przed override() rodzica')
        super(Child, self).override()
        print('diecko po override() rodzica ')

dad = Parent()
son = Child()
dad.override()
son.override()