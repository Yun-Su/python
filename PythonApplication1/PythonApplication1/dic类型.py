
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
#dict类型,给定'Michael'，dict在内部就可以直接计算出Michael对应的存放成绩的“页码”，
#也就是95这个数字存放的内存地址，直接取出来，所以速度非常快。
d['Bob']=20
print(d['Bob'])
#一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：
#避免key不存在的错误，有两种办法，一是通过in判断key是否存在
print('Thomas' in d)#返回值为Flase/True
#或者使用get
print(d.get('Thomas'))#默认返回None
print(d.get('Thomas', -10086))#可以自行指定返回值

d.pop('Bob')#删除一个'Bob'的key ,value也会被删除
print(d)
