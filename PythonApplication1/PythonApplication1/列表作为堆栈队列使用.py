#列表方法使得列表可以很方便的作为一个堆栈来使用，
#堆栈作为特定的数据结构，最先进入的元素最后一个被释放（后进先出）。
#用 append() 方法可以把一个元素添加到堆栈顶。
#用不指定索引的 pop() 方法可以把一个元素从堆栈顶释放出来。
stack = [3, 4, 5]
stack.append(6)
stack.append(7)

stack.pop()

stack.pop()

stack.pop()

#也可以把列表当做队列用，
#只是在队列里第一加入的元素，第一个取出来
#但是拿列表用作这样的目的效率不高。
#在列表的最后添加或者弹出元素速度快，
#然而在列表里插入或者从头部弹出速度却不快
#（因为所有其他的元素都得一个一个地移动）。
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
#'Eric'
queue.popleft()                 # The second to arrive now leaves
#'John'
print(queue)                    # Remaining queue in order of arrival
#deque(['Michael', 'Terry', 'Graham'])