classmates = ('Michael', 'Bob', 'Tracy')
#另一种有序列表叫元组：tuple。tuple和list非常类似，
#但是tuple一旦初始化就不能修改,以上元素不可修改
tt=();#定义一个空的tuple函数
print(tt)
#只有1个元素的tuple定义时必须加一个逗号,来消除歧义
#否则会和()出现歧义,解释为数学计算()而不是tuple()
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
#其中 A B X Y为list元素
print(t)

