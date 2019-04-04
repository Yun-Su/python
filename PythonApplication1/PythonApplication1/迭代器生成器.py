import sys         # 引入 sys 模块
 
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
 
while True:
    try:
        print (next(it))
    except StopIteration:
        #sys.exit()sys.exit()是退出python解释器回到上级shell，
        #而IDEL最高级别就是python解释器，所以没法退到上级。