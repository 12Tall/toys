# official document
# https://docs.python.org/3/library/functions.html

# import package
import math

print(hex(128))
print(hex(-1))
def nop():
    # pass means do nothing
    pass

def add(i,j):
    if not isinstance(i,(int,float)):
        # throw exception
        raise TypeError("invalid param")
    if not isinstance(j,(int)):
        raise TypeError("int needed")
    return i+j


print(add(3,40))

def MultiRtn():
    # return not 0,-1 exactly
    return math.sin(math.pi),math.cos(math.pi)

rtn = MultiRtn()
# function can return more than one result in a tuple, seems like more than one result
print(rtn)


