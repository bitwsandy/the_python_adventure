
from math_operations import add
from list_operations import print_len
print("name of script main.py : __name__ : ", __name__)

def main_message():
    print("Hello World, I am MAIN !!")

print("Befor If..")

if __name__ == "__main__" :
    print_len("pipeline started")
    add(10,15)
    print_len([1,2,3])
    print_len("pipeline finished")

print_len("if end")





