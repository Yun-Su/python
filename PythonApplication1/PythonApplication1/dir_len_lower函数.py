#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法
print(dir('ABC'))

print(len('ABC'))
print('ABC'.__len__())#和len()二者作用等价


print('ABC'.lower())
#打印出'abc'

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

print(hasattr(obj, 'x')) # 有属性'x'吗？
print(obj.x)#打印出属性x的值
print(hasattr(obj, 'y')) # 有属性'y'吗？
#setattr()会对已存在的属性进行赋值,如果属性不存在则创建属性如下所示
print(setattr(obj, 'y', 100)) # 设置一个属性'y'
print(hasattr(obj, 'y')) # 有属性'y'吗？
print(getattr(obj, 'y')) # 获取属性'y'
print(obj.y) # 获取属性'y'
print(getattr(obj, 'z', 404)) # 获取属性'z'，如果不存在，返回默认值404
