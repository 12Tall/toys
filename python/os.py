import os
# posix nt--win
print(os.name)
# environment
print(os.environ)
# path
print(os.path.abspath("."))
# path join
print(os.path.join("~/","toys"))
# path split
pt = os.path.abspath("~/toys/python/doc/file.txt")
print(os.path.splitext(pt))
# rename remove but no copyfile method in os module
