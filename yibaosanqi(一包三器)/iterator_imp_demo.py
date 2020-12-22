# coding=utf-8

"""
目标：实现一个自定义的迭代器供可迭代对象使用
"""

class CustomList(object):
    def __init__(self):
        self.items = []
    
    def __iter__(self):
        return CustomIterator(self)

    def add(self, val):
        self.items.append(val)
        

class CustomIterator(object):
    def __init__(self, CustomList):
        self.custom_list = CustomList
        self.current = 0  # 游标，记录当前访问到的位置

    def __next__(self):
        if self.current < len(self.custom_list.items):
            item = self.custom_list.items[self.current]
            self.current += 1
            return item
        else:
            raise StopIteration
    
    def __iter__(self):
        return self


if __name__ == "__main__":
    clist = CustomList()
    clist.add(1)
    clist.add(3)
    clist.add(5)
    clist.add(7)
    for i in clist:
        print(i)

















