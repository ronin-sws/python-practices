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
"""
在 except 中 return 后还会不会执行 finally 中的代码？怎么抛出自定义异常？
"""
# 会继续处理finally中的代码； 可以使用raise 抛出自定义异常


###################################################################
"""
介绍一下 except 的作用和用法？

except:用于捕获所有的异常
except <异常名>：捕获指定异常
except <异常名1， 异常名2> ：<数据>
"""

###################################################################
"""
常用的 Python 标准库都有哪些？

os 操作系统；random 随机数；queue队列；time 时间；pymysql 连接数据库；threading线程；multiprocessing 进程
requests, scrapy, xadmin , celery, re, numpy,pandas, collections
"""

###################################################################
"""
赋值、浅拷贝和深拷贝的区别？

solution:
赋值：赋值操作就是复制了对象的引用，可以用is或者id来判断两者的地址是否相同
浅拷贝：会创建新的对象，其内容非原对象本身的引用，而是在源对象内第一层的引用，浅拷贝有三种形式，切片操作，工厂函数，copy.copy()
    b = a[:] ; b = [i for i in a] ; b = list(a) ;  b = copy.copy(a)  
深拷贝：拷贝了对象的所有元素，包括多层嵌套的元素，只有一种拷贝形式那就是：copy.deepcopy();深拷贝出来的对象会是一个全新的对象，和原来对象没有任何关系了，

"""

###################################################################
"""
拷贝的注意点？

solution:
对于非容器类型（即不可变类型），如数字，字符以及其他'原子'类型，没有拷贝一说，产生的对象都是源对象的引用；
如果元组变量值包含原子类型对象，即时采用了深拷贝，也只能得到浅拷贝
"""

###################################################################
"""
__init__ 和__new__的区别？

solution:
init是在对象创建以后，对对象进行初始化，new是在创建对象之前创建一个对象，并将该对象返回给init
"""

###################################################################
"""
Python 里面如何生成随机数？

solution:
import random
print(random.random())  # 生成一个 0-1 之间的随机浮点数；
print(random.uniform(1,2))  #：生成[1,2]之间的浮点数；
print(random.randrange(1,5,2))  #  在指定的集合[1,5)中，以 2 为基数随机取一个数；
print(random.randint(1,6))  # 生成[1,6]之间的整数；
"""

###################################################################
"""
输入某年某月某日，判断这一天是这一年的第几天？
"""
# import datetime
# def get_date():
#     year, month, day = input('请输入年份：'), input('请输入月份：'), input('请输入日期：')
#     date1 = datetime.date(year=int(year), month=int(month), day=int(day))
#     date2 = datetime.date(year=int(year), month=1, day=1)
#     return (date1 - date2).days + 1
# print(get_date())


###################################################################
"""
打乱一个排好序的 list 对象 alist？
"""
# import random
# alist = [1,2, 3,5, 8]
# random.shuffle(alist)
# print(alist)

###################################################################
"""
说明一下 os.path 和 sys.path 分别代表什么？

solution
os.path：主要用于系统路径文件的操作
sys.path:主要用于python解释器的系统环境变量参数的操作，动态的改变python解释器搜索路径
"""

###################################################################
"""
Python 中的 os 模块常见方法？

solution:
import os
os.remove():删除文件
os.rename():重命名文件
os.walk():生成目录树下的所有文件名
os.chdir():改变目录
os.mkdir/makedirs: 创建目录/多层目录
os.listdir():列出指定目录的文件
os.getcwd():获取当前工作目录
os.path.basename()去掉目录路径，返回文件名
os.path.dirname()去掉文件名，返回目录路径
os.path.join()将分离的各部分组合成一个路径名
os.path.split():返回（dirname(), basename()）的元组
os.path.splitext():返回（filename, extension）的元组
os.path.getsize():返回文件的大小
os.path.exists():是否 存在
os.path.isabs(): 是否为绝对路径
os.path.isdir():是否为目录
os.path.isfile(): 是否为文件
"""

###################################################################
"""
Python 的 sys 模块常用方法？

solution:
import sys
sys.argv(): 命令行参数列表， 第一个元素时程序本身的路径
sys.modules.keys(): 返回所有已经导入的模块列表
sys.exc_info(): 获取当前正在处理的异常类，exc_type,exc_value, exc_tracback当前处理的异常详细信息
sys.modules: 返回系统导入的模块字段，key是模块名，value是模块
sys.path: 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.stdout:标注输出
sys.stdin: 标注输入
sys.stderr: 错误输出
"""

###################################################################
"""
unittest 是什么？

solution:
python的单元测试框架，它拥有支持共享搭建，自动测试，在测试中暂停代码，将不同测试迭代成一组等功能 """


###################################################################
"""
模块和包是什么？

solution:
模块是搭建程序的一种方式，每一个py文件都是一个模块，并可以引用其他的模块，
一个包中包含了很多的py文件夹，
"""

###################################################################
"""
Python 是强语言类型还是弱语言类型？

solution:
强类型的动态脚本语言，
强类型：不允许不同类型数据相加
动态：不用申明变量的类型，且确定一个变量的类型是在第一次给它赋值时，
脚本语言：一般称为解释性语言，运行代码只需要一个解释器，不需要编译
"""

###################################################################
"""
谈一下什么是解释性语言，什么是编译性语言?

solution:
解释性语言是在运行程序的时候才会进行翻译，
编译性语言是在程序执行之前，需要一个专门的编译过程，把程序编译成可执行文件
"""

###################################################################
"""
Python 中有日志吗?怎么使用?

solution:
有 logging模块， logging.basicConfig()，配置相应的参数
"""

###################################################################
"""
Python 是如何进行类型转换的？

solution:
python有很多的内置函数，可以使用内置函数进行类型转换
"""

###################################################################
"""
关于 Python 程序的运行方面，有什么手段能提升性能？

solution:
1. 使用多线程，充分利用机器的多核性能
2. 对于性能影响较大的部分代码，可以使用c或者C++编写
3. 对于IO阻塞造成性能影响的，可以使用IO多路复用来解决
4. 尽量使用python内置的函数
5. 尽量多使用局部变量
"""

###################################################################
"""
Python 中的作用域？

solution:
python中，一个变量的作用域，总是由在代码中被赋值的地方所决定，当遇到一个变量，会按照这个下面的顺序进行搜索
Local(本地作用域） ---> Enclosing locals(当前作用域被嵌入的本地作用域) ---> 全局/模块作用域 ---> 内置作用域（build-in）
"""

###################################################################
"""
什么是 Python？

solution:
python是一种强类型动态脚本语言，常被称为胶水语言，python中一切皆对象，有继承，封装，多态等特性，
"""

###################################################################
"""
什么是 Python 自省？

solution:
自省是python的一种特性，简单的说，在没有指明类型的情况下，程序在运行时能够自动获取对象的类型，
其中主要是通过，dir(),type(),hasattr(),isinstance()这些内置函数来实现的
"""

###################################################################
"""
什么是 Python 的命名空间？

solution:
在python中，所有的名字都存在一个空间中，他们在该空间存在和被操作，这就是命名空间；
当需要使用时，会从该空间中寻找相应的对象；
"""

###################################################################
"""
Linux 的基本命令（怎么区分一个文件还是文件夹）

solution:
ls -F 在显示名称的时候会在文件夹后添加'/', 在文件后面加'*'
"""

###################################################################
"""
日志以什么格式，存放在哪里？

solution:
.log,   通常存放在/var/log/
"""

###################################################################
"""
Linux 查看某个服务的端口?

solution:
netstat -anp | grep service_name
"""

###################################################################
"""
ubuntu 系统如何设置开机自启动一个程序?

solution:
直接修改/etc/rc0.d ~ /etc/rc6.d 和/etc/rcS.d 文件夹的内容，添加需启动的程序，S 开头的表示 启动，K 开头的表示不启动。
"""

###################################################################
"""
在 linux 中 find 和 grep 的区别

solution:

"""











###################################################################
"""
Linux 重定向命令有哪些？有什么区别？
"""













###################################################################
"""
软连接和硬链接的区别？
"""




###################################################################
"""
10 个常用的 Linux 命令？
"""



###################################################################
"""
Linux 关机命令有哪些？
"""




###################################################################
"""
git 合并文件有冲突，如何处理?
"""






###################################################################
"""
现有字典 d={‘a’:24，‘g’:52，‘i’:12，‘k’:33}请按字典中的 value 值进行排序？
"""








###################################################################
"""
说一下字典和 json 的区别？
"""







###################################################################
"""
什么是可变、不可变类型？
"""






###################################################################
"""
存入字典里的数据有没有先后排序？
"""







###################################################################
"""
字典推导式？
"""








###################################################################
"""
现有字典 d={‘a’:24，’g’:52，’l’:12，’k’:33}请按字 典中的 value 值进行排序？
"""








###################################################################
"""
如何理解 Python 中字符串中的\字符？
"""








###################################################################
"""
请反转字符串“aStr”?(
"""









###################################################################
"""
将字符串"k:1|k1:2|k2:3|k3:4"，处理成 Python 字典：{k:1， k1:2， ... } # 字 典里的 K 作为字符串处理
"""








###################################################################
"""
请按 alist 中元素的 age 由大到小排序
"""







###################################################################
"""

"""







###################################################################
"""

"""






###################################################################
"""

"""







###################################################################
"""

"""







###################################################################
"""

"""







###################################################################
"""

"""








###################################################################
"""

"""








###################################################################
"""

"""








###################################################################
"""

"""








###################################################################
"""

"""









###################################################################
"""

"""







###################################################################
"""

"""





###################################################################
"""

"""





###################################################################
"""

"""




###################################################################
"""

"""







