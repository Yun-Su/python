#!/usr/bin/python3

# 打开文件
fo = open("runoob.txt", "r")
print ("文件名为: ", fo.name)

for index in range(5):
    line = next(fo)
    print ("第 %d 行 - %s" % (index, line))

# 关闭文件
fo.close()


#!/usr/bin/python3

# 打开文件
fo = open("runoob.txt", "r+")
print ("文件名为: ", fo.name)

line = fo.read(10)
print ("读取的字符串: %s" % (line))

# 关闭文件
fo.close()