
na = ['Michael', 'Bob', 'Tracy']#y为变量,无需声明
for y in na: #注意此处标点符号:
    print(y)
#循环的一种方式
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:#X为变量无需声明
    sum = sum + x
print(sum)
#循环的二种方式
range(5)#python提供一个range()函数，
        #可以生成一个整数序列
        #比如range(5)生成的序列是从0开始小于5的整数
for z in range(5):
    print(z)

#也可以使range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'):
for w in range(0, 10, 3): #此处增量为3
    print('增量为3时的输出',w)

#循环的另外一种方式
sum = 0
n =10
while n > 0:
    sum = sum + n
    n = n-1
print(sum)