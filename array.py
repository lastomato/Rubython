import random

class RbArray:
    def __init__(self, ary):
        self.ary = ary

    #def assoc(self, element):

    def at(self, index):
        return self.ary[index]

    def clear(self):
        self.ary = []
        return self.ary

    def compact(self):
        self.ary = filter(lambda e:e != None, self.ary)
        return self.ary

    def concat(self, new_ary):
        self.ary.extend(new_ary)
        return self.ary

    def count(self, e):
        c = 0
        for element in self.ary:
            if element == e:
                c += 1
        return c

    def length(self):
        return len(self.ary)