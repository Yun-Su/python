

class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    def run_dog(self):
        print('Dog is running...')
class Cat(Animal):
    def run_cat(self):
        print('Dog is running...')

dog = Dog()
cat = Cat()
dog.run()
dog.run_dog()
cat.run()
cat.run_cat()
print('以上为类',"以下为函数")

def run_twice(Animal):
    Animal.run()
    #调用父类的方法的时候,类的方法的名称一定要一一对应.
run_twice(Animal())

print('以上为Animal类',"以下为dog类")

def run_twice(Dog):#继承自Dog()类
    Dog.run()#调用Animal类中的方法
    Dog.run_dog()#调用了Dog类中的方法
    #调用父类方法和调用子类方法会有不同的结果.
run_twice(Dog())
#Dog()存储了这个类当前的内存地址.作为参数传入到run_twice()中
#对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：