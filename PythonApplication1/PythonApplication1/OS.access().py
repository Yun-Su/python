#os.access() 方法使用当前的uid/gid尝试访问路径
#path -- 要用来检测是否有访问权限的路径。

#!/usr/bin/python3
import os, sys
# 假定 /tmp/foo.txt 文件存在，并有读写权限
ret = os.access("/tmp/foo.txt", os.F_OK)
print ("F_OK - 返回值 %s"% ret)
#os.F_OK: 作为access()的mode参数，测试path是否存在。
ret = os.access("/tmp/foo.txt", os.R_OK)
print ("R_OK - 返回值 %s"% ret)
#os.R_OK: 包含在access()的mode参数中 ， 测试path是否可读。
ret = os.access("/tmp/foo.txt", os.W_OK)
print ("W_OK - 返回值 %s"% ret)
#os.W_OK 包含在access()的mode参数中 ， 测试path是否可写。
ret = os.access("/tmp/foo.txt", os.X_OK)
print ("X_OK - 返回值 %s"% ret)
#os.X_OK 包含在access()的mode参数中 ，测试path是否可执行。