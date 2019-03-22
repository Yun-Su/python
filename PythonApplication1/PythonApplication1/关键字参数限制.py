#要限制关键字参数的名字，就可以用命名关键字参数
#只接收city和job作为关键字参数。这种方式定义如下：
def person(name, age, *, city, job):
    print(name, age, city, job)
#命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
print(person())