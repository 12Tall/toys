# slice is a kind of operator
# lst[start:end] means start<= index <end
# it also can be lst[:end] if start is 0
lst = [1,2,3,4,5]
print(lst[0:3])
# more funny thing is, nagtive numbers can index element from behind
print(lst[-2:])
# get element every two elems
print(lst[::2])
# copy a lst
print(lst[:])

# string is a kind of list like tuple
# while tuole is const
# so can use slice operator to get letters from s string
