class FooParent(object):
    def a(self):
        print ('Parent')
 
class FooChild(FooParent):
    def b(self):
        # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类B的对象 FooChild 转换为类 FooParent 的对象
        #还可以写成super().a()
        super().a()    
        print ('Child')

class FooGrandson(FooChild):
    def d(self):
        super().a()#如例所示,如果在上一个继承中没有找到对应的函数
        #super()就会在上上个继承中继续找,以此类推
        print ('GrandSon')



c=FooChild()
c.b()

e=FooGrandson()
e.d()