

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
    Animal.run()
    #调用父类的方法的时候,类的方法的名称一定要一一对应.
run_twice(Animal())

print('以上为Animal',"以下为dog")

def run_twice(Dog):
    Dog.run()
    Dog.run_dog()
    #调用父类方法和调用子类方法会有不同的结果.
run_twice(Dog())




