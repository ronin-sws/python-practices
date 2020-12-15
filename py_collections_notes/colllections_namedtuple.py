
from collections import namedtuple

# 面对对象的方式
class User:
    def __init__(self, name, age, height):
        pass

# 新的方式（在创建简单的对象时，比面对对象的方式更节省空间）
# 案例一：传元组
User = namedtuple("User", ["name", "age","like"])
tmptup = ('wss',25)
user = User(*tmptup, 'readbook')
print(user)
print("*"*15)
User = namedtuple("User", ("name", "age"))
# 元组
tmptuple = ('wss',25)
user = User._make(tmptuple)
print(user)
print("*"*15)
# 列表
tmplist = ['wss',25]
user = User._make(tmplist)
print(user)
print("*"*15)
# 转换为字典
user_dict=user._asdict()
print(user_dict)


# 案例二
websites = [
    ('Sohu', 'http://www.google.com/', u'张朝阳'),
    ('Sina', 'http://www.sina.com.cn/', u'王志东'),
    ('163', 'http://www.163.com/', u'丁磊')
]

Website = namedtuple('Website', ['name', 'url', 'founder'])

for website in websites:
    website = Website._make(website)
    print(website)
