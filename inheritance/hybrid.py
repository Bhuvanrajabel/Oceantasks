class A:
    def a(self):
        print("Method from class A")


class B(A):
    def b(self):
        print("Method from class B")


class C:
    def c(self):
        print("Method from class C")


class D(B, C):  
    def d(self):
        print("Method from class D")


d = D()
d.a()
d.b()
d.c()
d.d()
