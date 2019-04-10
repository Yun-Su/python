f=open("C:/Users/J/Desktop/新建文本文档.txt","w")
s=f.write("面具之下是一种思想\n而思想是不害怕子弹的\n")
#f.write()将字符写入到对应的文件中
#并返回s写入的字符个数
f.close()
print(s)

f=open("C:/Users/J/Desktop/新建文本文档.txt","r")
print(f.read())#读取了上次写入的文件并答应出来
f.close()

f=open("C:/Users/J/Desktop/新建文本文档 (2).txt","r")
str=f.readline()#读取到换行符以后就马上停止读取
print(str)
f.close()

f=open("C:/Users/J/Desktop/新建文本文档 (2).txt","r")
str=f.readlines()#读取文件所有内容,包括换行符
print(str)
f.close()


#!/usr/bin/python3
#写入字符串到文本中
f = open("C:/Users/J/Desktop/社会主义核心价值观.txt", "w")
value = ('www.Pornhub.com',123456789)#一个普通的tuple函数
s = str(value)
#Python3 str() 函数是内置函数，可以直接使用
#作用是将其他类型转化为字符串形式
f.write(s)
f.close()





