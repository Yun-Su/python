def printinfo(arg1,*vartuple):
    "打印任何传入的参数"
    print("输出:")
    print(arg1)
    print(vartuple)
#调用已有函数进行传参
printinfo(20,30,40,50)
#不定长参数在传入时,在有*号的参数会以tuple形式导入
#存放所有未命名的参数
printinfo(14)#如果在函数调用时没有指定参数，
#它就是一个空元组。我们也可以不向函数传递未命名的变量。

def function(arg1,**vardict):
    #加了两个星号 ** 的参数会以字典的形式导入
    "打印所有传入的参数"
    print("输出:")
    print(arg1)
    print(vardict)


function(1,a=2,b=3,c=100)
#pyton3的dict采用的是key=value的赋值方式,所以a=xx,b=xx

