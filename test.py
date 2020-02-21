import time
import os
cmd = 'ps -fe | grep tail | grep -v "grep"'
a = os.popen(cmd)  # 返回一个对象
txt = a.readlines()
if len(txt) != 0:
    for lin in txt:
        lin_ = lin.split()
        pid = lin_[1]
        cmd = 'kill -9 %d' % (int(pid))
        rc = os.system(cmd)
