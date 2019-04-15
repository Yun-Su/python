#https://www.zhihu.com/question/46973549/answer/103805810
class testClass:
    def __init__(self,name,gender):
        self.Name=name
        self.Gender=gender
        print('hello')#此处print说明__init__函数在进行初始化的时候立马被调用
testman=testClass('neo','male')
print(testman.Name,testman.Gender)

class testClass2:
    def __init__(me,name,gender):
        me.name=name
        me.gender=gender
        print('mmp')

testman2=testClass2('jim','male')
print(testman2.name,testman2.gender)