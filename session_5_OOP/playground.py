class Vector :
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector) :
            return Vector(self.x + other.x, self.y + other.y)
        else :
            print("Use Valid Vectors")

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(2, 3)

v3 = v1 + v2
# Vector.__add__(v1,v2)

sum = 10 + 15
print(f"Sum is : {sum}")

append = "abc" + " xyz"
print(f"Append is : {append}")

print(f"{v1} + {v2} = {v3}")