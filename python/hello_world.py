#!/usr/bin/env python3
# this comment clear .py file can be executed by double click  
# but should "chmod a+x filename.py" first

# -*- coding:utf-8 -*-
# using utf-8 charset

# comment begin with #
# comments in ''' '''
print("Enter your name first:")
name = input();
print("hello ",name);
# print a line even no '\n'
print("\nprint string\n")
print(r"print raw string\n")

# format string splited by '%' 
# single param can ignore quotes
# hope quote is right
print(r"%s"%("format string"))
# or using format function
# just like $"" in c#
print(r"{0} is {1}!".format(name,12))

# print multiline command style
# .py files will keep ...
print(""" multi
        ... line
        ... string""")


