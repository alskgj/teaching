
"""
- auch eine klasse Tree
>>> t = Tree(50)
>>> print(t)
Baum mit 50 Ästen

>>> print(t + 30)
80

"""

class Tree:
    def __init__(self, leaves):
        self.leaves = leaves

    def __str__(self):
        return f"Baum mit {self.leaves} Ästen"

    def __add__(self, other):
        """ The + operator """
        leaves = self.leaves + other
        return leaves

    def __sub__(self, other):
        """ The - operator """
        leaves = self.leaves - other
        return leaves

    def __len__(self):
        """ The len() operator """
        return 100

    def __le__(self, other):
        """ Less equal, the <= operator """
        pass

    def __ge__(self, other):
        """ Greater equal, the >= operator"""
        pass

    def __eq__(self, other):
        """ == """
        pass

t = Tree(50)
print(t)
print(t+30)
print(t-20)
print(len(t))  # --> 100

t1 = Tree(100)
t2 = Tree(1000)

baumliste = [t2, t, t1]


