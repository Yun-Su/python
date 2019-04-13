vec = [2, 4, 6]
print([3*x for x in vec])
print([[x,x*2]for x in vec])
print( [3*x for x in vec if x > 3])
vec2 = [4, 3, -9]
print([x*y for x in vec for y in vec2])
print([x+y for x in vec for y in vec2])
print([vec[i]*vec2[i] for i in range(len(vec))])
