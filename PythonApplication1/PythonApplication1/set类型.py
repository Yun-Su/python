
#set和dict类似，也是一组key的集合，但不存储value。
#由于key不能重复，所以，在set中，没有重复的key。
#要创建一个set，需要提供一个list作为输入集合：
s = set([1, 2, 3])
print(s)
#注意，传入的参数[1, 2, 3]是一个list，
#而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，
#显示的顺序也不表示set是有序的。。

#重复元素在set中自动被过滤：
s = set([1, 1, 2, 2, 3, 3])
print(s)
#通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s.add(4)
print(s)
s.add(4)
print(s)
#通过remove(key)方法可以删除元素：
s.remove(4)
pint(s)
#set可以看成数学意义上的无序和无重复元素的集合，
#因此，两个set可以做数学意义上的交集、并集等操作：

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print( s1 | s2)

#set和dict的唯一区别仅在于没有存储对应的value，
#set的原理和dict一样，所以，同样不可以放入可变对象，
#因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。
#试试把list放入set，看看是否会报错。

#上面我们讲了，str是不变对象，而list是可变对象。

#对于可变对象，比如list，对list进行操作，list内部的内容是会变化的，比如：
a = ['c', 'b', 'a']
a.sort()
print(a)
#而对于不可变对象，比如str，对str进行操作呢：

a = 'abc'
print(a.replace('a', 'A'))
print(a)
#虽然字符串有个replace()方法，也确实变出了'Abc'，
#但变量a最后仍是'abc'，应该怎么理解呢

#我们先把代码改成下面这样：
a = 'abc'
b = a.replace('a', 'A')#将'abc'更改为'Abc'并赋值给b
print( b)
print(a)
#要始终牢记的是，a是变量，而'abc'才是字符串对象！
#有些时候，我们经常说，对象a的内容是'abc'，
#其实是指，a本身是一个变量，它指向的对象的内容才是'abc'：