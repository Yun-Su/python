classmate=['第零','第一','第二']
#Python内置的一种数据类型是列表：list。
# list是一种有序的集合，可以随时添加和删除其中的元素。
print(len(classmate))
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
print('第0个元素',classmate[0]) 
print('第一个',classmate[1])
print('第二个',classmate[2])
print('第三个',classmate[3])
print('第四个',classmate[4])