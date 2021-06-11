
class Tree:

    superleaves = 50

    def __init__(self):
        self.leaves = 1000


t = Tree()
print(t.leaves)  # outputs 1000
t.leaves += 1
print(t.leaves)  # outputs 1001

print('t.superleaves:', t.superleaves)        # outputs 50
print('Tree.superleaves:', Tree.superleaves)  # outputs 50
# print(Tree().leaves)                            # this gives an error

# superleaves belongs to the class Tree
# leaves      belongs to the object t
# an object is an instanciation

t2 = Tree()
print(t2.leaves)  # outputs 1000

# forbidden!!!
# Tree.superleaves += 1
t.__class__.superleaves += 1
# t.__class__ == Tree


print(t.superleaves)     # outputs 51
print(t2.superleaves)    # outputs 50
print(Tree.superleaves)  # outputs 50

