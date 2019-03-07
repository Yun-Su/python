classmate=['第零','第一','第二']
#Python内置的一种数据类型是列表：list。
# list是一种有序的集合，可以随时添加和删除其中的元素。
print(len(classmate))
#使用len()函数统计元素个数
print(classmate[0])
print(classmate[1])
print(classmate[2])
#list列表从0开始计数，不能越界访问list以外的元素。
print('倒数第一个',classmate[-1])#意为取倒数第一个，以此类推
print('倒数第二个',classmate[-2])
print('倒数第三个',classmate[-3])
classmate.append('第三') #追加一个元素到classmate list的末尾
print('打印追加元素第三',classmate[3])#打印成功
classmate.insert(1, '插入元素')#插入一个元素到classmate list指定位置,
                               #其他元素依次延后
print('插入一个元素的列表现在是',classmate) 

#classmate.pop(x) 删除list中第x个元素，如果为空默认删除list中最后一个
print('删除项是',classmate.pop(1))
print('删除一个元素以后的列表现在是',classmate)
classmate[2]='第1000个'
print('对list中元素进行重新赋值',classmate[2])
print('重新赋值以后列表现在是',classmate)
s = ['python', 'java', ['asp', 'php'], 'scheme']
#还可以这样创建list,list中创建list
print(len(s))
