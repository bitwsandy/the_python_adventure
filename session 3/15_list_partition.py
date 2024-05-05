# Exercise 5: List Partition
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
size = 3
partitioned_list = [original_list[i:i+size] for i in range(0, len(original_list), size)]
print("Partitioned list:", partitioned_list)
