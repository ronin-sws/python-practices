from collections import defaultdict

d = defaultdict(int)  # 默认值0
str = 'wfdsfewfeswfs'
for s in str:
    d[s] += 1
print(d)
print(d['w'])
print(d['f'])
print(d['u'])  

d2 = defaultdict(list)  # 默认值[]
print(d2['z'])
d3 = defaultdict(lambda : 5) # 自定义默认值
print(d3['z'])

print("*"*20)

def generate_default():
    return {
        "a":1, 
        "b":3
        }
tempd = defaultdict(generate_default)
print(tempd['z'])

members = [
    # Age, name
    ['male', 'John'],
    ['male', 'Jack'],
    ['female', 'Lily'],
    ['male', 'Pony'],
    ['female', 'Lucy'],
]

result = defaultdict(list)
for sex, name in members:
    result[sex].append(name)

print(result) 
