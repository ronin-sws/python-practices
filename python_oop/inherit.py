# -*- coding: utf-8 -*-
"""
@Date   : 2020-09-24
@Desc   : The file is 类的继承，调用父类的属性和方法，super 的使用
"""

"""直接调用父类属性"""
class Base1(object):
    def __init__(self):
        self.a = 'aa'

    def do(self):
        print('调用父类的方法')

class BaseSon1(Base1):
    pass

# base_son = BaseSon1()
# base_son.do()
# print(base_son.a)

# 输出内容：
    # 调用父类的方法
    # aa


"""重写父类属性方法"""
"""结论：如果子类没有重写父类的方法，当调用该方法的时候，会调用父类的方法，当子类重写了父类的方法，默认是调用自身的方法"""
class Base2(object):
    def __init__(self):
        self.a = 'aa'

    def do(self):
        print('调用父类的方法')

class BaseSon2(Base2):
    def __init__(self):
        self.a = 'bb'

    def do(self):
        print('调用自己的方法')

# base_son = BaseSon2()
# base_son.do()
# print(base_son.a)

# 输出内容：
    # 调用自己的方法
    # bb

"""子类重写了父类的方法，但是还是想调用父类的方法，使用super()"""
class Base3(object):
    def do(self):
        print('调用父类的方法')

class BaseSon3(Base3):
    def do(self):
        super().do()

# base_son3 = BaseSon3()
# base_son3.do()
# 输出内容：
    # 调用父类的方法

"""强制调用父类的私有属性和方法"""
class Base4(object):
    def __do(self):
        print('调用父类的方法')

class BaseSon4(Base4):
    def do(self):
        super()._Base4__do()

# a = BaseSon4()
# a.do()
# 输出内容：
    # 调用父类的方法

"""调用父类的__init__方法"""
class SchoolMember:
    '''代表任何学校里的成员。'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        '''告诉我有关我的细节。'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")


class Teacher(SchoolMember):
    '''代表一位老师。'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))


class Student(SchoolMember):
    '''代表一位学生。'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

# 打印一行空白行
print()

members = [t, s]
for member in members:
    # 对全体师生工作
    member.tell()




if __name__ == '__main__':

    pass


