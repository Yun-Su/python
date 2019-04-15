a=[1,2,3]
a="Runoob"
#[1,2,3] 是 List 类型，"Runoob" 是 String 类型，
#而变量 a 是没有类型，她仅仅是一个对象的引用，
#可以是指向 List 类型对象，也可以是指向 String 类型对象。
def changeme( mylist ):
    "修改传入的列表"
    mylist.append([1,2,3,4])
    print ("函数内取值: ", mylist)
    return mylist
# 调用changeme函数

mylist = [10,20,30]
changeme( mylist )
print ("函数外取值: ", mylist)