class Animal(object):
    def __init__(self, name):
        self.name = name
    def greet(self):
        print ('Hello, I am %s.' % self.name)

class Dog(Animal):
    def at(self):
        super().greet()
        print('WangWang..')


#dog=Dog()
#dog.at()

class A:
     def add(self, x):
         y = x+1
         print(y)

class B(A):
    def add(self, x):
        super().add(x)
b = B()
b.add(2)  # 3