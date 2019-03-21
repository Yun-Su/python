
def enroll(name, gender, age=6, city='Beijing'):#设置所有默认值为age==6,city==Beijing
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
print(enroll('Sarah', 'F'))
print(enroll('Bob', 'M', 7))
print(enroll('Adam', 'M', city='Tianjin'))
#对指定参数进行重新赋值