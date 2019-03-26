
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
    #dict的存储不是按照list的方式顺序排列，
    #迭代出的结果顺序很可能不一样。
 
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
    #for循环里，同时引用了两个变量，在Python里是很常见
