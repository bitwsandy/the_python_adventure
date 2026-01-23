
# # Reading a file
# file_data = open(r"C:\Users\Sandeep\Desktop\data.txt", "r")
#
# # # Read Full Content of file
# # content = file_data.read()
# # print("content",content)
#
# # Read file line by line
# line1 = file_data.readline()
# print(f"line : {line1}")
#
# line2 = file_data.readline()
# print(f"line : {line2}")
#
# line3 = file_data.readline()
# print(f"line : {line3}")
#
# line4 = file_data.readline()
# print(f"line : {line4}")
#
# # line2 = file_data.readline()
# # print(line2)
#
# file_data.close()


# # Write to a file
# file_data = open(r"C:\Users\Sandeep\Desktop\data.txt", "w")
#
# content = "Nothing is Impossible (LOL)"
#
# file_data.write(content)
# file_data.close()



# # Append to a file
# file_data = open(r"C:\Users\Sandeep\Desktop\data.txt", "a")
#
# content = "\nNothing is Impossible (LOL)"
#
# file_data.write(content)
# file_data.close()


# # Write to a file which does not exist
# file_data = open(r"C:\Users\Sandeep\Desktop\katappa.txt", "w")
#
# content = "\nNothing is Impossible (LOL)"
#
# file_data.write(content)
# file_data.close()


# # Write to a file which does not exist
# file_data = open(r"C:\Users\Sandeep\Desktop\shivgami.txt", "a")
#
# content = "\nNothing is Impossible (LOL)"
#
# file_data.write(content)
# file_data.close()


# # Write to a file which does not exist
# file_data = open(r"C:\Users\Sandeep\Desktop\bhallaldev.txt", "r")
#
# content = file_data.read()
# print(content)
#
# file_data.close()

with open(r"C:\Users\Sandeep\Desktop\bhallaldev.txt", "r") as file_data :
    content = file_data.read()
    print(content)

print("DONE")



