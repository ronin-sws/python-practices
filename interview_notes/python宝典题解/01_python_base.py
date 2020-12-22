# -*- coding: utf-8 -*-
"""
@File   : 01_python_base.py.py
@Version: v1.0
@Date   : 2020-12-22 
@Desc   : The file is ...
"""

##################################################################
"""
代码中要修改不可变数据会出现什么问题? 抛出什么异常?
"""
# a = (1,2)
# a[0] = 2
# print(a)
# 不会正常运行，抛出TypeError

###################################################################
"""
a=1,b=2,不用中间变量交换 a 和 b 的值？
"""

a =1
b = 2
# a, b = b, a  # 方式一：
# print(a,b)

# a = a + b  # 方式二：
# b = a - b
# a = a -b
# print(a, b)

# a = a ^ b  # 方式三
# print(a)
# b = b ^ a
# print(b)
# a = a ^ b
# print(a, b)

###################################################################
"""
print 调用 Python 中底层的什么方法?
"""
# print默认调用的是sys.stdout.write()方法
# input 默认调用的是sys.stdin.readline()方法

###################################################################
"""
下面这段代码的输出结果将是什么？请解释？
"""
# class Parent(object):
#     x = 1
#
#
# class Child1(Parent):
#     pass
#
#
# class Child2(Parent):
#     pass

# print(Parent.x, Child1.x, Child2.x)  # out: 1, 1, 1
# Child1.x = 2
# print(Parent.x, Child1.x, Child2.x)  # out:1, 2, 1
# Parent.x = 3
# print(Parent.x, Child1.x, Child2.x)  # out: 3, 2, 3

###################################################################
"""
简述你对 input()函数的理解?
"""
# solution:
# 在python3中，无论input的内容是什么，获取到的都是字符串类型，
# 在py2中，有raw_input()和input(),raw_input和Py3的作用一样，而input()输入的是什么类型，获取到的就是什么类型

###################################################################

"""
阅读下面的代码，写出 A0，A1 至 An 的最终值。
"""
A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
A1 = range(10) # range(0,10)
A2 = [i for i in A1 if i in A0]  # []
A3 = [A0[s] for s in A0]  # [1, 2, 3, 4, 5]

print(A3)

###################################################################
"""
range 和 xrange 的区别？
"""

