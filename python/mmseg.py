# -*-coding:UTF-8-*-
import sys
import codecs
from math import log
from collections import defaultdict

class Trie(object):
    class TrieNode:
        def __init__(self):
            self.val = 0
            self.trans={}

    def __init__(self):
        self.root = Trie.TrieNode()

    def __walk(self,trienode,ch):
        if ch in trienode.trans:
            trienode = trienode.trans[ch]
            return trienode,trienode.val
        else:
# https://blog.csdn.net/huntinggo/article/details/38154487
