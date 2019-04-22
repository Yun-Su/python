class Parent(object):
    def a(self):
        print ('Parent')
 
class Child(Parent):
    def a(self):
        # super(Child,self)首先找到 Child 的父类(就是Parent),然后把类B的对象Child 转换为类Parent的对象
        #还可以写成super().a()
        super().a()  
        print ('Child')

class Grandson(Child):
    def a(self):
        super().a()#如例所示,如果在上一个继承中没有找到对应的函数
        #super()就会在上上个继承中继续找,以此类推
        print ('GrandSon')

c=Child()
c.a()
print('_________')
g=Grandson()
g.a()
print('_________')

#Parent
#Child
#______
#Parent
#Child
#Grandson