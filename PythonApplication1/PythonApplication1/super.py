class base(object):
    def pr(self):
        print("Base")

class B(base):
    def pr(self):
        super().pr()
        print("B")

class C(B):
    def pr(self):
        super().pr()
        print("C")

class D(B,C):
    def go(self):
        super().pr()
        print("D")


d=D()
d.go()
#Base
#B
#C
#D
