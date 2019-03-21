
def calc(*numbers):
#定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
#在函数内部，参数numbers接收到的是一个tuple，
#因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1,2,3))
print(calc())#传入0个参数
num1=[1,2,3,4]#定义一个list类型
num2=(5,6,7,8)#定义一个tuple类型
print(calc(num1[0],num1[1],num1[2]))#传入几个可变list参数
print(num2[0])#传入一个tuple参数
print(calc(*num1))# *num1代表将整个list传入到calc函数中
print(calc(*num2))# *num2代表将整个tuple传入到calc函数中


