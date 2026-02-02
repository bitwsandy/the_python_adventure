
even_nums = [num for num in range(1,51) if num % 2 == 0]
# print(even_nums)

even_nums_generator = (num for num in range(1,51) if num % 2 == 0)

for num in even_nums_generator:
    print(num)