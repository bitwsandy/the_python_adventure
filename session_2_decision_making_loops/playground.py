
# from 1 to 100 print all numbers except multiples of 3 and
# skip all numbers after 70

for num in range(1,101):
    if num % 3 == 0:
        continue
    elif num > 70 :
        break
    else:
        print(num, end='\t')

