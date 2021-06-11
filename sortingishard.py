
class Weird:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __lt__(self, other):
        """This operator is <
        Less than"""
        # if self.b == other.b:  # the two characters are equal
        #     return self.a < other.a
        # else:                  # the two characters are different
        #     return self.b < other.b

        return self.b < other.b


    def __repr__(self):
        return f"Weird object with ({self.a}, {self.b})"


a = [10, 54, 3, 2]
# to sort: 10 < 54, 54 < 3, 3 < 2

b = ["hallo", "a", "b"]
# to sort: hallo < a, a < b

c = [Weird(10, 'a'), Weird(5, 'c'), Weird(100, 'b')]
# to sort Weird(10, 'a') < Weird(5, 'c') --> ERROR!

print(sorted(a))
print(sorted(b))
print(sorted(c))  # TypeError: '<' not supported between instances of 'Weird' and 'Weird'

print("hallo" < "a")  # this works, and it gives either True or False --> False
