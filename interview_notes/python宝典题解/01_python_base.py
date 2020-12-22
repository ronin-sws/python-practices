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
# A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# A1 = range(10) # range(0,10)
# A2 = [i for i in A1 if i in A0]  # []
# A3 = [A0[s] for s in A0]  # [1, 2, 3, 4, 5]
# print(A3)

###################################################################
"""
range 和 xrange 的区别？
"""
#range返回的是一个列表，xrange返回的是一个生成器，，当列表数据较大时，xranged的性能要比range好

###################################################################
"""
说出一下代码运行的结果是什么？
"""
# l = []
# for i in range(10):
#     l.append({'num':i})
# # print(l)  #　[{'num': 0}, {'num': 1}, {'num': 2}, {'num': 3}, {'num': 4}, {'num': 5}, {'num': 6}, {'num': 7}, {'num': 8}, {'num': 9}]
#
# ll = []
# a = {'num':0}
# for i in range(10):
#     a['num'] = i
#     ll.append(a)
# print(ll)  # [{'num': 9}, {'num': 9}, {'num': 9}, {'num': 9}, {'num': 9}, {'num': 9}, {'num': 9}, {'num': 9}, {'num': 9}, {'num': 9}]
# 字典是可变对象，在for 循环中执行列表的append操作，是把a的引用传给列表，当执行a["num"]赋值操作时，a的引用发生变化，相当于浅拷贝

###################################################################
"""
以下程序输出什么
"""
# for i in range(5, 0, -1):
#     print(i)  #　５，４，３，２，１


###################################################################
"""
4G 内存怎么读取一个 5G 的数据
"""
# 方法一：可以使用生成器的方式，每次读取相对少的数据，分包读取，处理完毕后再读取后面的包
# 方法二：通过linux中的split切割成小文件，然后在对数据进行处理，这种做法效率也比较高，

###################################################################
"""
现在考虑有一个 jsonline 格式的文件 file.txt 大小约为 10K，之前处理文件的 代码如下所示：
def get_line():
    l = []
    with open('file.txt', 'rb') as f:
        for eachline in f:
            l.append(eachline)
    return l

if __name__ == '__main__':
    for e in get_line():
        process(e)  #　处理每一行数据

现在要处理一个大小为 10G 的文件，但是内存只有 4G，如果在只修改 get_lines 函数而其他代 码保持不变的情况下，应该如何实现？需要考虑的问题都有哪些？
"""
# def get_line():
#     l = []
#     with open('file.txt', 'rb') as f:
#         data = f.readlines(50000)
#     l.append(data)
#     yield l


###################################################################
"""
read、readline 和 readlines 的区别?
"""
# read读取整个文件
# readline 读取下一行，使用生成器方法
# readlines 读取整个文件到迭代器以供遍历操作

###################################################################
"""
补充下列缺失的代码
"""
# def print_directory_contents(sPath):
#     """
#     这个函数接收文件夹的名称作为输入参数，返回该文件夹中文件的路径，以及其包含文件夹文件的路径
#     """
#     import os
#     for s_child in os.listdir(sPath):
#         s_child_path = os.path.join(sPath, s_child)
#         if os.path.isdir(s_child_path):
#             print_directory_contents(s_child_path)
#         else:
#             print(s_child_path)


###################################################################
