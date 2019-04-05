def div(a,b):
    assert b != 0,"b cannot be zero"
    return a / b

print(div(1,2))
# assert will throw an exception while var doesnt correct
print(div(2,0))
print(div(0,2))

# logging is a more useful method when debug
# import logging first
# 
# pdb and other ides
