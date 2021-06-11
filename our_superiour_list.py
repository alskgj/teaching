"""
This is a list that is always sorted

>>> l = SuperList()
>>> l.append(1)
>>> l.append(5)
>>> l.append(3)
>>> print(l)
[1, 3, 5]


"""


class SuperList:

    def __init__(self):
        self.container = []

    def append(self, element):
        self.container.append(element)
        self.container.sort()

    def __str__(self):
        return str(self.container)


l = SuperList()
l.append(1)
l.append(5)
l.append(3)
print(l)
