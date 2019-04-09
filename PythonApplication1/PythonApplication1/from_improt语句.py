from fibo1 import fib3,fib4
#从fibo1某块中导入指定的fib3 fib4两个函数到当前文件以便于引用
from fibo1 import *
#如果嫌麻烦,可以用*号代替模块中所有函数
#除了下划线类似_函数的函数不会被导入进来
fib3(500)
print(fib4(600))
