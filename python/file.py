f=None
try:
    # path is not easy,abs or rel
    f=open("toys/python/doc/file.txt","r")
    print(f.read())
except Exception as e:
    # catch exceptions
    print(e)
finally:
    if f:
        f.close()

print("done")

# like using in c#
with open("toys/python/doc/file.txt","r") as f:
    print(f.read())

# there are many choice in open()
# w wr rb wb or encoding
# aslo many options to read
# read(size) readline()

