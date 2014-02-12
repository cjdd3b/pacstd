import operator
from collections import defaultdict

class InvertedIndex(object):
    def __init__(self):
        self.index = {}
 
    def insert(self, tokens):
        k, v = tokens
        if not self.index.has_key(k):
            self.index[k] = defaultdict(int)
        self.index[k][v] += 1
        return

    def search(self, string):
        return dict(self.index[string]) if self.index.has_key(string) else None

    def search_top_n(self, string, n):
        return sorted(self.search(string).iteritems(), key=operator.itemgetter(1), reverse=True)[:n] \
            if self.index.has_key(string) else None