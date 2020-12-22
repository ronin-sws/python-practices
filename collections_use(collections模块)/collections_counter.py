from collections import Counter

str1 = "sdfwetsfswfwef"
c1 = Counter(str1)
print(c1)
# print(c1.most_common(3))
# print(isinstance(c1, dict))
str2 = 'dfewafsfes'
c2 = Counter(str2)
print(c2)
c = c1 + c2
print(c)
c = c1 - c2
print(c)
c = c1 & c2
print(c)
c = c1 | c2
print(c)