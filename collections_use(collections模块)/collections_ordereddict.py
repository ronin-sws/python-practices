from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d) # dict的Key是无序的
{'a': 1, 'c': 3, 'b': 2}
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od) # OrderedDict的Key是有序的


od2 = OrderedDict()
od2['z'] = 1
od2['y'] = 2
od2['x'] = 3
print(od2.keys())
od2.move_to_end('z')  # 将指定的key移动到最后面
print(od2)
