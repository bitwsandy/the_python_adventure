
def deco1(func):
    def wrapper():
        print("Deco1")
        func()
    return wrapper

def deco2(func):
    def wrapper():
        print("Deco2")
        func()
    return wrapper

@deco1
@deco2
def greet_user():
    print("Hello User")

greet_user()