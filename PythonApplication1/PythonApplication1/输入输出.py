s="hello,world"
str(s)
repr(s)
print(s)
#str()： 函数返回一个用户易读的表达形式。
#repr()： 产生一个解释器易读的表达形式。
print('12'.zfill(5))
#将数据填充至5位,不够补0    00012

print('{}网址:"{}!"'.format('菜鸟教程','www.so.com'))
#菜鸟教程网址： "www.so.com!"
#括号及其里面的字符 (称作格式化字段) 
#将会被 format() 中的参数替换。
print('{1} 和 {0}'.format('Google', 'So'))
#输出Runoob和Google
print('{name}网址:{site}'.format(name='菜鸟教程', site='www.so.com'))

import math
print('常量 PI 的值近似为:{}。'.format(math.pi))
print('常量 PI 的值近似为:{!r}。'.format(math.pi))
#'!a'(使用 ascii()), '!s'(使用str())和'!r'(使用 repr()) 
#可以用于在格式化某个值之前对其进行转化:
print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))
#精确到小数点后三位
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} ==> {1:10d}'.format(name, number))
#0和1代表顺序,10代表字符占用宽度

import math
print('常量 PI 的值近似为：%5.3f。' % math.pi)
#% 操作符也可以实现字符串格式化。 
#它将左边的参数作为类似 sprintf() 式的格式化字符串, 
#而将右边的代入, 然后返回格式化后的字符串
print('常量 PI 的值近似为：%5.3f。' % math.pi)
#% 操作符也可以实现字符串格式化。
#它将左边的参数作为类似 sprintf()式的格式化字符串, 
#而将右边的代入, 然后返回格式化后的字符串.
