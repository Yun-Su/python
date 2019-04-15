
#定义类的时候，若是添加__init__方法，
#那么在创建类的实例的时候，实例会自动调用这个方法，
#一般用来对实例的属性进行初使化。比如：class  testClass: 
#def  __init__(self, name, gender): //定义 __init__方法，这里有三个参数，这个self指的是一会创建类的实例的时候这个被创建的实例本身（例中的testman），你也可以写成其他的东西，比如写成me也是可以的，这样的话下面的self.Name就要写成me.Name。                      self.Name=name//通常会写成self.name=name，这里为了区分前后两个是不同的东东，把前面那个大写了，等号左边的那个Name（或name）是实例的属性，后面那个是方法__init__的参数，两个是不同的）
#self.Gender=gender //通常会写成self.gender=gender                      print('hello')                         //这个print('hello')是为了说明在创建类的实例的时候，__init__方法就立马被调用了。testman = testClass('neo,'male')                               //这里创建了类testClass的一个实例 testman, 类中有__init__这个方法，在创建类的实例的时候，就必须要有和方法__init__匹配的参数了，由于self指的就是创建的实例本身，self是不用传入的，所以这里传入两个参数。这条语句一出来，实例testman的两个属性Name，Gender就被赋值初使化了，其中Name是 neo，Gender 是male
class testClass:
    def __init__(self,name,gender):
        self.Name=name
        self.Gender=gender
        print('hello')

testman=testClass('neo','male')
print(testman.Name,testman.Gender)

class testClass2:
    def __init__(me,name,gender):
        me.name=name
        me.gender=gender
        print('mmp')

testman2=testClass2('jim','male')
print(testman2.name,testman2.gender)