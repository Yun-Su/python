class A():
    def go(self):
        print ("class A")
class B(A):
    def go(self):
        super(B, self).go()
        print ("class B")
class C(A):
    def go(self):
        super(C, self).go()
        print ("class C")
class D(B,C):#从左到右执行,优先递归查找父类中的方法(如果有),并执行,然后递归查找父类中的属性,并执行,最后运行实例本身的属性和方法
    def go(self):
        super(D, self).go()
        print ("class D")

a = A()
b = B()
c = C()
d = D()

d.go()
#A C B D
#此处先执行父类B中方法,类B中执行父类A的继承输出'A'
#然后执行父类C中的方法,类C中执行父类A的继承,因为已经继承执行了一次,跳转执行方法中的属性'C'然后再跳转执行类B中未执行的属性'B'
#最后执行类D的属性'D'
######################原则##########################
#super类似于嵌套的一种设计，当代码执行到super实例化后，
#super()函数优先执行被继承的父类,然后执行父类中的实例,最后执行自身的方法.
#子类在父类前，所有类不重复调用，从左到右



class Base:
    def __init__(self):
        print('Base')

class A(Base):
    def __init__(self):
        super().__init__()
        print('A')

class B(Base):
    def __init__(self):
        super().__init__()
        print('B')

class C(A,B):
    def __init__(self):
        super().__init__()  # Only one call to super() here
        print('C')

c=C()
#base
#B
#A
#C


