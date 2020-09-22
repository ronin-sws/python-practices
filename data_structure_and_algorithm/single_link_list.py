# -*- coding: utf-8 -*-
"""
@Date   : 2020-09-22
@Desc   : The file is 单链表的实现
"""

class Node(object):
    """节点"""
    def __init__(self, element):
        self.element = element
        self.next = None


class SingleLinkList(object):
    """
        单链表
    """
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """判空操作"""
        return True if self.__head == None else False

    def length(self):
        """长度"""
        cursor, count = self.__head, 0  # cursor 游标指针， count记录数量
        while cursor != None:
            count += 1
            cursor = cursor.next
        return count

    def travelse(self):
        """遍历链表"""
        cursor = self.__head
        # print("cursor为:%s" % cursor.element)
        while cursor != None:
            # print(cursor.element)
            print(cursor.element, end=" ")
            cursor = cursor.next

    def add(self, item):
        """
        链表头部添加元素
        时间复杂度为:O(1)
        """
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """
        链表尾部添加元素
        时间复杂度为:O(n)
        """
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cursor = self.__head
            while cursor.next != None: # 只要cursor.next 为空，表示游标已指向最后一个元素的位置，退出循环，将新的节点挂载上来
                cursor = cursor.next
            cursor.next = node

    def insert(self, position, item):
        """
        链表指定位置添加元素
        时间复杂度为:O(n)
         """
        # position 默认从0开始
        if position <= 0:
            self.add(item)
        elif position > (self.length() - 1):
            self.append(item)
        else:
            pre_cursor, count = self.__head, 0
            while count < (position - 1):
                count += 1
                pre_cursor = pre_cursor.next
            # 当循环退出以后，pre_cursor 指向position - 1 的位置
            node = Node(item)
            node.next = pre_cursor.next
            pre_cursor.next = node

    def remove(self, item):
        """
        删除元素
       （需要考虑特殊情况，首末位是否符合条件）
        """
        pre_cursor, cursor = None, self.__head
        while cursor != None:
            if cursor.element == item:
                if cursor == self.__head: # 判断此节点是否为头节点，
                    self.__head = cursor.next
                else:
                    pre_cursor.next = cursor.next
                break  # 避免出现死循环
            else:
                pre_cursor = cursor
                cursor = cursor.next

    def search(self, item):
        """
        查找元素是否存在
        时间复杂度为:O(n)
        """
        cursor = self.__head
        while cursor != None:
            if cursor.element == item:
                return True
            else:
                cursor = cursor.next
        return False


if __name__ == '__main__':
    sll = SingleLinkList()
    print(sll.is_empty())
    print(sll.length())
    sll.append(1)
    print(sll.is_empty())
    print(sll.length())
    print("**********")
    sll.append(2)
    sll.append(5)
    sll.append(4)
    sll.append(9)
    sll.add(6)
    sll.insert(3, -1)
    sll.insert(4, 7)
    print(sll.search(4))
    print(sll.search(50))
    sll.remove(1)
    sll.remove(5)
    sll.travelse()

