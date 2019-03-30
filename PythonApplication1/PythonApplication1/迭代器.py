list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
#print (next(it))   # next()函数输出迭代器的下一个元素,以此类推
#print (next(it))

#使用for循环来输出
for x in it:
    print(x)
