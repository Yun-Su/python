#list在元素较多时会占用较大内存,如上百万个list元素
#为解决此问题使用生成器
g = (x * x for x in range(10))#一个生成器
L = [x * x for x in range(10)]#一个list
print('list',L)
print('generator',g)
#创建L和g的区别仅在于最外层的[]和()
#L是一个list，而g是一个generator。
#要一个一个打印出来，可以通过next()函数获得generator的下一个返回值
#print(next(g))
#print(next(g))
#print(next(g))#每次打印一个以后会打印下一个,依此类推..

for n in g:
    print(n)
    #用循环的方式打印出来
