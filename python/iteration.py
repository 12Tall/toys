from collections import Iterable
# import module Iterable
dic = {"name":"12tall","age":12,"gender":"male"}
# is Iterable
print(isinstance(dic,Iterable))
# normal like other language
for name in dic:
    print(name)
# iterate values
for v in dic.values():
    print(v)
# iterate key and values
for k,v in dic.items():
    print(k,v,)
# iterate key and index like other language
for i,v in enumerate(dic):
    print(i,v)


