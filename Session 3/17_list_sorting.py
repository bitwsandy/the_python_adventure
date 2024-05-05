# Exercise 9: List Sorting
list_of_tuples = [('Alice', 25), ('Bob', 30), ('Charlie', 20), ('David', 35)]
sorted_list = sorted(list_of_tuples, key=lambda x: x[1], reverse=True)
print("Sorted list:", sorted_list)