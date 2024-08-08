# Exercise 5: List Partition
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
size = 3
partitioned_list = [original_list[i:i+size] for i in range(0, len(original_list), size)]
print("Partitioned list:", partitioned_list)


# `original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`:
#       Defines the original list.
#
# `size = 3`:
#       Specifies the size of each partitioned sublist.
#
# `[original_list[i:i+size] for i in range(0, len(original_list), size)]`:
#       This is a list comprehension that iterates over indices `i` of the original list.
#       - For each index `i`, it creates a sublist by slicing the original list
#         from index `i` to index `i+size`.
#         This slice operation creates a sublist of size `size` starting from index `i`.
#       - The `range(0, len(original_list), size)` part generates indices
#         in steps of `size`, effectively partitioning the original list into sublists.
