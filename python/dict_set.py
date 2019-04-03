# list []
# tuple () couldnt be modified, like const array
# dict ❴❵
# set need a list as param
# dict and set save keys by hashcode
# so the key must be unchangeable
# hope i am right
dic = {"name":"12tall","age":12}
print(dic["name"])
print(dic.get("age"))
# if value doesnt exist will return None
print(dic.get("gender"))
# or we can choose a value as result but will not modify the dict
print(dic.get("gender","secret"))
# pop() will pop a element like list or stack
dic.pop("age")
print(dic)

#####set#####
# set has no value
# set need a list as param

s = set([1,2,3,4,3])
print(s)
s.add("key")
print(s)
s.remove(1)
print(s)

