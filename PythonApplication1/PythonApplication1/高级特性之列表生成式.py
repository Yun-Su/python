print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
#写列表生成式时，把要生成的元素x * x放到前面，
#后面跟for循环，就可以把list创建出来，
#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
print( [m + n for m in 'ABC' for n in 'XYZ'])
#使用两层排列进行组合遍历