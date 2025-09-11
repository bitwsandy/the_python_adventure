

# file = open(r"C:\Users\Sandeep\Desktop\data\wordcount.txt", 'r')

# print(file.readline())
# print(file.readline())
# print(file.readline())

# print(file.readlines())

# print(file.read())


# file = open(r"C:\Users\Sandeep\Desktop\data\wordcount_demo.txt", 'a')
#
# content = """\nGood Night"""
# file.write(content)
#
# file.close()

with open(r"C:\Users\Sandeep\Desktop\data\wordcount_demo.txt", 'a') as file :
    content = """\nGood Night"""
    file.write(content)

print("SUCCESS")








