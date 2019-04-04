print(range(1,11))
# range also means start <= index < end
print(list(range(1,11)))

# auto gen list to x*x
print([x * x for x in range(1,11)])

# add conditions
print([x * x for x in range(1,11) if x % 2 == 0])

# multi loop
print([m+n for m in "AB" for n in "ab"])

