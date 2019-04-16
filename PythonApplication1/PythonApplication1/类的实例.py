class Student(object):
    #Student是一个类
    #object表示该类是从哪个类继承下来的
    #通常，如果没有合适的继承类，就使用object类
    #object类是所有类最终都会继承的类。
    def __init__(self, name, score):#此为类的方法
        #类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性带上
        #有了__init__方法，在创建实例的时候，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：
        self.name = name
        self.score = score
    def print_score(self):#为了访问快捷我们对数据进行封装
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score>=90:
            return 'A'
        if self.score>=60:
            return 'B'
        else:
            return 'C'
AA=Student('小A',66)#bart指向了一个类的实例,它包含了这个实例的内存地址,由于__init__存在,需要传入指定格式参数,否则报错
BB=Student('小B',59)
CC=Student('小C',89)
print(AA.name,AA.score)#打印出了当前类的属性
AA.print_score()#输出了当前类的方法
print(AA.get_grade(),BB.get_grade(),CC.get_grade())