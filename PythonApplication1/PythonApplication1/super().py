class A(object):
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
class D(B,C):
    def go(self):
        super(D, self).go()
        print ("class D")

a = A()
b = B()
c = C()
d = D()

d.go()
#此处先执行父类B中方法,类B中执行父类A的继承输出'go A go'
#然后执行父类C中的方法,类C中执行父类A的继承,因为已经继承执行了一次,跳转执行方法中的属性'go C go'然后再跳转执行类B中未执行的属性'go b go'
#最后执行类D的属性'go D go'
######################原则##########################
#super类似于嵌套的一种设计，当代码执行到super实例化后，
#先去找同级父类，若没有其余父类，再执行自身父类，再往下走，
#子类在父类前，所有类不重复调用，从左到右

