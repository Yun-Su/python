class FooParent(object):
    def a(self):
        print ('Parent')
 
class FooChild(FooParent):
    def b(self):
        # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类B的对象 FooChild 转换为类 FooParent 的对象
        #还可以写成super().a()
        super().a()    
        print ('Child')

c=FooChild()
c.b()