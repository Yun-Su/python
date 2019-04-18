
class Parent:        # 定义父类
   def a(self):
      print ('调用a类方法')
 
class Child(Parent): # 定义子类
   def a(self):
      print ('调用a1类方法')
 
c = Child()          # 子类实例
c.a()#访问实例中的方法时,实例对象会先在当前类中找相同名字的类的方法,如果没有找到,继续找父类中的类的方法.

super(Child,c).a() 
super()
#用子类对象调用父类已被覆盖的方法
#super函数用于解决多重继承问题.