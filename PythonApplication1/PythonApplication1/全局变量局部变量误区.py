a = 10 
def test():
    a = a + 1
    #在test函数中的 a 使用的是未定义的局部变量,无法修改。
    #正确方法应该传入a到test函数中 test(a)即可
    print(a)

test()