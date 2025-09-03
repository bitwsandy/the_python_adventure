

def area_of_circle(r, pi=3.14):
    return pi * (r**2)

print(area_of_circle(10))


def greet(name, age=99, cno=9999999):
    print(f"Hello {name}")
    print(f"Your age is {age}")
    print(f"Your cno is {cno}")

greet("John")
greet("John", 33)
greet("John", 33, 33333333)


# This won't work, as parameters with default arguments must be mentioned
# after regular parameters

# def greet(name="User", age, cno):
#     print(f"Hello {name}")
#     print(f"Your age is {age}")
#     print(f"Your cno is {cno}")


def greet(name, age, cno=777, email="NA", address="0"):
    print("Name : ", name)
    print("Age : ", age)
    print("cno : ", cno)
    print("email : ", email)
    print("Address : ", address)

# greet("John", 35, 8745, "john@abraham.com", "Gym")


greet(age=37, name="jane")



def find_max(name, *nums):
    print("Name : ", name)
    return max(nums)

print(find_max("John", 50, 75,))