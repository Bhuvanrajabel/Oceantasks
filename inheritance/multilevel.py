class Grandparent:
    def grandparent(self):
        print("He is my grandfather")

class parents(Grandparent):
    def parents(self):
        print("They are my parents")

class child(parents):
    def child(self):
        print("Im the child")

a=child()
a.grandparent()
a.parents()
a.child()