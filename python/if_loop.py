lst = [1,2,3,4,5,6,7,8,9,0]
for e in lst:
    # '//' like '/' in other language
    # '/' in python returns float as result
    if e % 3 == 0:
        continue
    elif e % 3 == 1:
        print(e)
    else:
        print(0 - e)
print("game over")
