class student(object):
    def __init__(self,name,score):
        self.name=name
        self.__score=score#类的私有属性
        #在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问

    def print_score(self):
        print(self.name,self.__score)

    def get_score(self):
        return self.__score
        #如果一定要获取私有属性.需要使用内部代码来实现访问

    def set_score(self,score):
        self.__score=score
        #如果一定要私有属性实现外部代码访问可以用如上方法
        #还可以函数实现对传入参数检查 加入if 0<=score<=100: else... etc


xm=student('小明',99)
#对类中的实例进行赋值
xm.print_score()
xm.name='小红'
print(xm.name)
xm.__score#此处会报错,私有属性禁止访问


#在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。

#有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

#双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：