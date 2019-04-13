#!/usr/bin/python3
# 打开文件
fo = open("runoob.txt", "wb")
print("文件名为: ", fo.name)
# 关闭文件
fo.flush()#立刻刷新文件缓冲区执行相应动作到文件中.
fo.close()
