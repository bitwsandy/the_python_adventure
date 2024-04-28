# Loops can also be controlled using keywords like "break" and "continue":
#
# Break: It allows you to exit the loop prematurely based on some condition.
# Continue: It allows you to skip the rest of the code inside the loop
# for the current iteration and jump to the next iteration.
# Here's a quick example using "break" and "continue":


for i in range(10):
    if i == 5:
        print(f"Iteration {i + 1}")
        break  # Exit the loop when i is 3
        print(f"i = {i} printing from if\n")
    elif i == 1:
        print(f"Iteration {i + 1}")
        continue  # Skip printing when i is 1
        print(f"i = {i}  printing from elif\n")
    else :
        print(f"Iteration {i + 1}")
        print(f"i = {i} printing from else\n")
