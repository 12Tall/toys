# generate element when using
gen = (x * x for x in range(1,10))
print(gen)
# generator is stateable
print(next(gen))
for n in gen:
    print(n)
