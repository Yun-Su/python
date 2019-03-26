#要限制关键字参数的名字，就可以用命名关键字参数
#只接收city和job作为关键字参数。这种方式定义如下：
def person(name, age, *, city, job):
    print(name, age, city, job)
#命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数,也成为位置参数
print(person('Jack', 24, city='Beijing', job='Engineer'))
#打印出       Jack 24 Beijing Engineer
#print(person('hello',11,city='changsha',addres='rua'))
#因为没有使用限定的关键词参数,在传入addres的时候必定报错.


#如果函数定义中已经有了一个可变参数
#后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def perso(name, age, *args, city, job):
    print(name, age, args, city, job)

#print(perso('Jack', 24, 'Beijing', 'Engineer'))
#此处缺省了*args的值,位置参数传入失败,导致报错
print(perso('Jack',22,city='Beijing',job='Engineer'))
#此处指定了'Beijing'为city的传入参数 'Engineer'为job的参数,可以正常打印
print(perso('Jack',22,'cd',city='Beijing',job='Engineer'))


#使用命名关键字参数时，要特别注意，如果没有可变参数，
#就必须加一个*作为特殊分隔符。
#如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：



