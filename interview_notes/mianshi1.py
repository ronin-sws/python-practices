# [{1:'a'}, {2:'b'}]


tmpdict = [{1:"a"},{2:"b"}]
#[{'key':key, 'value':value} for key, value in tmpdict.items()]
#for key, value in tmpdict.items():
#   print(key,value)

tmpdict1 = dict()
for i in tmpdict:
    for key, value in i.items():
        tmpdict1[key] = value
print(tmpdict1)