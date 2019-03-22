def person(name, age, **kw):#name age为必选参数,若未自定义初始化,赋值时必须传入
#**kw可变参数允许你传入0个或任意个参数
#这些可变参数在函数调用时自动组装为一个tuple。
#而关键字参数允许你传入0个或任意个含参数名的参数
#这些关键字参数在函数内部自动组装为一个dict
    print('name:', name, 'age:', age, 'other:', kw)


print(person('Michael',30))#未传入时打印other:{}
print(person('Adam', 45, a='123',b='456'))
#打印出Adam age: 45 other: {'a': '123', 'b': '456'}
extra = {'city': 'Beijing', 'job': 'Engineer'}#声明一个dict
print(person('Jack', 24, city=extra['city'], job=extra['job']))#一种传入方法
print(person('Jack', 24, **extra))#另外一种传入方法
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数
#kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，
#对kw的改动不会影响到函数外的extra