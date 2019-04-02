lst = ["hello","tall"]
# print all elements
print(lst)
lst.insert(1,12)
# insert element at 1
print(lst)
# list can contain difference type elements
# insert element before current
# at least 2 params need
lst.insert(len(lst)-1,"hmm")
print(lst)
# pop element like stack
# but no push insert
temp = lst.pop()
print(temp)
lst.pop(2)
lst.insert(len(lst),"tall")
print(lst)
# so have a trick
# insert is a smart method
lst.insert(10,["!","?"])
print(lst)
# append element
lst.append(12)
print(lst)

#####tuple#####
# tuple is readonly list
# tuple can contains list which can be modified

# make difference with (1) which means number 1
tpl = (1,)
# even print the same format
print(tpl)
