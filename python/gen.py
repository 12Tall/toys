# if a function has a 'yield' keyword,its called generator
def gen(count):
    i = 0
    sum = 0
    while(i<count):
        sum = sum + i
        i = i+1
        yield sum
    return

g = gen(4)
print(g)
print(next(g))
print(next(g))

# there is a sender in generator
def gen2():
    # defined before use
    val = None
    while True:
        rec = yield val
        if rec == "exit":
            break
        val = "got:%s"%rec
g2 = gen2()
# must send None first
print(g2.send(None))
print(g2.send("12tall"))
print(g2.send(12))
print(g2.send("exit"))

# yield from: get item in list .etc
# yield: get instance


            
