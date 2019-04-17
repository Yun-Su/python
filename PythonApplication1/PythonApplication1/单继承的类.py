class people:
    #定义基本属性
    name = ''
    age = 0
    __weight = 0#定义私有属性,私有属性在类外部无法直接进行访问
    def __init__(self,n,a,w): #定义构造方法
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
#单继承示例
class student(people):
    grade = ''
    def __init__(self,n,a,w,g): 
       
        people.__init__(self,n,a,w) #调用父类的构函
        self.grade = g
   
    def speak(self): #覆写父类的方法
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
 
s = student('ken',10,60,3)
s.speak()