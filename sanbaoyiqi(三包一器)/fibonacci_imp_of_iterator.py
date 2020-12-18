# coding=utf-8
"""
forbonacci数列的迭代器的实现方式
"""
class FibonIterator(object):
    def __init__(self, n):
        """
        n: 数列的前n个数
        current: 保存当前生成数列的第几个数
        num1,num2:表示前前一个数，和前一个数
        """
        self.n, self.current, self.num1, self.num2 = n, 0, 0, 1

    def __next__(self):
        if self.current < self.n:
            num = self.num1
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            self.current += 1
            return num
        else:
            raise StopIteration

    def __iter__(self):
        return self

    
if __name__ == "__main__":
    fi1 =FibonIterator(5)
    for i in fi1:
        print(i, end=' ')
    fi2 =FibonIterator(11)
    print("*"*20)
    for x in fi2:
        print(x, end=' ')