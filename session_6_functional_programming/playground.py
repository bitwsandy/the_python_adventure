def make_multipliers_right():
    funcs = []
    for i in [1, 2, 3]:
        def inner(x, i=i):
            return x * i
        funcs.append(inner)
    return funcs

right = make_multipliers_right()

print(right[0](2))
print(right[1](3))
print(right[2](4))