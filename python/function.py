# official document
# https://docs.python.org/3/library/functions.html

# import package
import math

print(hex(128))
print(hex(-1))
def nop():
    # pass means do nothing
    pass

# param j's default value is 1
def add(i,j=1):
    if not isinstance(i,(int,float)):
        # throw exception
        raise TypeError("invalid param")
    if not isinstance(j,(int)):
        raise TypeError("int needed")
    return i+j

# use default param
print(add(3))

def MultiRtn():
    # return not 0,-1 exactly
    return math.sin(math.pi),math.cos(math.pi)

rtn = MultiRtn()
# function can return more than one result in a tuple, seems like more than one result
print(rtn)

# default params like a const pointer in c/c++
# basic var is copy,while object is reference such as lst,dic,set etc.
# the following fn() will append "12tall" to lst every called
def fn(i=1,lst=[]):
    i=i+1
    lst.append("12tall")
    print(i)
    print(lst)
    return
fn()
fn()

# params[]
# var parasm more like a tuple 
# likes return multiresult
def fn2(*p):
    print(p)
    return
fn2(1,2,3)

# keyword function
def fn3(n,**kv):
    print(n)
    print(kv)
    return
# no same param name!!!
fn3(1,m=2)

# named keyword function
# param after * is named
# this type of function accept declared keyword param only
def fn4(n,*,a):
    print(n)
    print(a)
    return
# must use a=*** when called
fn4(1,a=2)

# it's confusing
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431752945034eb82ac80a3e64b9bb4929b16eeed1eb9000

