
class Tree:
    def __init__(self):
        self.leaves = 1000

    def __str__(self):
        """Returns string that should be displayed on print"""
        return f"Baum mit {self.leaves} Blätter"

    def __add__(self, other):
        """
        t1 + t2 --> Dann ist t2 das "other" argument
        """

        result = Tree()
        result.leaves = self.leaves + other.leaves
        return result


t = Tree()
t2 = Tree()
t2.leaves = 140

print(t)   # outputs Baum mit 1000 Blätter
print(t2)

t3 = t + t2  # gibt uns hoffentlich einen Baum mit 1140 blättern
# genau das gleiche, wie
# t4 = t.__add__(t2)

t4 = t + t2 + t3
# thats the EXACT same thing as

t4 = t.__add__(t2.__add__(t3))
print(t3)
print(t4)  # outputs Baum mit 2280 Blätter

