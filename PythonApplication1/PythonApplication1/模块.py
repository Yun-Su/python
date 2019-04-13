#!/usr/bin/python3
import sys
#import sys 引入 python 标准库中的 sys.py 模块
#这是引入某一模块的方法。
print('命令行参数如下')
for i in sys.argv:
    #sys.argv 是一个包含命令行参数的列表。
    print(i)
print('Python路径为:',sys.path)