# -*- coding: utf-8 -*-
"""
下面这个是一个有趣的例子，主要使用了deque的rotate方法来实现了一个无限循环
的加载动画
"""
import sys
import time
from collections import deque


q = deque(['a','b','c'])
q.append('w')
q.appendleft('x')
print(q)
# output: deque(['x', 'a', 'b', 'c', 'w'])


# 案例二
fancy_loading = deque('>--------------------')

while True:
    print('\r%s' % ''.join(fancy_loading))
    fancy_loading.rotate(1)  # rotate方法用于旋转，如果参数大于0，表示将队列右端的n个元素移动到左端，否则相反
    sys.stdout.flush()
    time.sleep(0.5)