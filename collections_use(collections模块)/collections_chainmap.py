from collections import ChainMap
a = {"x":1, "z":3}
b = {"y":2, "z":4}
c = ChainMap(a,b)
print(c)
print("x: {}, y: {}, z: {}".format(c["x"], c["y"], c["z"]))
print("*"*20)
temp1 = c.maps
print(temp1, type(temp1))
print("*"*20)
temp2 = c.parents
print(temp2, type(temp2))








